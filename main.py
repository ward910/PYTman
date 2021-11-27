import datetime
from flask import Flask, render_template
from randomText import text, title, link

app = Flask(__name__)

@app.route('/')
def index():
    titleArticle = title
    textArticle = text
    linkArticle = link
    date = datetime.date.today().strftime('%m/%d/%Y')
    return render_template('index.html', titleArticle=titleArticle, date=date, textArticle=textArticle, linkArticle=linkArticle)



if __name__ == "__main__":
    app.run()