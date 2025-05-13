from fastapi import FastAPI
from app.database import Base, engine
from app.routers import auth, users, posts, analytics

app = FastAPI()

# Initialize the database (Auto-create tables)
Base.metadata.create_all(bind=engine)

# Register API routers
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(users.router, prefix="/api/users", tags=["Users"])
app.include_router(posts.router, prefix="/api/posts", tags=["Posts"])
app.include_router(analytics.router, prefix="/api/analytics", tags=["Analytics"])

@app.get("/")
def root():
    return {"message": "Database connected successfully"}
