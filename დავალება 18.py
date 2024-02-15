#1
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
            return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)


#მაგალითად
v1 = Vector(2, 3)
v2 = Vector(3, 4)
v3 = v1 + v2
print(v3)  # Output იქნება: (5, 7)

#2
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        else:
            return False


# magalitad
book1 = Book('wigni', ' topuria')
book2 = Book('wigni', ' topuria')
book3 = Book('wigni', 'ghvaberidze')

print(book1 == book2)  # Output aris: True
print(book1 == book3)  # Output aris: False
