class Duck:
    def Talk(self):
        print("Quack-Quack-Quack..")

class Dog:
    def bark(self):
        print("Bow-Bow-Bow..")

class Cat:
    def Talk(self):
        print("Meow-Meow-Meow..")

class Goat:
    def Talk(self):
        print("Maya-Maya-Maya..")


l=[Duck(),Dog(),Cat(),Goat()]
for obj in l:
    if hasattr(obj,'Talk'):
        obj.Talk()
    elif hasattr(obj,'bark'):
        obj.bark()