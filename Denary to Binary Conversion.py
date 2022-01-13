def binary():
     binary = input("Please input your denery number to convert to binary : ")
     binary = int(binary)
     binary = bin(binary)[2:]
     print(binary)