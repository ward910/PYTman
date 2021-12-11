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
    textAbout = """My first site using Flask and hosted on heroku used bootstrap 4.1 (I didn't use 5 because only 4.1 documentation was translated to my language).
                   I created a system that every time a user enters it shows a different subject but it didn't go as planned because heroku is static and it just seemed to change the subject when I do a rebuild.
                   This site is a proof of knowledge for me and I found it very easy and thought it would be more difficult."""
    return render_template('about.html', textAbout=textAbout)

if __name__ == "__main__":
    app.run()