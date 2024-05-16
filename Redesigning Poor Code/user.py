from storage import Storage
from logger import Logger

class User:
    def __init__(self, filename): # In the intialize method a File for the User class is created which we can access through user object only.
        self.storage = Storage(filename)
        self.attributes = ['Id', 'Name', 'Borowed books'] # This list holds the list of default field the records will have, user can later change these fields. This is used so that the application used doesn't have to enter them every time
        self.logger = Logger('logData') # A logger object is created which will enter every action to the log data

    def changeDefaultAttributes(self): # This method is used to change the default attributes.
        self.attributes = input("Enter the new attributes separating with a ',' : ").split(',')
        self.logger.logAction('Default attributes changed for user Data.')

    def getDefaultAttributes(self): # This method is used to display the default fields
        print(self.attributes)
        self.logger.logAction('Default attributes requested for User Data.')

    def addUserDetails(self): # This method is used to add the record
        dictt = {}
        for attribute in self.attributes:
            dictt[attribute] = input(f"Enter the {attribute} of user : ")
        self.storage.addData(dictt)
        self.logger.logAction('User details added to User Data')

    def get(self): # This method is used to retrieve data with a value like "Name" and "Id"
        data = input("Enter a detail of the user you want : ")
        self.storage.get(data)
        self.logger.logAction('Request for a specific user details.')

    def getAll(self): # This method is used to retrieve all the records
        self.storage.getAll()
        self.logger.logAction('Request for all user details.')

    def delete(self): # This method is used to delete a specific record
        id = input("Enter the id of the user : ")
        self.storage.delete(id)
        self.logger.logAction('Deleted a specific user details.')

    def deleteAll(self): # This method is used to delete all the records
        self.storage.deleteAll()
        self.logger.logAction('Deleted all user details.')

    def editData(self): # This method is used to edit a record
        id = input("Enter the id of the user you want to edit or add a detail : ")
        attribute = input("Enter the attribute you want to edit : ")
        new_data = input("Enter the new data : ")
        self.storage.editData(id, attribute, new_data)
        self.logger.logAction("Edited a users's details.")
