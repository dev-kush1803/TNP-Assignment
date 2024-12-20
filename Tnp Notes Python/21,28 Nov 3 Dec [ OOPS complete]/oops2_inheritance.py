#inheritance
#member variable of class
#constructor
class LNCT:
    city = "bhopal" #class Variable
    def __init__(self,year):
        self.year = year
        print(f"Welcome in LNCT in {self.year}")
class CSE(LNCT):
    def __init__(self,name,branch,ye):
        #LNCT.__init__(self,ye)
        #super().__init__(ye)
        self.name = name
        self.branch = branch
        print(f"{CSE.city}")
    def exam(self):
        print(f"Hello {self.name}, you are appearing for exam")

#obj = CSE("john","CSE",2025) #

#MRO - Method Resolution order

class check:
    def __init__(self):
        super().__init__()

obj =check()
print(obj)
