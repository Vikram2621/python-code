class car:
   name=""
   ex_room_price=0
   third_party_price=0
   taxes=0
   
   def on_road_price(self):
      on_road=self.ex_room_price+self.third_party_price+self.taxes
      return on_road


car1=car()
car1.name="Alto"
car1.ex_room_price=500000
car1.third_party_price=50000
car1.taxes=20000

print(car1.name)
print(car1.ex_room_price)
print(car1.third_party_price)
print(car1.taxes)
print("car 1 price :",car1.on_road_price())