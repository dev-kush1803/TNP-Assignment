#polymorphism

class LNCT:
    def add(self,a,*b):
        res = a
        for i in b:
            res += i
        return res

obj = LNCT()
print(obj.add(5))
print(obj.add(10,20))
print(obj.add(10,20,4,5,67,8,9))
