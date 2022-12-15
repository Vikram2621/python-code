class month:
    def __init__(self,name,age):
        self.name=name 
        self.age=age 

    def show(self):
        print("month name",self.name,self.age,"month")

    def show_month(self):
        print(self.age,"month")
    

s1=month("jan",1)           
s2=month("feb",2)
s3=month("mar",3)
s4=month("api",4)

s1.show()
s2.show()
s3.show()
s4.show()
s4.show_month
print(getattr(s1,'name'),":",getattr(s1,'age'))  
setattr(s1,'name','dec')  
print(getattr(s1,'name'),":",getattr(s1,'age'))
print(hasattr(s1,'d'))