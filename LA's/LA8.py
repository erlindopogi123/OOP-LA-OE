class Book:
    def __init__(self,title, author):
        self.title = title
        self.author = author
     
book = Book("Kimetsu No Yaiba", "Koyoharu Gotouge")
print(f"Output:\nBook:{book.title}\nAuthor:{book.author}\n")
del book.author

book2 = Book("Tangle", "Jacob Grimm")
print(f"Book2:{book2.title}\nAuthor2:{book2.author}")