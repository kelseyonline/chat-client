# This is the abstract state 

from abc import ABC, abstractmethod 

class Mode(ABC): 
    @abstractmethod 
    def process(self, message: str) -> str:
        pass