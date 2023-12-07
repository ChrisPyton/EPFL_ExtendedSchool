# Converter

def Farenheit(celsius):
    farenheit = (celsius * 9/5) + 32
    return farenheit

print(str(34)+" celsius is "+str(Farenheit(34))+" farenheit")

def ConvertE(amount):
    FinalAmount = amount * 0.95
    return FinalAmount

name = input("Please enter your name: ")
print("Your name is " + name)
#HowMuch = input()
#print(ConvertE(int(HowMuch)))

def ConvertN(nautica):
    return str(nautica)+" milles nautiques are "+str(int(nautica)*1.852)+" kilometers"

print(ConvertN(int(input("How many nautica ? "))))