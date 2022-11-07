import random 
def leap_year (year):
    print(year)
   
    if year % 4 !=0: 
        print(year, "is not a leap year")

    if year % 4==0:
        print (year, "is a leap year")
year= int(input ("Välj ett skott år? "))
leap_year(year)  


