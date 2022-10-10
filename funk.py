from ssl import ALERT_DESCRIPTION_DECOMPRESSION_FAILURE


def bäst(name):
    # TODO Skriv ut att namnet är bäst
    # Ex: "Katherine" in - skriver ut "Katherine är bäst"
    print (F"{name} är bäst")

bäst ("mohammed")
bäst ("arda")
bäst ("Ariful")


def square(number):
    # TODO Returnera talet kvadrerat
    # Ex: 5 in - 25 ut
    return number **2
print (square(4))
print (square(5))
print (square (6))
print (square(7))


def sums(a, b):
    # TODO Returnera summan av a och b
    # Ex: 2, 6 in - 8 ut
    return a + b 

print (sums(3,5))
print (sums(2,8))
print (sums(5,9))
print (sums (6,3))

# Nu blir det lite svårare


def maximum(a, b, c):
    # TODO Returnera det största av a,b,c
    # Ex: 3, 6, 12 in - 12 ut
    if a>b and a>c:
        return a 
    elif c>b:
        return b
print (maximum (6,8,14))

"""
def palindrom(ord):
    # TODO Returnera True om ord är ett palindrom
    # Ex: abba in - True ut
    # Palindrom är ett ord som stavas likadant baklänges och framlänges.
    pass


def prime(nr):
    # TODO Returnera True om nr är ett primtal, annars returnera false
    # Ex: 5 in - True ut
    pass"""