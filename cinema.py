films = {
    "Finding Dory": [3,5],
    "Bourne":[18,5],
    "Tarzan":[15,5],
    "Ghost Busters":[12,5]
}

while True:
    choice = input("What film you you like to watch?: ").strip().title()

    if choice in films:
        age = int(input("How old are you?: ").strip())
        
        if age >= films[choice][0]:
            num_seats = films[choice[1]]

            if num_seats > 0:
                print("Enjoy the movie!")
                films[choice[1]] = films[choice[1]] - 1

            else:
                    print("Sorry, we're out of tickets for that show!")

        else:
            print("That movie is for older people sorry!")

    else:
        print("We don't have that film sorry!")
    