import sqlite3
from peewee import Model, SqliteDatabase, CharField, IntegerField, TextField


DB = SqliteDatabase('btd.db')
DB.connect()


class Metronome(Model):
    name = CharField()
    bpm = IntegerField()


    class Meta:
        database = DB


class Lyrics(Model):
    title_text = CharField()
    text = TextField()


    class Meta:
        database = DB

DB.create_tables([Metronome, Lyrics])
DB.close()
