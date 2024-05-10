class Animal:
    
    alive = True


    def  eat(self):
        print("This animals  is eating ")

    
    def sleep(self):
        print("This amials is sleeping ")



class  Rabbit(Animal):
    pass


class  Hawk(Animal):
    pass



rabbit =  Rabbit()


hawk = Hawk()



print(rabbit.alive)



rabbit.eat()


name =  3


name =  "fate"

print(name)


class babyRabbit(Rabbit):
    pass



print("this is the babyRabbit " + str(babyRabbit.alive))