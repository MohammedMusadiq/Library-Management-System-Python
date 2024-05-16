from storage import Storage
import datetime

class Logger:
    def __init__(self, filename) -> None: # This method is used to create a json file which will log every option choosen
        self.storage = Storage(filename)

    def logAction(self, action): # The time when the method is executed and the action is added into the logger
        current_time = datetime.datetime.now()
        current_time = current_time.strftime("%H:%M:%S")
        self.storage.addData({'Time': current_time, 'Action': action})

    def getAllActions(self): # Using this method all of the actions are displayed.
        self.storage.getAll()
    