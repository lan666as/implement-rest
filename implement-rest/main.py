from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/karyawan/", response_model=schemas.Karyawan)
def create_karyawan(karyawan: schemas.KaryawanCreate, db: Session = Depends(get_db)):
    # db_karyawan = crud.get_karyawan_by_email(db, email=karyawan.email)
    # if db_karyawan:
    #     raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_karyawan(db=db, karyawan=karyawan)


@app.get("/karyawan/", response_model=List[schemas.Karyawan])
def read_karyawan(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    karyawan = crud.get_karyawans(db, skip=skip, limit=limit)
    return karyawan


@app.get("/karyawan/{karyawan_id}", response_model=schemas.Karyawan)
def read_karyawan(karyawan_id: int, db: Session = Depends(get_db)):
    db_karyawan = crud.get_karyawan(db, karyawan_id=karyawan_id)
    if db_karyawan is None:
        raise HTTPException(status_code=404, detail="Karyawan not found")
    return db_karyawan

@app.put("/karyawan/{karyawan_id}", response_model=schemas.Karyawan)
def read_karyawan(karyawan_id: int, karyawan: schemas.KaryawanCreate, db: Session = Depends(get_db)):
    db_karyawan = crud.edit_karyawan(db, karyawan_id=karyawan_id, karyawan=karyawan)
    if db_karyawan is None:
        raise HTTPException(status_code=404, detail="Karyawan not found")
    return db_karyawan

@app.delete("/karyawan/{karyawan_id}", response_model=schemas.Karyawan)
def read_karyawan(karyawan_id: int, db: Session = Depends(get_db)):
    db_karyawan = crud.delete_karyawan(db, karyawan_id=karyawan_id)
    if db_karyawan is None:
        raise HTTPException(status_code=404, detail="Karyawan not found")
    return db_karyawan