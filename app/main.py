from fastapi import FastAPI
from app.routers import auth

app = FastAPI(
    title="API Sistem presensi Geofencing & Face Recognition", 
    version="1.0.0", 
    description="Backend service menggunakan FastAPI untuk Frontend"
)


app.include_router(auth.router)
@app.get("/")
def read_root():
    return{"message": "Selamat datang di Backend Presensi API!", "status": "Running"}