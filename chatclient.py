from mode import Mode
from plain import Plain 

# This is the Context (or Canvas)

class Client: 
    def __init__(self): 
        self.mode: Mode = Plain()

    def set_mode(self, mode: Mode): 
        self.mode = mode

    def send(self, message: str):
        processed = self.mode.process(message)
        print(processed)

