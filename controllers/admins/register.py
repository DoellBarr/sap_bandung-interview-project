from models import Users
from controllers import users
from utils import ainput


async def register(mail: str = None):
    prompt = """
Halo Calon Admin!

Silakan masukkan email Anda: """
    email = await ainput(prompt)
    if not await Users.get_or_none(email=email):
        print("Email Anda tidak terdaftar")
        print("Silakan Daftar sebagai user terlebih dahulu")
        c_input = await ainput(
            "Tekan enter untuk pergi ke menu pendaftaran user.\nDan ketik 0 untuk kembali ke menu awal: "
        )
        if c_input == "0":
            from .menu import menu
            return await menu(mail)
        return await users.menu()
