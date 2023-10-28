from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt
from jwt import PyJWTError
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, MetaData, Table
from sqlalchemy.orm import Session
from databases import Database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database setup
DATABASE_URL = "postgresql://users:password@127.0.0.1:5432/users"
database = Database(DATABASE_URL)
metadata = MetaData()
Base = declarative_base()
engine = create_engine(DATABASE_URL)

# Define the 'users' table
users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("username", String, unique=True, index=True),
    Column("full_name", String),
    Column("email", String, unique=True, index=True),
    Column("hashed_password", String),
    Column("active", Boolean, default=True),
    Column("created_at", DateTime, default=datetime.utcnow),
)

SECRET_KEY = "e41f6b654b3e3f41e3a030ef783cbe2fec5824d5543a0d408ee3ba0677e1750a"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Create a FastAPI app
app = FastAPI()

# Initialize the database
Base.metadata.create_all(bind=engine)

# Hashing password
password_hash = CryptContext(schemes=["bcrypt"], deprecated="auto")

# User Pydantic model
class User(BaseModel):
    username: str
    full_name: str
    email: str

# Token Pydantic model
class Token(BaseModel):
    access_token: str
    token_type: str

# User registration
class UserInDB(User):
    password: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# User model
class UserDB(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

# Get user data
def get_user(db, username: str):
    return db.query(UserDB).filter(UserDB.username == username).first()

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)

def create_access_token(data, expires_delta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# OAuth2 password scheme for token generation
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Register a new user
@app.post("/register", response_model=User)
async def register(user: UserInDB, db: Session = Depends(get_db)):
    existing_user = get_user(db, user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed_password = password_hash.hash(user.password)
    new_user = UserDB(username=user.username, full_name=user.full_name, email=user.email, hashed_password=hashed_password)
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return User(username=new_user.username, full_name=new_user.full_name, email=new_user.email)

# Login and get JWT token
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    db = SessionLocal()  # Get the database session
    user = get_user(db, form_data.username)
    if user is None or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}

# Protected route
@app.get("/protected")
async def get_protected_data(current_user: User = Depends(oauth2_scheme)):
    return current_user
