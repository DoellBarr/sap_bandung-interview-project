import asyncio

from .show import show
from .register import register
from utils import ainput
from models import Users


async def menu(mail: str = None):
    text_menu = """
Halo Admin!

Silakan pilih menu berikut ini:
1. Menampilkan statistik
2. Penambahan Admin

0. Kembali ke Menu Awal
99. Keluar
Pilih Disini: """
    login = mail or await ainput("Silakan masukkan email Anda: ")
    mail = login
    if not await Users.get_or_none(email=mail):
        print("Email Anda tidak terdaftar")
        await asyncio.sleep(3)
        print("Daftarkan diri Anda terlebih dahulu melalui form user.")
        await asyncio.sleep(2)
        from main import main
        return await main(True)
    choice = await ainput(text_menu)
    while choice not in {"0", "1", "2", "99"}:
        print("Menu yang Anda berikan tidak ada, pilihlah menu yang tersedia!")
        choice = await ainput("")
    if choice == "0":
        from main import main
        return await main(True)
    if choice == "99":
        return print("Terima kasih telah menggunakan layanan kami!")
    if choice == "1":
        return await show(mail)
    if choice == "2":
        return await register(mail)
