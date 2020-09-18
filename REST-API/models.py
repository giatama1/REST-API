from peewee import *

db = SqliteDatabase('merempahdb.db')

class Data_user(Model):
    rowid = AutoField(primary_key=True)
    nama_user = CharField()
    alamat_user = CharField()
    noHp_user = CharField()
    email_user = CharField()

    class Meta:
        database = db

def initialize():
    db.connect()
    db.create_tables([Data_user],safe=True)
    db.close()


