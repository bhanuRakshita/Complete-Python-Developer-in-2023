# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title
        # TODO: add properties
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = 'secret'

    # TODO: create instance methods
    def getPrice(self):
        if hasattr(self, '_discount'):
            return self.price-(self.price*self._discount/100)
        return self.price

    def setDiscount(self, discount):
        self._discount = discount

# TODO: create some book instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)

# TODO: print the price of book1
print(b1.getPrice())
print(b1._Book__secret)

# TODO: try setting the discount
# b1.setDiscount(20)
# print(b1.getPrice())s

# TODO: properties with double underscores are hidden by the interpreter
print(b1._Book__secret)