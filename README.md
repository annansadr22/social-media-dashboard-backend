# 📊 Social Media Dashboard (FastAPI)

A backend-powered social media analytics and management system built with **FastAPI** and **PostgreSQL**. It allows users to register, login, manage posts, view analytics, and filter data — with admin-level control over users and data.

---

## 🚀 Features

- ✅ User Registration & Login (JWT Authentication)  
- 🔐 Email Verification for Secure Access  
- 👥 Role-based Access (Admin vs User)  
- 📝 Create, Update, Delete Posts  
- 📊 Mock Analytics for Posts (views, likes, comments)  
- 🔍 Filter Posts by Date, Keyword, or User  
- ⚙️ Admin Panel to manage users and content  
- 🌐 Deployed on Render (or your preferred cloud provider)  

---

## 🛠 Tech Stack

- **Backend:** FastAPI  
- **Database:** PostgreSQL  
- **ORM:** SQLAlchemy  
- **Auth:** JWT (with optional Google OAuth)  
- **Migrations:** Alembic  
- **Environment Management:** Python-dotenv  

---

## 🌐 Live Demo

My app is already running on the cloud.  
👉 **Try this URL**:  
[https://social-media-dashboard-backend-pwn9.onrender.com/docs](https://social-media-dashboard-backend-pwn9.onrender.com/docs) 

This link opens the **inbuilt FastAPI Swagger UI** — an interactive documentation interface where you can explore and test all available endpoints directly from your browser.


---

## 💻 Run This Project Locally

To run this FastAPI project on your own machine:

### 1. Clone the Repository

```bash
git clone https://github.com/annansadr22/social-media-dashboard-backend.git
cd social-media-dashboard
```

### 2. Create & Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate         # On Windows: venv\Scripts\activate
```

### 3. Install the Requirements

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory and add:

```env
DATABASE_URL=postgresql://your_user:your_password@localhost/your_db_name
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```
Replace with your database connection string and also generate a good secret key

### 5. Run Database Migrations

```bash
alembic upgrade head
```
Run this so that your models get saved into your database

### 6. Start the FastAPI App

```bash
uvicorn app.main:app --reload
```

Now visit [http://localhost:8000/docs](http://localhost:8000/docs) to use the same Swagger UI locally.

---

## 📬 API Endpoints (Sample)

| Method | Endpoint           | Description             |
|--------|--------------------|-------------------------|
| POST   | /register          | Register a new user     |
| POST   | /login             | Login and get JWT token |
| GET    | /posts             | Get all posts           |
| POST   | /posts             | Create a post           |
| GET    | /analytics/{id}    | View analytics for post |
| GET    | /posts/filter      | Filter posts by query   |

These are some of the sample API Endpoints. You can explore more.

---

## 🔐 Authentication

- JWT tokens are used for securing API access.
- After login, send the token via:  
  `Authorization: Bearer <your_token_here>`

---

## 🧪 Testing

You can test the APIs using:

- 🛠 [Postman](https://www.postman.com/)
- 🌐 Swagger UI at `http://localhost:8000/docs`

---

## 🌍 Deployment (Render)

To deploy on [Render](https://render.com/):

1. Push code to GitHub  
2. Create a new web service on Render  
3. Add required environment variables from `.env`  
4. Connect to PostgreSQL via Render dashboard  
5. Done 🎉

---

## 🙌 Acknowledgements

Thanks to **FastAPI**, **SQLAlchemy**, and all open-source contributors who made this stack awesome.








