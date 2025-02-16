import json


class FormException:
    def __init__(self, message):
        self.message = message
    
    def json(self):
        return json.dumps({"message": self.message})