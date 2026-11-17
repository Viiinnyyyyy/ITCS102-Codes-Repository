#movie - concept

romcom = []
action = []
adventure = []
fantasy = []
drama = []


while True:
    ans = input("Do you love movies? (yes/no): ").lower()
    if ans == "yes":
        print("What kind of movies do you love to watch? \n1 romcom\n2 action\n3 adventure\n4 fantasy\n5 drama") 
        choice = int(input("Enter the number of your choice"))
        if choice == 1 :
            print("You love romcom movies")
            title = input("Enter the title of the movie: ")
            romcom.append(title)
            print("list of romcom movies: \n", romcom)
            con = input("Do you want to add another movie? (yes/no): ").lower()
            if con == "yes":
                continue
        elif choice == 2:   
            print("You love action movies")
            title = input("Enter the title of the movie: ")
            action.append(title)
            print("list of action movies: \n", action)
            con = input("Do you want to add another movie? (yes/no): ").lower()
            if con == "yes":
                continue
        elif choice == 3:
            print("You love adventure movies")
            title = input("Enter the title of the movie: ")
            adventure.append(title)
            print("list of adventure movies: \n", adventure)
            con = input("Do you want to add another movie? (yes/no): ").lower()
            if con == "yes":
                continue
        elif choice == 4:
            print("You love fantasy movies")
            title = input("Enter the title of the movie: ")
            fantasy.append(title)
            print("list of fantasy movies: \n", fantasy)
            con = input("Do you want to add another movie? (yes/no): ").lower()
            if con == "yes":
                continue
        elif choice == 5:
            print("You love drama movies")
            title = input("Enter the title of the movie: ")
            drama.append(title)
            print("list of drama movies: \n", drama)
            con = input("Do you want to add another movie? (yes/no): ").lower()
            if con == "yes":
                continue
            else:
                break
    elif ans == "no":
        print("You don't love movies")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        