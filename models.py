import sqlite3
from peewee import Model, SqliteDatabase, CharField, IntegerField, TextField, ForeignKeyField, BooleanField


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


class Tabs(Model):
    name = CharField()
    link = CharField()


    class Meta:
        database = DB


class Songs(Model):
    name = CharField()
    text = ForeignKeyField(Lyrics)
    tabs = ForeignKeyField(Tabs)
    bpm = ForeignKeyField(Metronome)
    cover = BooleanField()


    class Meta:
        database = DB


DB.create_tables([Metronome, Lyrics, Tabs, Songs])
DB.close()
