import datetime
from random import randint
from flask import Flask, render_template
from content import Text

app = Flask(__name__)

@app.route('/')
def index():
    number = randint(0, 2)
    Article = Text(number)
    titleArticle = Article.getText['Title']
    textArticle = Article.getText['Text']
    linkArticle = Article.getText['Link']
    date = datetime.date.today().strftime('%m/%d/%Y')
    return render_template('index.html', titleArticle=titleArticle, date=date, textArticle=textArticle, linkArticle=linkArticle)

@app.route('/about')
def about():
    textAbout = """My first site using Flask and hosted on heroku used bootstrap 4.1 
                   (I didn't use 5 because only 4.1 documentation was translated to my language).
                """
    return render_template('about.html', textAbout=textAbout)

@app.route('/photos')
def photos():

    picsumPhotosAPI = "https://picsum.photos/300/300"

    return render_template('photos.html', picsumPhotosAPI=picsumPhotosAPI)

if __name__ == "__main__":
    app.run()