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

Username = input("Enter the Object name:")
Username = Library()
UserIn1= input("Do you wanna add a book/category? Yes/No\n")
if UserIn1 == "Yes" or "yes":
    UserIn2= input("Category or Book?")
    if UserIn2== "Category" or "category" or "cat" or "Cat" or "C" or "c":
        Input_Cat= input("Enter the Category:")
        Username.addcategory()
        print("Category successfully added.")
    
    if UserIn2 == "Book" or "book" or "B" or "b":
        Input_B= input("Enter the book name:")
        Username.addbook()
        print("Book is added to the library.")

else: 
    print("User is created, you can add whenever you want.")






                        
                            

        
        

