class calculation1:
    def summition(self,a,b,):
        return a+b
class calculation2(calculation1):
    def multiplication(self,a,b):
        return a*b

class derived(calculation2): 
    def divide(self,a,b):
        return a/b

d=derived()
print(d.summition(5,4)) 
print(d.multiplication(6,2))
print(issubclass(calculation2,calculation1))       
print(issubclass(derived,calculation2))       
print(issubclass(calculation1,calculation2))
print(isinstance(d,derived))       