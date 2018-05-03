import sqlite3
from peewee import Model, SqliteDatabase, CharField, IntegerField


DB = SqliteDatabase('btd.db')
DB.connect()


class Metronome(Model):
    name = CharField()
    bpm = IntegerField()

    class Meta:
        database = DB

DB.create_tables([Metronome])
DB.close()
