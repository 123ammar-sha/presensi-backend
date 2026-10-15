from sqlalchemy import Column, Integer, String, Text, Enum
from app.database import Base
import enum

# enum untuk role

class UserRole(str, enum.Enum):
    admin = "admin"
    karyawan = "karyawan"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password =Column(String(255), nullable=False)
    role = Column(Enum(UserRole), default=UserRole.karyawan, nullable=False)

    #data face encoding disimpan dalam JSON string dari array numpy
    face_encoding = Column(Text, nullable=True)