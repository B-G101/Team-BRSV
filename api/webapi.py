import random
from flask import Blueprint, jsonify
api_bp = Blueprint('api', __name__,
                   url_prefix='/api',
                   template_folder='templates',
                   static_folder='static', static_url_path='static/api')

songs = []
song_list = [
    {'name':"Before You Go", 'artist':"Lewis Capaldi", 'releaseYear':2019},
    "Toxic by Brittney Spears",
    "God’s Plan by Drake",
    "Firework by Katy Perry",
    "Blinding Lights by The Wknd",
    "Hips Don't Lie by Shakira",
    "No Tears Left to Cry by Ariana Grande (our queen)",
    "Party in the U.S.A. by Miley Cyrus",
    "Bad Guy by Billie Eilish",
    "Royals by Lorde",
    "Starships",
    "Sorry by Justin Bieber (ew)",
    "Titanium by Sia ",
    "Happy",
    "Hotline Bling by Drake",
    "Dancing Queen by ABBA",
    "Good Vibrations",
    "Bohemian Rhapsody by Queen",
    "Hey Jude",
    "One",
    "Waterloo Sunset",
    "Live Forever",
    "The Twist",
    "Stairway To Heaven",
    "Your Song",
    "Hotel California",
    "London Calling",
    "Sweet Child O'Mine",
    "Cream by Wu-tang Clan",
    "In da Club by 50 Cent",
    "Big Pimpin' by Jay Z",
    "Insane in the Brain by Cypress Hill",
    "Industry Baby",
    "Blood on the Leaves by Kanye West",
    "Monster by Kanye West",
    "Mrs. Jackson by Outcast",
    "Straight Outta Compton by NWA",
    "Jin and Juice by Snoop Dog",
    "Still Dre by Dr.Dre",
    "It was a Good Day by Ice Cube",
    "Dior by Pop Smoke",
    "Bad and Boujee by Migos",
    "The Box by Roddy Rich",
    "The Race by Tay-k",
    "Boom Boom Pow by Black Eye Peas",
    "Best Friend by Saweetie",
    "MONTERO by Lil Nas X",
    "Butterfly Effect by Travis Scott",
]

def _find_next_id():
    return max(songs["id"] for song in songs) + 1


def _init_songs():
    id = 1
    for song in song_list:
        songs.append({"id": id, "song": song,})
        id += 1



@api_bp.route('/song')
def get_song():
    if len(songs) == 0:
        _init_songs()
    return jsonify(random.choice(songs))


@api_bp.route('/songs')
def get_songs():
    if len(songs) == 0:
        _init_songs()
    return jsonify(songs)


if __name__ == "__main__":
    print(random.choice(song_list))