from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User
from app.schemas import UserCreate, UserResponse, UserLogin, Token
from app.auth import get_password_hash, verify_password, create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

# Endpoint Registrasi Akun Baru
@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    # 1. Cek apakah email sudah terdaftar
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email sudah terdaftar di sistem."
        )
    
    # 2. Hash password sebelum disimpan ke database
    hashed_password = stvar = get_password_hash(user.password)
    
    # 3. Buat objek User baru
    new_user = User(
        nama=user.nama,
        email=user.email,
        hashed_password=hashed_password,
        role=user.role,
        face_encoding=user.face_encoding
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

# Endpoint Login untuk Mendapatkan Token JWT
@router.post("/login", response_model=Token)
def login_user(form_data: UserLogin, db: Session = Depends(get_db)):
    # 1. Cari user berdasarkan email
    user = db.query(User).filter(User.email == form_data.email).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email atau password salah.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # 2. Buat akses token JWT
    access_token = create_access_token(data={"sub": user.email, "role": user.role.value})
    
    return {"access_token": access_token, "token_type": "bearer"}