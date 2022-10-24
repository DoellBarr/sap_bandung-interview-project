from tortoise import Tortoise
import asyncio
from controllers import admins, users
from utils import ainput


async def init_db():
    await Tortoise.init(
        db_url='postgres://abdul:root@localhost:5432/loker', # database url format: postgres://username:password@host:port/database
        modules={'models': ["models"]}
    )
    await Tortoise.generate_schemas()


async def main(is_init: bool = False):
    if not is_init:
        await init_db()
    text_menu = """
Halo User!
Selamat datang di tempat penyewaan loker!

Role Tersedia:
1. Admin
2. User

Jika Anda bukan bagian dari staff, maka Anda harus memilih role nomor 2 (User)!

Silakan pilih role, jika ingin keluar dari program ketik q atau exit: """
    choice = await ainput(text_menu)
    while choice not in {"q", "1", "2"}:
        print("Menu tersebut tidak tersedia, pilihlah menu tersedia!")
        choice = await ainput("")
    if choice.lower() in {"q", "exit", r"\q"}:
        return print("Terima kasih telah menggunakan aplikasi ini!")
    return await admins.menu() if choice == "1" else await users.menu()


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
