import sys
from datetime import datetime as dt
from models import Loker, LokerDisewa, Users
from utils import ainput


async def sewa():
    loker_tersedia = await Loker.all().count() - await LokerDisewa.filter(is_selesai_sewa=False).count()
    loker_kecil = await Loker.filter(tipe=0).count() - await LokerDisewa.filter(is_selesai_sewa=False).count()
    loker_gede = await Loker.filter(tipe=1).count() - await LokerDisewa.filter(is_selesai_sewa=False).count()
    harga_loker_kecil = (await Loker.get_or_none(tipe=0)).harga
    harga_loker_gede = (await Loker.get_or_none(tipe=1)).harga
    prompt = f"""
Halo User

Jumlah loker tersedia adalah: {loker_tersedia} loker

Berikut loker yang tersedia:
1. Loker Kecil, tersedia: {loker_kecil}, harga: {harga_loker_kecil}/hari
2. Loker Besar, tersedia: {loker_gede}, harga: {harga_loker_gede}/hari

Note:
Maksimal sewa untuk setiap lokernya adalah dua hari...
Apabila Anda menyewa lebih dari dua hari, maka Anda akan dikenakan denda sebesar 20% dari total harga.

Pilih loker yang anda ingin sewa: """
    pilihan = await ainput(prompt)
    while pilihan not in {"1", "2"}:
        print("Pilihan tidak ditemukan, pilihlah pilihan yang ada")
        pilihan = await ainput("")
    email = await ainput("Masukkan email anda disini: ")
    if not await Users.get_or_none(email=email):
        await ainput("Email anda tidak ditemukan, silakan tekan enter untuk pergi ke menu pendaftaran.")
        from controllers import users
        return await users.register(state=sewa)
    total_harga = harga_loker_kecil if pilihan == "1" else harga_loker_gede
    info = f"""
{'=' * 20}
Anda menyewa:

Loker: {'Kecil' if pilihan == "1" else 'Besar'}
Dengan harga total: {total_harga}

Apakah data ini sudah benar? [y/n]: """
    choice = await ainput(info)
    if choice.lower() == "y":
        loker = await Loker.get(tipe=int(pilihan))
        user = await Users.get(email=email)
        lokers = await LokerDisewa.create(
            loker=loker,
            user=user,
            total_harga=total_harga,
            tanggal_sewa=dt.now(),
        )
        await ainput(
            f"""
Loker berhasil disewa!

Harap diingat! Pin loker anda yaitu {lokers.loker.pin}

Jika sudah dicatat, tekan apapun lalu enter untuk pergi ke dashboard loker"""
        )
        from controllers import loker
        return await loker.dashboard(user, loker=lokers)
    choice = await ainput("Apakah anda ingin mengulangi input? [y/n]: ")
    if choice.lower() == "n":
        print("Terimakasih telah berkunjung ke digital loker!")
        sys.exit()
    return await sewa()
