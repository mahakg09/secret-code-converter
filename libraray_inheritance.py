class item:
    def __init__(self,title,author,year):
        self.title = title 
        self.author=author 
        self.year = year 
        
    def display_info(self):
        print(f"TITLE:{self.title}")
        print(f"AUTHOR:{self.author}")
        print(f"YEAR:{self.year}")
        
        
class Book(item):
    def __init__(self,title,author,year,genre):
        super().__init__(title,author,year)
        self.genre=genre 
    def display_info(self):
        super().display_info()
        print(f"GENRE:{self.genre}") 
        
class DVD(Book):
    def __init__(self,title,author,year,genre,duration):
        super().__init__(title,author,year,genre)
        self.duration=duration
    def display_info(self):
        super().display_info()
        print(f"DURATION:{self.duration}")
        
obj1=item("atomic habits","chetan bhagta",1999)
obj1.display_info()
print("--------------------------------------------------------------------------")
obj2=Book("Atomic habits","chetan bhagta",1999,"romantic")
obj2.display_info()
print("------------------------------------------------------------------------------------------")
obj3=DVD("Atomic habits ","chetan bhagta",1999,"romantic","13days")
obj3.display_info()