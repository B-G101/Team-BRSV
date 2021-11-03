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

old_songs = []
old_list = [
    {"id":52907687,"name":"Strange Fruit by Billie Holiday","photo":"https://www.youtube.com/watch?v=-DGY9HvChXk"},
    {"id":35506267,"name":"Smoke on the Water by Deep Purple","photo":"https://www.youtube.com/watch?v=zUwEIt9ez7M"},
    {"id":16807306,"name":"Indian Reservation by The Raiders","photo":"ndian Reservation by The Raiders"},
    {"id":63521043,"name":"Zombie by The Cranberries","photo":"https://www.youtube.com/watch?v=6Ejga4kJUts"},
    {"id":91132400,"name":"The Big Bang Theory by The Barenaked Ladies","photo":"https://www.youtube.com/watch?v=TzhIfN4UQv8"},
    {"id":74127064,"name":"Mesopotamia by The B-52's","photo":"https://www.youtube.com/watch?v=0FyLcHxbSRk"},
    {"id":30283700,"name":"Run To The Hills by Iron Maiden","photo":"https://www.youtube.com/watch?v=86URGgqONvA"},
    {"id":40834926,"name":"Oliver's Army by Elvis Costello","photo":"https://www.youtube.com/watch?v=LrjHz5hrupA&t=30s"},
    {"id":59676726,"name":"The Trooper by Iron Maiden","photo":"https://www.youtube.com/watch?v=X4bgXH3sJ2Q"},
    {"id":18959030,"name":"Mister Custer by Larry Verne","photo":"https://www.youtube.com/watch?v=vXuPJNXjlRM"},
    {"id":19220801,"name":"Rasputin by Boney-M","photo":"https://www.youtube.com/watch?v=16y1AkoZkmQ"},
    {"id":41880845,"name":"Enola Gay by Orchestral Manoeuvres In The Dark","photo":"https://www.youtube.com/watch?v=d5XJ2GiR6Bo"},
    {"id":38744009,"name":"Raised by Wolves by U2","photo":"https://www.youtube.com/watch?v=xt0vGieEWFA"},
    {"id":46032709,"name":"P.L.U.C.K. by System of a Down","photo":"https://www.youtube.com/watch?v=VxVzT0znI8Q"},
    {"id":63172387,"name":"Brighter Than a Thousand Suns by Iron Maiden","photo":"https://www.youtube.com/watch?v=Cx_yCoPP1EY"},
    {"id":23127852,"name":"The Wreck of the Edmund Fitzgerald by Gordon Lightfoot","photo":"https://www.youtube.com/watch?v=9vST6hVRj2A"},
    {"id":91913599,"name":"The British Are Coming by Weezer","photo":"https://www.youtube.com/watch?v=jGUPsdOCZ-A"},
    {"id":34324158,"name":"The Longest Day by Iron Maiden","photo":"https://www.youtube.com/watch?v=JDCgvcH301A"},
    {"id":54027019,"name":"The Infanta by The Decemberists","photo":"https://www.youtube.com/watch?v=nFlTBJdpy5A"},
    {"id":49932101,"name":"Mississippi Goddam by Nina Simone","photo":"https://www.youtube.com/watch?v=LJ25-U3jNWM"},
    {"id":28040377,"name":"Battle of New Orleans by Johnny Horton","photo":"https://www.youtube.com/watch?v=__uFnEMJqjg"},
    {"id":34061331,"name":"Buffalo Soldier by Bob Marley","photo":"https://www.youtube.com/watch?v=S5FCdx7Dn0o"},
    {"id":24724551,"name":"American Witch by Rob Zombie","photo":"https://www.youtube.com/watch?v=MdKXShP_oc4"}
]
def _find_next_id():
    return max(songs["id"] for song in songs) + 1


def _init_songs():
    id = 1
    for song in song_list:
        songs.append({"id": id, "song": song,})
        id += 1

def _init_oldsongs():
    id = 1
    for song in old_list:
        old_songs.append({"id": id, "song": song,})
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
    def _find_next_id():
        return max(song["id"] for song in song) + 1


@api_bp.route('/oldisgold')
def get_oldsong():
    if len(old_songs) == 0:
        _init_oldsongs();
    return jsonify(random.choice(old_songs))
