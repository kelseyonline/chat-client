# This is the abstract state 

from abc import ABC, abstractmethod 

class Mode(ABC): 
    @abstractmethod 
    def send(self, message: str) -> str:
        pass