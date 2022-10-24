from typing import Callable
from models import Users
from utils import ainput


async def register(state: Callable = None):
    print("Register User")
    nik = await ainput("Silakan masukkan NIK Anda: ")
    if await Users.get_or_none(nik=nik):
        return print("Anda sudah pernah mendaftar!")
    nama = await ainput("Silakan masukkan nama Anda: ")
    telepon = await ainput("Silakan masukkan nomor telepon Anda: ")
    if await Users.get_or_none(telepon=telepon):
        return print("Nomor telepon sudah pernah digunakan")
    email = await ainput("Silakan masukkan email Anda: ")
    if await Users.get_or_none(email=email):
        return print("Email sudah pernah digunakan.")
    check = await ainput(f"""{'=' * 20}
Apakah input ini sudah benar?
NIK: {nik}
Nama: {nama}
Telepon: {telepon}
Email: {email}
{'='*20}

[y/n]: """)
    if check.lower() != 'y':
        return await register()
    await Users.create(nik=nik, nama=nama, telepon=telepon, email=email)
    print("User berhasil dibuat!")
    if state:
        return await state()
    from main import main
    return await main(True)
