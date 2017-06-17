#Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    def display(self):
        self.price = str(self.price)
        print("Title: " + self.title + "\nAuthor: " + self.author + "\n Price: " + self.price)
        
