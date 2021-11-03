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
    "Strange Fruit by Billie Holiday",
    "Smoke on the Water by Deep Purple",
    "Indian Reservation by The Raiders",
    "Zombie by The Cranberries",
    "The Big Bang Theory by The Barenaked Ladies",
    "Mesopotamia by The B-52's",
    "Run To The Hills by Iron Maiden",
    "Oliver's Army by Elvis Costello",
    "The Trooper by Iron Maiden",
    "Mister Custer by Larry Verne",
    "Rasputin by Boney-M",
    "Enola Gay by Orchestral Manoeuvres In The Dark",
    "Raised by Wolves by U2",
    "P.L.U.C.K. by System of a Down",
    "Brighter Than a Thousand Suns by Iron Maiden",
    "The Wreck of the Edmund Fitzgerald by Gordon Lightfoot",
    "The British Are Coming by Weezer",
    "The Longest Day by Iron Maiden",
    "The Infanta by The Decemberists",
    "Mississippi Goddam by Nina Simone",
    "Battle of New Orleans by Johnny Horton",
    "Buffalo Soldier by Bob Marley",
    "American Witch by Rob Zombie",
    "I Walk the Line by Johnny Cash",
    "Jolene by Dolly Parton",
    "Friends in Low Places by Garth Brooks",
    "Choices by George Jones",
    "Concrete Angel by Martina McBride",
    "Kiss an Angel Good Morning Charley Pride",
    "Where Were You by Alan Jackson",
    "Live Like You Were Dying by Tim McGraw",
    "I Hope You Dance by Lee Ann Womack",
    "Take Me Home Country Roads by John Denver",
    "Walkin' After Midnight by Patsy Cline",
    "Breathe by Faith Hill",
    "Before He Cheats by Carrie Underwood",
    "Follow Your Arrow by Kacey Musgraves",
    "Blue Eyes Crying in the Rain by Willie Nelson",
    "Somebody Like You by Keith Urban",
    "Devil Went Down to Georgia by Charlie Daniels Band",
    "You'll Never Know by Mindy McCready",
    "Whiskey Lullaby by Brad Paisley",
    "Love Story by Taylor Swift",
    "Coal Miner’s Daughter by Loretta Lynn",
    "Goodbye Earl by The Dixie Chicks",
    "Man! I Feel Like a Woman by Shania Twain",
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
    "Strange Fruit by Billie Holiday",
    "Smoke on the Water by Deep Purple",
    "Indian Reservation by The Raiders",
    "Zombie by The Cranberries",
    "The Big Bang Theory by The Barenaked Ladies",
    "Mesopotamia by The B-52's",
    "Run To The Hills by Iron Maiden",
    "Oliver's Army by Elvis Costello",
    "The Trooper by Iron Maiden",
    "Mister Custer by Larry Verne",
    "Rasputin by Boney-M",
    "Enola Gay by Orchestral Manoeuvres In The Dark",
    "Raised by Wolves by U2",
    "P.L.U.C.K. by System of a Down",
    "Brighter Than a Thousand Suns by Iron Maiden",
    "The Wreck of the Edmund Fitzgerald by Gordon Lightfoot",
    "The British Are Coming by Weezer",
    "The Longest Day by Iron Maiden",
    "The Infanta by The Decemberists",
    "Mississippi Goddam by Nina Simone",
    "Battle of New Orleans by Johnny Horton",
    "Buffalo Soldier by Bob Marley",
    "American Witch by Rob Zombie",
]


country_songs = []
country_list = [
    "I Walk the Line by Johnny Cash",
    "Jolene by Dolly Parton",
    "Friends in Low Places by Garth Brooks",
    "Choices by George Jones",
    "Concrete Angel by Martina McBride",
    "Kiss an Angel Good Morning Charley Pride",
    "Where Were You by Alan Jackson",
    "Live Like You Were Dying by Tim McGraw",
    "I Hope You Dance by Lee Ann Womack",
    "Take Me Home Country Roads by John Denver",
    "Walkin' After Midnight by Patsy Cline",
    "Breathe by Faith Hill",
    "Before He Cheats by Carrie Underwood",
    "Follow Your Arrow by Kacey Musgraves",
    "Blue Eyes Crying in the Rain by Willie Nelson",
    "Somebody Like You by Keith Urban",
    "Devil Went Down to Georgia by Charlie Daniels Band",
    "You'll Never Know by Mindy McCready",
    "Whiskey Lullaby by Brad Paisley",
    "Love Story by Taylor Swift",
    "Coal Miner’s Daughter by Loretta Lynn",
    "Goodbye Earl by The Dixie Chicks",
    "Man! I Feel Like a Woman by Shania Twain",
]
rap_songs = []
rap_list = [
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

def _init_oldsongs():
    id = 1
    for song in old_list:
        old_songs.append({"id": id, "song": song,})
        id += 1

def _init_countrysongs():
    id = 1
    for song in country_list:
        country_songs.append({"id": id, "song": song,})
        id += 1

def _init_rapsongs():
    id = 1
    for song in rap_list:
        rap_songs.append({"id": id, "song": song,})
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

@api_bp.route('/rap')
def get_rap():
    if len(rap_songs) == 0:
        _init_rapsongs();
    return jsonify(random.choice(rap_songs))

@api_bp.route('/countrytunes')
def get_countrysong():
    if len(country_songs) == 0:
        _init_countrysongs();
    return jsonify(random.choice(country_songs))