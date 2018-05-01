import sqlite3
from peewee import Model, SqliteDatabase, CharField


DB = SqliteDatabase('btd.db')
DB.connect()


class Metronome(Model):
    id_metronome = IntegerField()
    name = CharField()
    bpm = IntegerField()

    class Meta:
        database = DB

DB.create_table(Metronome)
DB.close()
