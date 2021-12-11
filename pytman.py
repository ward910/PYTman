import datetime
from flask import Flask, render_template
from randomSwitch import randomSwitch

app = Flask(__name__)

@app.route('/')
def index():
    ArticleContent = randomSwitch()
    titleArticle = ArticleContent[0]
    textArticle = ArticleContent[1]
    linkArticle = ArticleContent[2]
    date = datetime.date.today().strftime('%m/%d/%Y')
    return render_template('index.html', titleArticle=titleArticle, date=date, textArticle=textArticle, linkArticle=linkArticle)

@app.route('/about')
def about():
    textAbout = """My first site using Flask and hosted on heroku used bootstrap 4.1 
                   (I didn't use 5 because only 4.1 documentation was translated to my language).
                """
    return render_template('about.html', textAbout=textAbout)

if __name__ == "__main__":
    app.run()