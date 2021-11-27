from random import randint


titleRandom = ['Python', 'Django', 'Pandas']
textRandom = ['Python is a high-level programming language, interpreted as scripting, imperative, object-oriented, functional, dynamic and strong typing. (Wikipedia)', 'Django is a Python-based free and open-source web framework that follows the model–template–views architectural pattern. (Wikipedia)', 'In computer programming, pandas is a software library written for the Python programming language for data manipulation and analysis. (Wikipedia)']
linkRandom = ['https://en.wikipedia.org/wiki/Python', 'https://en.wikipedia.org/wiki/Django', 'https://en.wikipedia.org/wiki/Pandas_(software)']
random = randint(0, 2)
    
if random == 0:
    title = titleRandom[0]
    text = textRandom[0]
    link = linkRandom[0]
elif random == 1:
    title = titleRandom[1]
    text = textRandom[1]
    link = linkRandom[1]
else:
    title = titleRandom[2]
    text = textRandom[2]
    link = linkRandom[2]