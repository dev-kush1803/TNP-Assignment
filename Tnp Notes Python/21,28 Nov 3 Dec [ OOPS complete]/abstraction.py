#abstraction

from abc import ABC, abstractmethod
class LNCT(ABC):
    college = "LNCT"
    @abstractmethod
    def login(self):
        pass
    def greet(self):
        print(f"Welcome in {LNCT.college}")

class LNCTE(LNCT):
    college = "LNCTE"
    def greet(self):
        print(f"Welcome in {LNCTE.college}")
    def login(self):
        pass
obj = LNCTE()
obj.greet()
