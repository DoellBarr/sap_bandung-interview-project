from models import Loker, LokerDisewa, Users, LokerData
from utils import ainput
from datetime import datetime as dt


async def pengembalian():
    email = await ainput("Masukkan email Anda: ")
    user = await Users.get_or_none(email=email)
    if not user:
        await ainput("Email Anda tidak ditemukan, silakan tekan enter untuk pergi ke menu pendaftaran.")
        from controllers import users
        return await users.register()
    loker_sewa = await LokerDisewa.get_or_none(user=user, is_selesai_sewa=False)
    if not loker_sewa:
        print("Anda tidak memiliki loker yang disewa")
        return
    loker = await Loker.get(id=loker_sewa.loker_id)
    choice = await ainput("Apakah anda sudah selesai menggunakan loker? [y/n]: ")
    while choice not in ["y", "n"]:
        choice = await ainput("Apakah anda sudah selesai menggunakan loker? [y/n]: ")
    if choice == "y":
        lama_sewa = (dt.now() - loker_sewa.tanggal_sewa).days
        if lama_sewa > 2:
            loker_sewa.total_harga = (loker.harga * lama_sewa) * 0.2
        else:
            loker_sewa.total_harga = loker.harga * lama_sewa
        loker_sewa.is_selesai_sewa = True
        await loker_sewa.save()
        print("Terima kasih telah menggunakan loker kami")
        print(f"Total harga yang harus dibayar adalah {loker_sewa.total_harga}")
    else:
        loker_data = await LokerData.get_or_none(loker=loker, user=user, is_opened=True)
        if not loker_data:
            print("Anda tidak memiliki loker yang sedang dibuka\nSilakan hapus data terlebih dahulu")
            await ainput("Tekan enter untuk melanjutkan")
            from controllers.loker import dashboard
            return await dashboard()
    return print("Anda belum melakukan penyewaan")
