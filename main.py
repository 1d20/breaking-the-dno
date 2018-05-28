from flask import Flask, render_template, request, redirect, url_for
from models import Metronome, Lyrics, Tabs, Songs


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
    return render_template('index.html')


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


@app.route('/songs')
def songs():
    rows_bpm = list(Metronome.select(Metronome.name, Metronome.bpm, Metronome.id))
    rows_title_text = list(Lyrics.select(Lyrics.title_text, Lyrics.id))
    rows_link = list(Tabs.select(Tabs.name, Tabs.id, Tabs.link))

    results = Songs.select(Songs.name, Songs.id, Songs.text, Songs.tabs, Songs.bpm)
    cover = request.args.get('cover')
    if cover:
        results = results.where(Songs.cover == int
            (cover))
    return render_template('songs.html', rows=list(results), rows_bpm=rows_bpm, rows_title_text=rows_title_text, rows_link=rows_link)


@app.route('/songs/create', methods=['POST'])
def songs_create():
    name = request.form['name']
    title_text = request.form['title_text']
    text = Lyrics.get(Lyrics.title_text == title_text).id
    bpm_start = request.form['bpm']
    bpm = Metronome.get(Metronome.name == bpm_start).id
    link_start = request.form['link']
    link = Tabs.get(Tabs.name == link_start).id
    option = request.form['optionsRadios']
    if option == "option1":
        cover = True
    else: 
        cover = False
    Songs.get_or_create(name=name, text=text, tabs=link, bpm=bpm, cover=cover)
    return redirect(url_for('songs'))


@app.route('/songs/delete/<ID>')
def songs_delete_id(ID):
    query = Songs.delete().where(Songs.id == ID)
    query.execute()
    return redirect(url_for('songs'))


@app.route('/songs/<ID>')
def songs_id(ID):
    song = Songs.get(Songs.id == ID)
    return render_template('songs_id.html', song=song)


if __name__ == "__main__":
    app.run(debug=True) 
