from typing import List, Optional

from pydantic import BaseModel


class KaryawanBase(BaseModel):
    nama: str


class KaryawanCreate(KaryawanBase):
    posisi: str


class Karyawan(KaryawanBase):
    id_karyawan: int
    posisi: str

    class Config:
        orm_mode = True