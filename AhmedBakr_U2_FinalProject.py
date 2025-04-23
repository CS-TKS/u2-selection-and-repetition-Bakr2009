print("Welcome to Water usage tracker!")
print("Make sure to put all of the answers in numbers!")

water_usage = [7, 75, ]
questions = ["How many times did you flush the toilet today: ", "How many times did you shower today: ",
             "How many times did you brush your teeth today: ", "How many times did you wash your car today:",
             "How many times did you use the laundry machine today:", ]

continue_tracking = True  # this is a boolena
while continue_tracking:
    user = input(questions[0])  # this is a string input
    liters = int(user)
    water_usage.append(liters)  # this stores all in list

    print("You used", liters, "liters today!")  # output

    if liters < 100:
        print("Fantastic job! You are saving water!")
    elif liters > 300:
        print("You are now in the wasting water phase. Please follow the advice below to save water!")
        print("You should go to the toilet when____")
        print("You should brush your teeth only____")
        print("You should be showering only_________")
        print("Fix any leaky faucet or some sort to save more water.")
