from models import Users
from utils import ainput


async def show(email: str = None):
    total = await Users.all().count()
    print(f"Total User Terdaftar: {total}")
    await ainput("Tekan enter untuk kembali ke menu awal")
    from controllers import admins
    return await admins.menu(email)
