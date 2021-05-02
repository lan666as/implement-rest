from sqlalchemy.orm import Session

from . import models, schemas


def get_karyawan(db: Session, karyawan_id: int):
    return db.query(models.Karyawan).filter(models.Karyawan.id_karyawan == karyawan_id).first()

def get_karyawans(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Karyawan).offset(skip).limit(limit).all()

def create_karyawan(db: Session, karyawan: schemas.KaryawanCreate):
    db_karyawan = models.Karyawan(nama = karyawan.nama, posisi = karyawan.posisi)
    db.add(db_karyawan)
    db.commit()
    db.refresh(db_karyawan)
    return db_karyawan

def edit_karyawan(db: Session, karyawan_id: int, karyawan: schemas.KaryawanCreate):
    db_karyawan = db.query(models.Karyawan).filter(models.Karyawan.id_karyawan == karyawan_id).first()
    db_karyawan.nama = karyawan.nama
    db_karyawan.posisi = karyawan.posisi
    db.add(db_karyawan)
    db.commit()
    db.refresh(db_karyawan)
    return db_karyawan

def delete_karyawan(db: Session, karyawan_id: int):
    db_karyawan = db.query(models.Karyawan).filter(models.Karyawan.id_karyawan == karyawan_id).first()
    db.delete(db_karyawan)
    db.commit()
    return db_karyawan