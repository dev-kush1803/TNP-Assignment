# Polymorphism

class LNCT:
    def exam(self,a,b=10):
        c = a + b
        print(f"Exam 1 Method {c}")

class LNCTE(LNCT):
    def exam1(self):
        print("LNCTE METHOD")

obj = LNCTE()
obj.exam(10)
