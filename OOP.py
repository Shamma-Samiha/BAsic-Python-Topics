# Class & Object
"""class Samiha:
    name = ""
    age = ""

x = Samiha()
y = Samiha()

x.name = "Samiha"
y.name = "Tun"

print(y.name)
print(x.name)
"""

# Inheritance
"""
class Abbu:
    car = "BMW"
    home = "Duplex"
    phone = "iphone"
class Ammu:
    flat = "19 sqft"

class Shamma(Abbu,Ammu):
     tk = "2 billion"
     iq = 120

class Galib(Shamma):
    ph = ""

x = Shamma()
y = Galib()
print(x.car)
print(x.flat)
print(y.flat)
print(y.tk)
"""

# Constructor

# Without Constructor
"""
class PartnerInfo:
    def GalibInfo(self,name,age):
        print(f"My boyfies name is {name}, And his age is {age}.")

x = PartnerInfo()
x.GalibInfo("Abdullah Al Galib", "22")
"""
# With using constructor

"""
class PartnerInfo:
    def __init__(self,name,age):
        print(f"My boyfies name is {name}, And his age is {age}.")

p = PartnerInfo("Abdullah al galib" , "22")
"""
# Polymorphism

class Animal:
    def __init__(self,sound,size):
        self.sound = sound # instance variable & public
        self.size = size

class Dog(Animal):
    pass
class Bird(Animal):
    pass

x = Dog("Gheu Gheu","4 feet")

y = Bird("Chrip", "2 feet")

print(x.size,y.sound)