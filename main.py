from flask import Flask, render_template, request, redirect, url_for
from models import Metronome

app = Flask(__name__,static_url_path="/static")


@app.route('/metronome/channel')
def channel():
    rows = list(Metronome.select(Metronome.name, Metronome.bpm, Metronome.id))
    return render_template('channel.html', rows=rows)

@app.route('/metronome/channel/<ID>')
def channel_id(ID):
    rows = list(Metronome.select(Metronome.name, Metronome.bpm, Metronome.id))
    bpm = Metronome.get(Metronome.id == ID).bpm
    name = Metronome.get(Metronome.id == ID).name
    return render_template('channel_id.html', ID=ID, rows=rows, bpm=bpm, name=name)

@app.route('/metronome/delete/<ID>')
def channel_delete_id(ID):
    query = Metronome.delete().where(Metronome.id == ID)
    query.execute()
    return redirect(url_for('channel'))

@app.route('/metronome/create', methods=['POST'])
def channel_create():
    name = request.form['name']
    Metronome.get_or_create(name=name, bpm=40)
    return redirect(url_for('channel'))

@app.route('/metronome/update/<ID>', methods=['POST'])
def bpm_save(ID):
    bpm = request.form['number']
    query = Metronome.update(bpm=bpm).where(Metronome.id == ID)
    query.execute()
    return redirect(url_for('channel'))

@app.route("/") 
def hello(): 
    return redirect(url_for('channel'))


if (__name__ == "__main__"): 
    app.run(port = 5000) 
