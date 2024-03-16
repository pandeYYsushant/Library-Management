class Library:
    def __init__(self):
        self.category= {}
        self.category_count= 0
        self.books= []
        self.books_count= 0
        

    def addcategory(self, cat):
       if cat in self.category:
           print("The category already exists.")
       else:
           self.category[cat]= []
           self.category_count+=1

    def addbook(self, book):
        
        askcat= input("What is the book category?:")
        if askcat in self.category:
            self.category[askcat].append(book)
        else:
             print("The category doesn't exist. We're creating this category for you-")
             self.category[askcat]= []
             self.category[askcat].append(book)
             self.category_count+=1


        self.books.append(book)
        self.books_count+= 1
        

            

    def getinfo(self):
        print(f"There are {self.category_count} categories.")
        print(f"No. of books are {self.books_count}")
        for key in self.category:
            print("For category", key, "\nthe books are", self.category[key])


U1= Library()
U2= Library()
U1.addcategory("Anime")
U1.addcategory("Romance")
U2.addcategory("Action")
U1.addbook("Naruto")
U2.addbook("Captain America")
U1.addbook("Titanic")