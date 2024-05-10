# import os 
import shutil
import os

source ="file.txt"

destination = "C:\\Users\\pc\\Documents\\PYTHON\\study\\folder_moved\\file.txt"

# try:
#    if (os.path.exists(destination)):
#           print("There is already a file  there ")
#    else:
#         os.replace(source, destination)
#         print("replaced")       

# except FileNotFoundError:
#       print("not found")

# shutil.copyfile('file.txt','copy.txt') 

path =  "file                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   "


try:
     # os.remove(path)
     # os.rmdir(path)
     os.rmtree(path)
except FileNotFoundError:
     print("that file was not found")

except PermissionError:
     print("You do not have  persmission")

except OSError:
     print("you cannot  delete  this")

else:
     print("was deleted")               


# path = "C:\\Users\\pc\\Documents\\PYTHON\\study"

 
num1 = 10;

num2 = 0


result = 10 / 0

print(result);


# if os.path.exists(path):
#      print("that location exists")
#      if os.path.isfile(path):
#           print("That is a file")
#      elif  os.path.isdir(path):
#       print("this is a  folder not a text")     
# else:
#      print("it does not  exists")     




# try:
#   with open('file2.txt') as file:
#     print(file.read())
# except FileNotFoundError:
#     print("That was not found")


# print(file.closed)


try:
     file1 = open('file.txt')
     print(file1.read())
except FileNotFoundError:
     print("file not found")


with open('file.txt', 'w') as file:
     file.append("\nthis is what  is wri\n  this is a good  one  ")



  