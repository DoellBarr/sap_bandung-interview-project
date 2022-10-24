from models import Users, LokerData, Loker, LokerDisewa
import asyncio
from utils import ainput


async def dashboard(user: Users = None, loker: LokerDisewa = None):
    if user is None or loker is None:
        email = await ainput("Silakan masukkan email Anda: ")
        user = await Users.get_or_none(email=email)
    if user is None:
        print("Email Anda tidak terdaftar")
        await asyncio.sleep(3)
        from main import main
        return await main(True)
    loker = await LokerDisewa.get_or_none(user=user)
    if loker is None:
        print("Anda tidak memiliki loker")
        await asyncio.sleep(3)
        from main import main
        return await main(True)
    if (lok_data := await LokerData.get_or_none(user=user, loker=loker)) and not lok_data.is_opened:
        return print("Maaf, Loker Tidak bisa dibuka lagi.\n")
    pin_input = await ainput(f"""
Hello {user.nama}!
Selamat Datang Di Dashboard Loker Anda!

Silakan masukkan pin loker Anda: """)
    while not pin_input.isdigit():
        print("Pin loker hanya berupa angka.")
        pin_input = await ainput("")
    loker = await loker.loker
    while int(pin_input) != loker.pin:
        pin_input = await ainput("Pin loker salah, silakan coba lagi: ")
    choice = await ainput("""
Sukses Masuk Loker!

Menu:
1. Tambah Data
2. Lihat Data
3. Hapus Data

0. Kembali ke Menu Awal
99. Keluar
Silakan Pilih Menu: """)
    while choice not in {"0", "1", "2", "3", "99"}:
        choice = await ainput("Silakan pilih pilihan yang sudah tersedia: ")
    if choice == "0":
        from main import main
        return await main(True)
    if choice == "99":
        return print("Terima kasih telah menggunakan layanan kami!")
    if choice == "1":
        from .tambah import tambah
        return await tambah(user, loker)
    if choice == "2":
        from .show import show
        return await show(user, loker)
    if choice == "3":
        from .delete import delete
        return await delete(user, loker)
