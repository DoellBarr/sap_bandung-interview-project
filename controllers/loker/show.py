import asyncio

from models import Users, Loker, LokerData, LokerDisewa


async def show(user: Users, loker: Loker):
    if lok_data := await LokerData.get_or_none(user=user, loker=loker, is_opened=False):
        return print("Data Loker Anda: " + "\n".join(lok_data.data))
    print("Data Anda kosong\nSilakan tambah data terlebih dahulu")
    from .dashboard import dashboard
    return await dashboard(user)


async def show_ready_loker(mail):
    lokers = await Loker.all()
    print("Berikut adalah loker yang siap digunakan")
    for loker in lokers:
        print(f"{loker.id}. Loker {'Kecil' if loker.tipe == 0 else 'Besar'} - {loker.harga}/hari")
    await asyncio.sleep(2)
    from controllers import admins
    return await admins.menu(mail)


async def show_used(mail):
    lokers = await Loker.all()
    for loker in lokers:
        if lok_data := await LokerDisewa.get_or_none(loker=loker, is_selesai_sewa=False):
            user = await lok_data.user
            print(f"{loker.id}. {loker.tipe} - {loker.harga} - {user.email}")
        else:
            print(f"{loker.id}. {loker.tipe} - {loker.harga} - Tidak ada yang menyewa")
    await asyncio.sleep(2)
    from controllers import admins
    return await admins.menu(mail)
