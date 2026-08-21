target = 50
#here we write input inside a loop.so repeatative asks for number until found
while True:
    guess = int(input("Guess: "))

    if guess == target:
        print("Correct!")
        break
    elif guess < target:
        print("Too low")
    else:
        print("Too high")
