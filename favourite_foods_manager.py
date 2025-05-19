favourite_food = [] #list where food will be added
while True:
    print("\nWelcome to Favourite Foods Manager")
    print("Enter 0 to Exit")
    print("Enter 1 to Add foods")
    print("Enter 2 to Remove foods")
    print("Enter 3 to View favourite all foods")

    choice = input("Choose an option: ")  # Take user input

    if choice == "0":
        print("Thanks for using our Favourite Foods Manager")
        break
    elif choice == "1":
        food = input("Enter your favourite food: ")
        favourite_food.append(food)
        print(f"{food} added successfully")
    elif choice == "2":
        if not favourite_food:
            print("No foods to remove. The list is empty.")
        else:
            food = input("Enter the food name to remove: ")
            if food in favourite_food:
                favourite_food.remove(food)
                print(f"{food} removed successfully")
            else:
                print(f"{food} not found in the list")
    elif choice == "3":
        if not favourite_food:
            print("No favourite foods in the list")
        else:
            print("Your favourite foods are:")
            for idx, food in enumerate(favourite_food, start=1):
                print(f"{idx}. {food}")
    else:
        print("Invalid choice, please try again.")
