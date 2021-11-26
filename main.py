import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    nameArticle = 'Python'
    date = datetime.date.today().strftime('%m/%d/%Y')
    text = 'Python is a high-level programming language, interpreted as scripting, imperative, object-oriented, functional, dynamic and strong typing. (Wikipedia)'
    linkNavbr = ''
    return render_template('index.html', nameArticle=nameArticle, date=date, textArticle=text, linkNavbr=linkNavbr)



if __name__ == "__main__":
    app.run()