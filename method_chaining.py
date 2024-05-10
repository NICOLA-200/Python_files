class Car:

     def turnon(self):
          print("You start the engine ")
          return self

     def drive(self):
          print("You drive the car")
          return self


     def brake(self):

          print("step on the brakes")
          return self

     def turnoff(self):
          print("You turn off the engine")
          return self




car  = Car()

car.turnon().drive()

        