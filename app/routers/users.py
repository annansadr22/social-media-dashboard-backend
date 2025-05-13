from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User
from app.schemas import UserProfileResponse, UserProfileUpdate, AdminPromotionResponse
from app.routers.auth import SECRET_KEY, ALGORITHM
from jose import JWTError, jwt
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

router = APIRouter()
security = HTTPBearer()  # ✅ JWT-style Bearer token

# ✅ Dependency to extract user from JWT
def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid credentials")

        user = db.query(User).filter(User.email == email).first()
        if user is None:
            raise HTTPException(status_code=401, detail="User not found")

        return user
    except JWTError:
        raise HTTPException(status_code=401, detail="Token verification failed")
    
def admin_required(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid credentials")

        user = db.query(User).filter(User.email == email).first()
        if not user or not user.is_admin:
            raise HTTPException(status_code=403, detail="Admin access required")

        return user
    except JWTError:
        raise HTTPException(status_code=401, detail="Token verification failed")

# ✅ Get user profile
@router.get("/profile", response_model=UserProfileResponse)
def get_user_profile(current_user: User = Depends(get_current_user)):
    return current_user

# ✅ Update user profile
@router.put("/profile", response_model=UserProfileResponse)
def update_user_profile(
    profile_data: UserProfileUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    current_user.name = profile_data.name
    current_user.bio = profile_data.bio
    current_user.age = profile_data.age
    current_user.hobbies = profile_data.hobbies
    db.commit()
    db.refresh(current_user)
    return current_user

#To get all user (Admin only)
@router.get("/all", response_model=list[UserProfileResponse])
def get_all_users(
    db: Session = Depends(get_db),
    current_admin: User = Depends(admin_required)
):
    users = db.query(User).all()
    return users

