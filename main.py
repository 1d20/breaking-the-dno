from flask import Flask, render_template, request, redirect, url_for
from models import Metronome, Lyrics, Tabs

app = Flask(__name__, static_url_path="/static")


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
    return render_template('main.html')


@app.route("/metronome")
def metronome():
    return render_template('metronome.html')


@app.route("/lyrics")
def lyrics():
    rows = list(Lyrics.select(Lyrics.title_text, Lyrics.id))
    return render_template('lyrics.html', rows=rows)


@app.route('/lyrics/delete/<ID>')
def lyrics_delete_id(ID):
    query = Lyrics.delete().where(Lyrics.id == ID)
    query.execute()
    return redirect(url_for('lyrics'))


@app.route('/lyrics/create', methods=['POST'])
def lyrics_create():
    title_text = request.form['name']
    text = request.form['content']
    Lyrics.get_or_create(title_text=title_text, text=text)
    return redirect(url_for('lyrics'))


@app.route('/lyrics/<ID>')
def lyrics_id(ID):
    title_text = Lyrics.get(Lyrics.id == ID).title_text
    text = Lyrics.get(Lyrics.id == ID).text
    print(text)
    return render_template('lyrics_id.html', title_text=title_text, text=text)


@app.route("/tabs")
def tabs():
    rows = list(Tabs.select(Tabs.name, Tabs.id, Tabs.link))
    return render_template('tabs.html', rows=rows)


@app.route('/tabs/create', methods=['POST'])
def tabs_create():
    name = request.form['name']
    link = request.form['content']
    Tabs.get_or_create(name=name, link=link)
    return redirect(url_for('tabs'))


@app.route('/tabs/delete/<ID>')
def tabs_delete_id(ID):
    query = Tabs.delete().where(Tabs.id == ID)
    query.execute()
    return redirect(url_for('tabs'))


if (__name__ == "__main__"):
    app.run(port = 5000) 
