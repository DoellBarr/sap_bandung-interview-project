from utils import ainput


async def show(mail: str = None):
    prompt = """
Halo Admin!

Silakan pilih menu berikut ini:
1. Tampilkan Total User Terdaftar
2. Tampilkan Sisa Loker Tersedia
3. Tampilkan Loker Yang Digunakan

0. Kembali ke Menu Awal
99. Keluar
Pilih Disini: """
    choice = await ainput(prompt)
    while choice not in {"0", "1", "2", "3", "99"}:
        print("Menu yang Anda berikan tidak ada, pilihlah menu yang tersedia!")
        choice = await ainput("")
    if choice == "0":
        from controllers import admins
        return await admins.menu(mail)
    if choice == "99":
        return print("Terima kasih telah menggunakan layanan kami!")
    if choice == "1":
        from controllers import users
        return await users.show(mail)
    if choice == "2":
        from controllers import loker
        return await loker.show(mail)
    if choice == "3":
        from controllers import loker
        return await loker.show_used(mail)
