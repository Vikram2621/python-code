class bank:
    def rate(self):
        return 10
class hdfc(bank):
    def rate(self):
        return 8       
class punjab(bank):
    def rate(self):
        return 5        

a=bank()
b=hdfc()
c=punjab()
print(a.rate())
print(b.rate())
print(c.rate())