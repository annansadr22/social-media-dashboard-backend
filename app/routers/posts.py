from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Post, User
from app.schemas import PostCreate, PostUpdate, PostResponse, PostFilterRequest
from app.routers.users import get_current_user, admin_required

router = APIRouter()

# ✅ Create a new post
@router.post("/", response_model=PostResponse)
def create_post(post: PostCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_post = Post(**post.dict(), user_id=current_user.id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

# ✅ Get current user's posts
@router.get("/", response_model=list[PostResponse])
def get_my_posts(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(Post).filter(Post.user_id == current_user.id).all()

# ✅ Get all posts (admin only)
@router.get("/all", response_model=list[PostResponse])
def get_all_posts(db: Session = Depends(get_db), current_user: User = Depends(admin_required)):
    return db.query(Post).all()

# ✅ Update a post (only by owner)
@router.put("/{post_id}", response_model=PostResponse)
def update_post(post_id: int, post: PostUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_post = db.query(Post).filter(Post.id == post_id, Post.user_id == current_user.id).first()
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found or not yours")

    for key, value in post.dict(exclude_unset=True).items():
        setattr(db_post, key, value)

    db.commit()
    db.refresh(db_post)
    return db_post

# ✅ Delete a post (only by owner)
@router.delete("/{post_id}", response_model=dict)
def delete_post(post_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_post = db.query(Post).filter(Post.id == post_id, Post.user_id == current_user.id).first()
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found or not yours")

    db.delete(db_post)
    db.commit()
    return {"message": "Post deleted successfully"}

#Filter of user's post(Limited to their own posts)
@router.post("/filter", response_model=list[PostResponse])
def filter_user_posts(
    filters: PostFilterRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    query = db.query(Post).filter(Post.user_id == current_user.id)

    if filters.content:
        query = query.filter(Post.content.ilike(f"%{filters.content}%"))

    if filters.platform:
        query = query.filter(Post.platform.ilike(f"%{filters.platform}%"))

    if filters.status:
        query = query.filter(Post.status.ilike(f"%{filters.status}%"))
        
    if filters.from_date:
        query = query.filter(Post.scheduled_time >= filters.from_date)

    if filters.to_date:
        query = query.filter(Post.scheduled_time <= filters.to_date)

    # ✅ Apply sort order
    if filters.sort_order == "asc":
        query = query.order_by(Post.scheduled_time.asc())
    else:
        query = query.order_by(Post.scheduled_time.desc())

    return query.all()


#Filtering by Admin (All posts)
@router.post("/filter/all", response_model=list[PostResponse])
def filter_all_posts(
    filters: PostFilterRequest,
    db: Session = Depends(get_db),
    current_admin: User = Depends(admin_required)
):
    query = db.query(Post)

    if filters.content:
        query = query.filter(Post.content.ilike(f"%{filters.content}%"))

    if filters.platform:
        query = query.filter(Post.platform.ilike(f"%{filters.platform}%"))

    if filters.status:
        query = query.filter(Post.status.ilike(f"%{filters.status}%"))

    if filters.from_date:
        query = query.filter(Post.scheduled_time >= filters.from_date)

    if filters.to_date:
        query = query.filter(Post.scheduled_time <= filters.to_date)

    if filters.sort_order == "asc":
        query = query.order_by(Post.scheduled_time.asc())
    else:
        query = query.order_by(Post.scheduled_time.desc())

    return query.all()
