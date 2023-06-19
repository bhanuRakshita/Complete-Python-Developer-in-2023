# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods


class Book:
    # TODO: Properties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    # TODO: double-underscore properties are hidden from other classes
    __bookList = None

    # TODO: create a class method
    @classmethod
    def getBookTypes(cls):
        return cls.BOOK_TYPES
    
    # TODO: create a static method
    @staticmethod
    def getBookList():
        if Book.__bookList == None:
            Book.__bookList=[]
        return Book.__bookList

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def setTitle(self, newtitle):
        self.title = newtitle
        
    def __init__(self, title, bookType):
        self.title = title
        if bookType in Book.BOOK_TYPES:
            self.bookType = bookType
        else:
            raise ValueError(f'{bookType} is not a valid booktype')

# TODO: access the class attribute
print('Book types are: ', Book.getBookTypes())

# TODO: Create some book instances
b1 = Book("Title 1","HARDCOVER")
b2 = Book("Title 2","EBOOK")

# TODO: Use the static method to access a singleton object
books = Book.getBookList()
print(books)

books.append(b1)
print(books)
print(Book.getBookList())