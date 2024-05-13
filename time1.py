import time

print (time.time())


print(time.ctime(1000000000))


time_obj = time.localtime();

print(time_obj)

time_string = "20 April, 2020"

time_object = time.strptime(time_string,"%d %B, %Y")

print(time_object)




