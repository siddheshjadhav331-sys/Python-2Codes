class lib:
    def __init__(self,book_name,author_name):
      self.book_name = book_name
      self.author_name = author_name
      self.is_available = True
    
    def check_out(self):
      if self.is_available:
         self.is_available = False
         print(f"'{self.book_name}' has been checked out.")
      else:
         print(f"Sorry, '{self.book_name}' is already checked out.")

    def return_book(self):
       if not self.is_available:
          self.is_available = True
          print(f"'{self.book_name}' has been returned.")
       else:
          print(f"'{self.book_name}' was not checked out.") 

    def display_book(self):
       status = "Available" if self.is_available else "Not Available"   
       print(f"Book Name : {self.book_name}")
       print(f"Author: {self.author_name}") 
       print(f"Status: {status}")      

# Main Object Creation
book1 = lib("Python Programming" , "Guido van Rossum")
book2 = lib("C++ Basics" , "Bjarne Stroustrup")

# Display book
book1.display_book()
book2.display_book()

# Check out book
book1.check_out()
book1.display_book()
book2.check_out()
book2.display_book()

# Return the book
book1.return_book()
book1.display_book()
book2.return_book()
book2.display_book()
