secret_number = 5

guess = input("guess the secret number ? ")
print(secret_number == int(guess))

secret_word = 9
guess_word = int(input("So, guess 7+2 ? "))

if secret_word == guess_word:
    print("bg! ")