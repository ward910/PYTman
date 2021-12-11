from random import randint

def rText():
    titleRandom = ['Python', 'Django', 'Pandas']
    textRandom = ['Python is a high-level programming language, interpreted as scripting, imperative, object-oriented, functional, dynamic and strong typing. (Wikipedia)', 'Django is a Python-based free and open-source web framework that follows the model–template–views architectural pattern. (Wikipedia)', 'In computer programming, pandas is a software library written for the Python programming language for data manipulation and analysis. (Wikipedia)']
    linkRandom = ['https://en.wikipedia.org/wiki/Python', 'https://en.wikipedia.org/wiki/Django', 'https://en.wikipedia.org/wiki/Pandas_(software)']
    random = randint(0, 2)

    rTextExports = [titleRandom, textRandom, linkRandom, random]
    return rTextExports

rTextExports = rText()

exports = {
    "titleRandom": rTextExports[0], "textRandom": rTextExports[1],
    "linkRandom": rTextExports[2], "random": rTextExports[3]
}