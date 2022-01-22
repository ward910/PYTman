class Text:
    def __init__(self, number):
        self.number = number
        self.getText = self.getArticle()
    
    def getArticle(self):
        if self.number == 0:    
            Text = { 'Title': 'Python', 'Text': 'Python is a high-level programming language, interpreted as scripting, imperative, object-oriented, functional, dynamic and strong typing. (Wikipedia)', 'Link': 'https://en.wikipedia.org/wiki/Python' }
                
        if self.number == 1:
            Text = { 'Title': 'Django', 'Text': 'Django is a Python-based free and open-source web framework that follows the model–template–views architectural pattern. (Wikipedia)', 'Link': 'https://en.wikipedia.org/wiki/Django' }
            
        if self.number == 2:
            Text = { 'Title': 'Pandas', 'Text': 'In computer programming, pandas is a software library written for the Python programming language for data manipulation and analysis. (Wikipedia)', 'Link': 'https://en.wikipedia.org/wiki/Pandas_(software)' }
        return Text
