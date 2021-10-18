from flask import Blueprint, render_template

from pathlib import \
    Path  # https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f

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


@app_starter.route('/songs', methods=['GET', 'POST'])
def songs():

    url = "http://127.0.0.1:5000/api/songs"

    response = requests.request("GET", url)
    return render_template("starter/songs.html", songs=response.json())


