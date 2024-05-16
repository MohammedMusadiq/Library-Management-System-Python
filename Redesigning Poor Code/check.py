import json

class Check:
    def __init__(self, bookFileName, userFileName) -> None: # This method is used to access the Data of books and users
        self.bookFile = bookFileName
        self.userFile = userFileName

    def checkIn(self, bookId, userId): # This method is executed when an user returns a borrowed book.
        try:
            with open(self.bookFile, "r") as file:
                json_string = file.read()
                existing_bookData = json.loads(json_string)
        except FileNotFoundError:
            print(f"{self.bookFile} not found, initialize it in the Storage class")
            return
        try:
            with open(self.userFile, "r") as file:
                json_string = file.read()
                existing_userData = json.loads(json_string)
        except FileNotFoundError:
            print(f"{self.userFile} not found, initialize it in the Storage class")
            return
        # Both the files data are accessed and checked if both the user and book exist in the data and displaying a message when eiher of them doesn't exist
        flag = True
        for i, dicts in enumerate(existing_bookData):
            if dicts['Id'] == bookId:
                flag = False
                break
        if flag:
            print("The book details doesn't exist in the database add them")
            return
        flag = True
        for j, dicts in enumerate(existing_userData):
            if dicts['Id'] == userId:
                flag = False
                break
        if flag:
            print("The user details doesn't exist in the database add them")
            return
        
        existing_bookData[i]['Number'] = str(int(existing_bookData[i]['Number'])+1) # As the book is submitted, the number of books is incremented in the books json file
        existing_userData[j]['Borowed books'] = str(int(existing_userData[j]['Borowed books'])-1) # As the book is submitted, the number of books borrowed by the user is decremented in the users json file
        try: # The updated data is then overwritten into the json file. 
            with open(self.bookFile, "w") as file:
                json.dump(existing_bookData, file)
            with open(self.userFile, "w") as file:
                json.dump(existing_userData, file)
        except FileNotFoundError:
            print("Error while updating")
            return

    def checkOut(self, bookId, userId): # This method is executed when an user returns a borrowed book.
        try:
            with open(self.bookFile, "r") as file:
                json_string = file.read()
                existing_bookData = json.loads(json_string)
        except FileNotFoundError:
            print(f"{self.bookFile} not found, initialize it in the Storage class")
            return
        try:
            with open(self.userFile, "r") as file:
                json_string = file.read()
                existing_userData = json.loads(json_string)
        except FileNotFoundError:
            print(f"{self.userFile} not found, initialize it in the Storage class")
            return
        # Both the files data are accessed and checked if both the user and book exist in the data and displaying a message when eiher of them doesn't exist
        flag = True
        for i, dicts in enumerate(existing_bookData):
            if dicts['Id'] == bookId:
                if dicts['Number'] == '0': # There's an extra condition where we have to check if the number of available books for that title are 0 and if it is '0' then a message is displayed that the book is unavailable
                    print('The book is Currently unavailable')
                    return
                flag = False
                break
        if flag:
            print("The book details doesn't exist in the database add them")
            return
        flag = True
        for j, dicts in enumerate(existing_userData):
            if dicts['Id'] == userId:
                flag = False
                break
        if flag:
            print("The user details doesn't exist in the database add them")
            return
        existing_bookData[i]['Number'] = str(int(existing_bookData[i]['Number'])-1) # As the book is given, the number of books is decremented in the books json file
        existing_userData[j]['Borowed books'] = str(int(existing_userData[j]['Borowed books'])+1) # As the book is given, the number of books the user borrowed has incremented in the users json file
        try:
            with open(self.bookFile, "w") as file:
                json.dump(existing_bookData, file)
            with open(self.userFile, "w") as file:
                json.dump(existing_userData, file)
        except FileNotFoundError:
            print("Error while updating")
            return