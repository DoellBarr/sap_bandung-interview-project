from models import Users, Loker, LokerData
from utils import ainput


async def delete(user: Users, loker: Loker):
    choice = await ainput("Apakah Anda yakin ingin menghapus data? (y/n): ")
    while choice.lower() not in {"y", "n"}:
        choice = await ainput("Silakan pilih pilihan yang sudah tersedia: ")
    if choice.lower() == "y":
        if lok_data := await LokerData.get_or_none(user=user, loker=loker):
            await lok_data.delete()
            return print("Data berhasil dihapus!")
        return print("Maaf, Anda belum melakukan penyewaan")
    print("Data tidak dihapus")
    from .dashboard import dashboard
    return await dashboard(user, loker)
