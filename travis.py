
#8 users
known_users =["Oskar", "Caroline", "Martin", "Tobias", "Greta", "Ziyad", "Benny", "Emma"]

print(len(known_users))

while True: 
    print("Hi, my name is Travis and im a security bot")
    name = input("What is your name?: ").strip().capitalize()

    if name in known_users:
        print("Hello {}! You're already known to me, Welcome!".format(name))
        remove = input("Would you like to be removed from my memory? y/n? ").strip().lower()
        if remove == "y":
            print(known_users)
            known_users.remove(name)
            print(known_users)   
        elif remove == "n":
            print("No problem, i want to remember you!")

    else: 
        print("HEY! Who are you, i don't know you {}".format(name))
        add_me = input("{}, would you like me to add you to my memory? ".format(name)).strip().lower()
        if add_me == "y":
            print(known_users)
            known_users.append(name)
            print(known_users)
        elif add_me == "n":
            print("No worries, see you around")

        



