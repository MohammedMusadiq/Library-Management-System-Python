from storage import Storage
from logger import Logger

class Book:
    def __init__(self, filename) -> None: # In the intialize method a File for the book class is created which we can access through book object only.
        self.storage = Storage(filename)
        self.attributes = ['Title', 'Id', 'Author', 'Number'] # This list holds the list of default field the records will have, user can later change these fields. This is used so that the application used doesn't have to enter them every time 
        self.logger = Logger('logData') # A logger object is created which will enter every action to the log data

    def changeDefaultAttributes(self): # This method is used to change the default attributes.
        self.attributes = input("Enter the new attributes separating with a ',' : ").split(',')
        self.logger.logAction('Default attributes changed for Book Data.')

    def getDefaultAttributes(self): # This method is used to display the default fields
        print(self.attributes)
        self.logger.logAction('Default attributes of Book Data displayed.')

    def addBookDetails(self): # This method is used to add the record
        dictt = {}
        for attribute in self.attributes:
            dictt[attribute] = input(f"Enter the {attribute} of book : ")
        self.storage.addData(dictt)
        self.logger.logAction('Book details added to Book Data')
        
    def get(self): # This method is used to retrieve data with a value like "Author name" and "Title"
        data = input("Enter a detail of the book you want : ")
        self.storage.get(data)
        self.logger.logAction('Request for a specific book details.')

    def getAll(self): # This method is used to retrieve all the records
        self.storage.getAll()
        self.logger.logAction('Request for all the book details.')

    def delete(self): # This method is used to delete a specific record
        id = input("Enter the id of the book : ")
        self.storage.delete(id)
        self.logger.logAction('Deleted a specific book details.')

    def deleteAll(self): # This method is used to delete all the records
        self.storage.deleteAll()
        self.logger.logAction('Deleted all book details.')

    def editData(self): # This method is used to edit a record
        id = input("Enter the id of the book you want to edit or add a detail : ")
        attribute = input("Enter the attribute you want to edit : ")
        new_data = input("Enter the new data : ")
        self.storage.editData(id, attribute, new_data)
        self.logger.logAction("Edited a book's details.")