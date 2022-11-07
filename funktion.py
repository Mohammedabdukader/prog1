
namne= "mohammed"
age= int(input ("hur gammal är du?"))
print (age)

while not (age := input ("write you age: ")).isdigit():
    print ("din hurunge lägg till siffror")

age= int (age)

if age >17:
    print ("lol du är gammal")
else:
    print ("du är ung")

"""
while not (height := input("Write your height: ")).isdigit() :
    print("Please enter a number\n")

height = int(height)

if height < 170:
    print("Lol you are short")
        
else:
    print("Wow so tall lamppost")"""
