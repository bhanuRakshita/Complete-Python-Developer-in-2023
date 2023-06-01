# Python Object Oriented Programming by Joe Marini course example
# Using composition to build complex objects


class Book:
    def __init__(self, title, price, author):
        self.title = title
        self.price = price
        self.author = author
        self.chapters = []

    def addchapter(self, chapter):
        self.chapters.append(chapter)

    def getBookPageCount(self):
        totalPages = 0
        for chap in self.chapters:
            totalPages+=chap.pages
        return totalPages

class Author:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self):
        return (self.firstname + " " + self.lastname)

class Chapter:
    def __init__(self, chapterName, pages):
        self.chapterName = chapterName
        self.pages = pages

auth1 = Author("Leo", "Tolstoy")

b1 = Book("War and Peace", 39.0, auth1)

b1.addchapter(Chapter("Chapter 1", 2))
b1.addchapter(Chapter("Chapter 2", 3))
b1.addchapter(Chapter("Chapter 3", 4))

print(b1.getBookPageCount())
print(b1.author)