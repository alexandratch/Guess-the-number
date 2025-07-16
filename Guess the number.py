numar_de_ghicit = 50
numar_de_incercari = int(input("How many tries are you allowed:  "))
numar_dat = int(input("Enter a number:  "))

while numar_de_incercari > 0 and numar_dat != numar_de_ghicit:
    if numar_dat > numar_de_ghicit:
        print("The number is too big!")
    elif numar_dat < numar_de_ghicit:
        print("The number is too small!")
    else:
        print("Congrats! You guessed the number!")
        break

    numar_de_incercari -= 1
    print(f"You have {numar_de_incercari} guesses left!")

    if numar_de_incercari > 0:
        numar_dat = int(input("Enter another number:  "))

if numar_de_incercari == 0 and numar_dat != numar_de_ghicit:
    print("You lost! :(")
elif numar_dat == numar_de_ghicit:
    print("Congrats! You guessed the number!")  # În caz că ghicești din prima