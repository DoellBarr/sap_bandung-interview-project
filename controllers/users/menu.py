from utils import ainput


async def menu():
    choice = await ainput("""
Halo User!

Silakan pilih menu dibawah ini:
1. Registrasi
2. Sewa Loker
3. Pengembalian Loker
4. Dashboard Loker

0. Kembali ke Menu Awal
99. Keluar
Pilih Menu Disini: """)
    while choice not in {"0", "1", "2", "3", "4", "99"}:
        print("Pilihlah menu yang sudah disediakan")
        choice = await ainput("")
    if choice == "0":
        from main import main
        return await main(True)
    if choice == "99":
        return print("Terima kasih telah menggunakan aplikasi ini!")
    if choice == "1":
        from .register import register
        return await register()
    if choice == "2":
        from controllers.loker import sewa
        return await sewa.sewa()
    if choice == "3":
        from controllers.loker import pengembalian
        return await pengembalian.pengembalian()
    if choice == "4":
        from controllers.loker import dashboard
        return await dashboard()
