



double  =  lambda x:x*2


print(double(2))

multiple = lambda x,y:  x +y


print(multiple(2,10))

grown = lambda age: True if age > 18 else False

print(grown(12))


students = ["squad","sandy","patrick","spongebob","krabs"]


# students.sort(reverse=True)

students = sorted(students)


for i  in students:
     print(i)



teachers = [("mbappe","F",60),
            ("mbpe","A",33),
            ("pepe","D",50),
            ("mane","B",20),
            ("mbane","C",80),
            ]

grade  = lambda grades:grades[1]



teachers.sort(key=grade)

for i in students:
     print(i)



store =  [("shirt",20.00),
          ("pants",25.00),
          ("jacket",50.00),
          ("socks",10.00)]


to_euros = lambda data: (data[0],data[1]* 0.82)


store_euros  =  list(map(to_euros,store))


for i in store_euros:
     print(i)




friends = [("Rachel",19),
           ("Monica",18),
           ("joey",16),
           ("ross",20)]


age =  lambda data: data[1] >= 18

drinking = list(filter(age, friends))


print(drinking)



# list compprehension     

 
squares = [i * i for i in range(1,11)]    


pupils = [i for i in students if i >= 60]


cities_in_f = {"york": 32,"boston": 75,"angele": 100, "chic":50}


cities_in_c = {key: ((value-32)) for (key,value) in cities_in_f.items() }


usernames = ["dude","bro","pepe","fate"]

passwords = ("abc","123","dfg","098")


users = zip(usernames, passwords)

for key , value in users.items():
     print(key,value)





