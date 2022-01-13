def binary():
     binary = input("Please input your denery number to convert to binary : ")
     binary = int(binary)
     binary = bin(binary)[2:]
     print(binary)

def denery():
     denery = input("Please input your binary number to convert to denery : ")
     denery = int(denery, 2)
     print(denery)

def hexadecimal():
     hex1 = input("Please input your hex number to convert to denery : ")
     hex1 = int(hex1, 16)
     print(hex1)

def  dentohex():
     hexadecimal = input("Please input your denery number to convert to hex : ")
     hexadecimal = int(hexadecimal)
     hexadecimal = hex(hexadecimal)[2:]    
     print(hexadecimal)
  


print("1 - Denery to Binary")
print("2 - Binary to Denery")
print("3 - Hexadecimal to Denery")
print("4 - Denery to Hex")

answer = input("Please input your choice: ")

if answer == "1":
     binary()

elif answer == "2":
          denery()

elif answer == "3":
     hexadecimal()

elif answer == "4":
     dentohex()

else:
     print("Sorry This is not an option")
