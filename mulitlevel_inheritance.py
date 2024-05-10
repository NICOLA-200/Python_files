class Prey:

     white= "clock"

     def flee(self):
          print("This animal flees")



class Predator:


     def hunt(self):
          print("This is animals  is hunting ")



     
class Rabbit(Prey):
     pass


class Hawk(Predator):
     pass

class Fish(Prey, Predator):
     pass

          
rabit = Rabbit()     


 




class Rectangle:
     def __init__(self,length,width):
           self.length = length
           self.width = width





class Square(Rectangle):
     def __init__(self, length, width):
          super().__init__(length, width)




sq =  Square(12,20)


req =  Rectangle()


print(sq.length)






