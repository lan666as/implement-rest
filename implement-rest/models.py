from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Karyawan(Base):
    __tablename__ = "karyawan"

    id_karyawan = Column(Integer, primary_key=True, index=True)
    nama = Column(String, index=True)
    posisi = Column(String)