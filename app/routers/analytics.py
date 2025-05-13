from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Post, Analytics
from app.schemas import PostAnalyticsResponse
from app.routers.users import get_current_user
import random

router = APIRouter()

@router.get("/{post_id}", response_model=PostAnalyticsResponse)
def get_post_analytics(post_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    if post.user_id != current_user.id and not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Not authorized")

    # Check if analytics already exist; if not, generate mock data and store
    analytics = db.query(Analytics).filter(Analytics.post_id == post_id).first()
    if not analytics:
        analytics = Analytics(
            post_id=post_id,
            likes=random.randint(100, 500),
            shares=random.randint(20, 100),
            views=random.randint(1000, 5000)
        )
        db.add(analytics)
        db.commit()
        db.refresh(analytics)

    return analytics
