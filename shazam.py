import requests

def song(song_given):

    term = str(song_given)

    url = "https://shazam.p.rapidapi.com/auto-complete"

    querystring = {"term":term,"locale":"en-US"}

    headers = {
        'x-rapidapi-host': "shazam.p.rapidapi.com",
        'x-rapidapi-key': "435f957ca1msh508be3bb9ed13fap1d89c7jsn47a12462048a"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text