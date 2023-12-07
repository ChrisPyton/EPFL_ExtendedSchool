color = input("Color ? ")
number = int(input("Number ? "))

def guess_secrets(color, number):

    secret_color = "blue"
    secret_number = 20

    if color == secret_color and number == secret_number:
        print("Well fucking done! ")
    elif color == secret_color or number == secret_number:
        print("One out of Two! ")
    else: print("Too bad! ") 

guess_secrets(color, number)

