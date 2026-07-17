class BookStore:
    NoOfBooks=0
    def __init__ (self,Name,Author):
        self.Name = Name
        self.Author = Author
        
        BookStore.NoOfBooks += 1

    def Dis(self):
        print(f"{self.Name} By {self.Author} No of Books : {BookStore.NoOfBooks}")


book1=BookStore("The Life","S.J.")
book1.Dis()

book1=BookStore("The Life2","S.G.")
book1.Dis()

book1=BookStore("The Life2","J.G.")
book1.Dis()
