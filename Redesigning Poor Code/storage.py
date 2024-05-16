import json
import os

class Storage:
    def __init__(self, filename):
        self.filename = filename # This filename can be set at the start in the main.py and the only hard code part if any user needs to do if he wishes
        if not(os.path.exists(self.filename)):  # The if-else checks if the current program has been execueted before and if so we don't want to overwrite the existing details with a blank json
            print("New File Created")
            with open(self.filename, "w") as f:
                json.dump([], f) # '[]' is used to create an empty list which contain the dictionaries

    def addData(self, data): # This method is used to add record to the json file
            try:
                with open(self.filename, "r") as file:
                    json_string = file.read()
                    existing_data = json.loads(json_string) # The method 'loads' can only load data from json string so we first have to read the file which is done in the above step
            except FileNotFoundError:
                existing_data = [] # If any error occurs an empty list is created and a json file will be created
            if 'Id' in data:
                for dicts in existing_data:
                    if data['Id'] == dicts['Id']:
                        print("id number already exists") # 'Id' has been set as a primary key which will differentiate every record
                        return
            existing_data.append(data) # After checking for any flaws in the entered data, the data is added to existing data
            with open(self.filename, "w") as file:
                json.dump(existing_data, file) # The final data is then pushed into the file
            print("Data has been successfully entered.")
    
    def get(self, data):# This method is used to get records with a value
        try:
            with open(self.filename, "r") as file:
                json_string = file.read()
                existing_data = json.loads(json_string)
        except FileNotFoundError:
            print("File doesn't have any data regarding books")
            return
        for dicts in existing_data:
            if data in dicts.values(): # Every value in all the records are checked, to give the application user the ease of searching by title or searching for authors multiple works
                for key in dicts:
                    print(key," : ",dicts[key])
        print("Data retrieved")
    
    def editData(self, id, attribute, new_data):# This method is used to edit a particular records
        try:
            with open(self.filename, "r") as file:
                json_string = file.read()
                existing_data = json.loads(json_string)
        except FileNotFoundError:
            print("File doesn't exist, please initialize the storage class first.")
            return
        flag = True # A boolean variable is used to check if the given id exists 
        for dicts in existing_data:
            if id == dicts['Id']:  # Id is used to identify the particular data
                dicts[attribute] = new_data
                flag = False # the variable is set to False as the record is found
                with open(self.filename, "w") as file:
                    json.dump(existing_data, file)    
                break
        if flag: 
            print("The id doesn't exist") # Since the record is not found, this message is displayed
        else:
            print("Data retrieved")

    def delete(self, id):# This method is used to delete a particular record
        try:
            with open(self.filename, "r") as file:
                json_string = file.read()
                existing_data = json.loads(json_string)
        except FileNotFoundError:
            print("File doesn't exist, please initialize the storage class first")
            return
        flag = False
        for i, dicts in enumerate(existing_data):
            if id == dicts['Id']:
                flag = True
                existing_data.pop(i) # The record is then removed if the id exists
                with open(self.filename, "w") as file:
                    json.dump(existing_data, file)
                break    
        if flag:
            print("The record has been successfully deleted")
        else:
            print("The record for the given isbn file doesn't exist")

    def deleteAll(self):# This method is used to delete all of the records
        try:
            with open(self.filename, "w") as file:
                json.dump([], file) # The value in the json file is intialized '[]', making the data empty 
        except FileNotFoundError:
            print("File doesn't exist, please initialize the storage class first")
        
    def getAll(self):# This method is used to display all of the records
        try:
            with open(self.filename, "r") as file:
                json_string = file.read()
                existing_data = json.loads(json_string)
        except FileNotFoundError:
            print("File doesn't exist, please initialize the Storage class")
            return
        for dicts in existing_data:
            for key in dicts:
                print(key,' : ', dicts[key]) 
        print("Data has been successfully retrieved")

    