from peewee import *

db = SqliteDatabase('merempahdb.db')


class Data_user(Model):
    rowid = AutoField(primary_key=True)
    nama_user = CharField()
    password = CharField()
    nama_lengkap_user = CharField()
    alamat_user = CharField(null=True)
    noHp_user = CharField()
    email_user = CharField()

    class Meta:
        database = db


class Data_product(Model):
    row_id = AutoField(primary_key=True)
    product_id = CharField(null=True)
    product_name = CharField()
    product_description = CharField()
    product_price = IntegerField()
    product_image_url = CharField()
    user_id = ForeignKeyField(Data_user, backref="Data_product")

    class Meta:
        database = db


def initialize():
    db.connect()
    Data_user.create_table()
    Data_product.create_table()
    db.close()


# def dropTable():
#     Data_product.drop_table()
#     Data_user.drop_table()
