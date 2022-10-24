import asyncio

from models import LokerData, Users, Loker
from utils import ainput


async def tambah(user: Users, loker: Loker):
    if (is_opened := await LokerData.filter(user=user, loker=loker, is_opened=False)) and not is_opened[0].is_opened:
        print("Maaf, Loker Tidak bisa dibuka lagi.\n")
        await asyncio.sleep(2)
        from .dashboard import dashboard
        return await dashboard(user)
    print("""
WARNING!!!

Loker ini hanya bisa dibuka sekali saja!
Admin tidak bertanggungjawab atas kesalahan penginputan data.
Maka dari itu, masukkan data dengan benar!""")
    data_input = await ainput("Silakan masukkan data disini\nJika sudah, ketik qexit\n")
    datas = []
    while data_input.lower() != "qexit":
        datas.append(data_input)
        data_input = await ainput("")
    await LokerData.create(user=user, loker=loker, data=datas, is_opened=False)
    print("""
Data terekam!
Setelah ini, Anda tidak bisa merubah data yang telah tersimpan.
Silakan hapus data terlebih dahulu jika ingin merubah data.""")
    await asyncio.sleep(2)
    from .dashboard import dashboard
    return await dashboard(user)
