from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.orm import Session
import jwt
from database import get_db
from models.user import User
from schemas import UserCreate, UserOut, Token
from utils import get_password_hash, verify_password, create_access_token
from config import SECRET_KEY, ALGORITHM

router = APIRouter(prefix="/auth", tags=["auth"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers = {"WWW-Authenticate":"Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms = [ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except jwt.PyJWTError:
        raise credentials_exception
    user = db.query(User).filter(User.username == username).first()
    
    if user is None:
        raise credentials_exception
    
    return user

@router.post("/register", response_model = UserOut, summary = 'Register a new user')
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    """Register a new user with username and password"""
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code = 400, detail = "Username already exists")
    hashed_password = get_password_hash(user.password)
    new_user = User(username = user.username, hashed_password = hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/token", response_model = Token, summary = "Login and create access token")
async def login_for_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    """Login with username and password to get access token"""
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Incorrect username or password",
            headers = {"WWW-Authenticate":"Bearer"},
        )
    access_token = create_access_token(data = {"sub": user.username})
    return {"access_token": access_token, "token_type": "Bearer"}

@router.get("/user/me", response_model = UserOut, summary = "Get current user details")
async def read_users_me(current_user: User = Depends(get_current_user)):
    """Receive information about the currently authenticated user"""
    return current_user



        

    
