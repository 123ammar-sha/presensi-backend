from app.database import engine,Base
from app.models import User

def init_db():
    print("Menghubungkan ke database Supabase...")
    Base.metadata.create_all(bind=engine)
    print("Tabel berhasil dibuat di supabase!")

if __name__ == "__main__":
    init_db()