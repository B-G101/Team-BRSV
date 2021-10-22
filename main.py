from flask import Flask, render_template, request, url_for, redirect
from templates.technicals.image import image_data
from pathlib import Path
from api.webapi import api_bp
from starter import app_starter


app = Flask(__name__)

app.register_blueprint(api_bp)
app.register_blueprint(app_starter)


@app.route('/rgb/')
def rgb():
    path = Path(app.root_path) / "static" / "img"
    return render_template('technicals/rgb.html', images=image_data(path))
    #return render_template('rgb.html', images=image_data(Path(app.root_path)))



@app.route('/game/easy', methods=['GET', 'POST'])
def easy():
    names = get_names(SONGS)
    # you must tell the variable 'form' what you named the class, above
    # 'form' is the variable name used in this template: index.html
    form = NameForm()
    message = ""
    if form.validate_on_submit():
        name = form.name.data
        if name.lower() in names:
            # empty the form field
            form.name.data = ""
            id = get_id(SONGS, name)
            # redirect the browser to another route and template
            return redirect( url_for('hard', id=id) )
        else:
            message = "That song is not in our database."
    return render_template('game/easy.html', names=names, form=form, message=message)
@app.route('/bria/')
def bria():
    return render_template("aboutus/bria.html")
@app.route('/game/medium')
def medium():
    return render_template("game/medium.html")
@app.route('/game/hard')
def hard():
    return render_template("game/hard.html")
@app.route('/riya/')
def riya():
    return render_template("aboutus/riya.html")
@app.route('/sreeja/')
def sreeja():
    return render_template("aboutus/sreeja.html")
@app.route('/valerie/')
def valerie():
    return render_template("aboutus/valerie.html")
@app.route('/')
def index():
    return render_template("index.html")
# connects /kangaroos path to render aboutus.html
@app.route('/aboutus/')
def aboutus():
    return render_template("aboutus.html")
@app.route('/favorites/')
def favorites():
    return render_template("favorites.html")
@app.route('/favoriteSong', methods=['GET', 'POST'])
def favoriteSong():
    # changed greet function for favorites.htm;
    if request.form:
        fname = request.form.get("fname")
        if len(fname) != 0:  # input field has content
            return render_template("Favorites.html", fname=fname)
        else:
            return render_template("Favorites.html", fname=" Try entering a song!")
@app.route('/songFavorite', methods=['GET','POST'])
def songFavorite():
    if request.form:
        gname = request.form.get("gname")
        if len(gname) != 0:  # input field has content
            return render_template("Favorites.html", gname=gname)
        else:
            return render_template("Favorites.html", gname=" Try entering a song!")

@app.route('/Lifechangingsongs/')
def lifechangingSongs():
    return render_template("LifechangingSongs.html")
@app.route('/Technicals/')
def technicals():
    return render_template("Technicals.html")
@app.route('/stub/')
def stub():
    return render_template("technicals/stub.html")
@app.route('/minilabs/')
def video():
    return render_template("minilabs.html")
@app.route('/greet', methods=['GET', 'POST'])
def greet():
    # submit button has been pushed
    if request.form:
        fname = request.form.get("fname")
        if len(fname) != 0:  # input field has content
            return render_template("technicals/stub.html", fname=fname)
        else:
            return render_template("technicals/stub.html", fname="World")
@app.route('/binary/', methods=['GET', 'POST'])
def binary():
    # submit button has been pushed
    if request.form:
        bits = request.form.get("bits")
        if len(bits) != 0:  # input field has content
            return render_template("technicals/binary.html", BITS=int(bits))
    return render_template("technicals/binary.html", BITS=8)

@app.route('/binary/colorcode/')
def colorcode():
    return render_template("technicals/binary (logic gates)/colorcode.html")

@app.route('/binary/signedaddition/')
def signedaddition():
    return render_template("technicals/binary (logic gates)/signedaddition.html")

@app.route('/concerts/')
def concerts():
    return render_template("concerts.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
