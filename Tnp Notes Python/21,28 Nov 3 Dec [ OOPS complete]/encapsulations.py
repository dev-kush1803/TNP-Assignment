# Getter, Setter, decorator, generator
class A:
    city = "Bhopal"

    _year = 2024
    __dean = "john"
    def history(self):
        print("HISTORY")
    def _mgmt(self):
        print("Management")
    def __finance(self):
        print("Finance")
    # via public method
    def get_finance(self):
        print(A.__dean)
        A.__finance(self)
    def change_dean(self, de):
        A.__dean = de
        print(f"NEW DEAN is {A.__dean}")
mac = A()
print(mac.city)
print(mac._year)
mac.city = "Indore"
print(mac.city)
mac._year = 2025
print(mac._year)
mac.__dean = "MAC"
print(mac.__dean)
mac.get_finance()
# Name mangling
mac._A__finance()
mac.change_dean("SAM")




#mac.__finance()
