
number = 12
print(number)

## variables rules ##

# You can use any letter or the underscore character (_).
# You can use numbers in your variable names but you can't start the name with a number.
# You can't use whitespaces or special characters that have a meaning in Python such as + or -.
# Variable names are case sensitive. That means that fruits and Fruits are two different variables.
# Start your variable names with a lower case letter. fruits and not Fruits. It's not a rule but a convention.
# Separate multiple words with an underscore like number_of_rooms, car_color.
# Python reserved words cannot be used as variable names. We will see a list of these later. 

print('Hello, "my name" is Nico.')

print("Hello"+" "+"Nico")

Celsius = 25

Farenheit = (Celsius * 9/5) + 32
print(Farenheit)

def show_colors():
    print("Red")
    print("Blue")

show_colors()
show_colors()
show_colors()

def Farenheit(celsius):
    farenheit = (celsius * 9/5) + 32
    return farenheit

F = Farenheit(25)
print(F)
Farenheit(30)

def add(a,b):
    return a + b

print(add(1,2))
