from tortoise import Model, fields


class Users(Model):
    id = fields.IntField(pk=True)
    nik = fields.CharField(max_length=50)
    nama = fields.CharField(max_length=100)
    telepon = fields.BigIntField(unique=True)
    email = fields.CharField(max_length=100, unique=True)
    is_admin = fields.BooleanField(default=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
