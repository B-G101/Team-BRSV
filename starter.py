from flask import Blueprint, render_template
import requests
from pathlib import \
    Path  # https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b5
app_starter = Blueprint('starter', __name__,
                        url_prefix='/starter',
                        template_folder='templates',
                        static_folder='static',
                        static_url_path='assets')


@app_starter.route('/song', methods=['GET', 'POST'])
def song():

    url = "http://127.0.0.1:5000/api/song"

    response = requests.request("GET", url)
    return render_template("starter/song.html", song=response.json())

@app_starter.route('/oldisgold', methods=['GET', 'POST'])
def oldisgold():

    url = "http://127.0.0.1:5000/api/oldisgold"
    response = requests.request("GET", url)
    return render_template("starter/song.html", song=response.json())

@app_starter.route('/countrytunes', methods=['GET', 'POST'])
def countrytunes():

    url = "http://127.0.0.1:5000/api/countrytunes"
    response = requests.request("GET", url)
    return render_template("starter/song.html", song=response.json())


@app_starter.route('/rap', methods=['GET', 'POST'])
def rap():

    url = "http://127.0.0.1:5000/api/rap"
    response = requests.request("GET", url)
    return render_template("starter/song.html", song=response.json())




@app_starter.route('/songs', methods=['GET', 'POST'])
def songs():

    url = "http://127.0.0.1:5000/api/songs"

    response = requests.request("GET", url)
    return render_template("starter/songs.html", songs=response.json())


