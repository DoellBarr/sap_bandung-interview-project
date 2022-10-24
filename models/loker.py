from tortoise import Model, fields


class Loker(Model):
    id = fields.IntField(pk=True)
    tipe = fields.SmallIntField(default=0, description="0: Kecil, 1: Besar")
    harga = fields.IntField()
    pin = fields.IntField()
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)


class LokerDisewa(Model):
    id = fields.IntField(pk=True)
    loker = fields.ForeignKeyField('models.Loker', related_name='loker_disewa')
    user = fields.ForeignKeyField('models.Users', related_name='loker_disewa')
    total_harga = fields.IntField()
    tanggal_sewa = fields.DatetimeField()
    is_selesai_sewa = fields.BooleanField(default=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)


class LokerData(Model):
    id = fields.IntField(pk=True)
    loker = fields.ForeignKeyField('models.Loker', related_name='loker_data')
    user = fields.ForeignKeyField('models.Users', related_name='loker_data')
    is_opened = fields.BooleanField(default=True)
    data = fields.JSONField()
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
