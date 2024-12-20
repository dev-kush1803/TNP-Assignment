#OOP

class LnctCollege:
    city = "bhopal"
    COLLEGE = "LNCT" #class
    def showDetails(self):
        year = 2024 #local
        self.section = "A" #instance
        print("Show Details")

    def showsection(self):
        print(f"your section is {self.section} in year {year}")
a = LnctCollege()
print(a.city)
a.showDetails()

b = LnctCollege()
b.city = "Indore"
print(b.city)
b.showDetails()
b.showsection()
