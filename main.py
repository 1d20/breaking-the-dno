from flask import Flask, render_template, request
from models import Metronome

app = Flask(__name__)


@app.route('/metronome/channel')
def channel():
    rows = list(Metronome.select(Metronome.name, Metronome.bpm, Metronome.id))
    return render_template('channel.html', rows=rows)


@app.route('/metronome/channel/<ID>')
def channel_id(ID):
    return render_template('channel_id.html', ID=ID)

@app.route('/metronome/delete/<ID>')
def channel_delete_id(ID):
    query = Metronome.delete().where(Metronome.id == ID)
    query.execute()
    return channel()

@app.route('/metronome/create', methods=['POST'])
def channel_create():
    name = request.form['name']
    Metronome.get_or_create(name=name, bpm=40)
    return channel()
