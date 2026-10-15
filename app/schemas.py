from pydantic import BaseModel, EmailStr
from app.models import UserRole
from typing import Optional

# Skema untuk Registrasi User Baru
class UserCreate(BaseModel):
    nama: str
    email: EmailStr
    password: str
    role: Optional[UserRole] = UserRole.karyawan
    face_encoding: Optional[str] = None  # Menyimpan data string face encoding nantinya

# Skema data yang dikembalikan ke Client (Tanpa password demi keamanan)
class UserResponse(BaseModel):
    id: int
    nama: str
    email: EmailStr
    role: UserRole

    class Config:
        from_attributes = True

# Skema untuk Login
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Skema untuk Token JWT Response
class Token(BaseModel):
    access_token: str
    token_type: str