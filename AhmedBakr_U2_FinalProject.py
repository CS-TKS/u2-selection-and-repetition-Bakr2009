questions = ["How many times did you flush the toilet today? ",
             "How many times did you shower today? ",
             "How many times did you wash your hands today? ",
             "How many times did you use the laundry machine today? "]
average_water_use = [6, 40, 3, 65]
water_usage = []

print("Welcome to Water usage tracker!") #output
print("Make sure to put all of the answers in numbers!")

continue_tracking = True  # this is a boolena
for i in range(0, 4):
    print(questions[i])
    answer = input("Enter number of times (or type 'done' to finish):")# input

if answer.lower() == "done":
    continue_tracking = False
else:
    times = int(answer)
    water_usage.append(times)
# calculations
sum_usage = 0
sum_usage = sum(water_usage)
print("Your total", water_usage, "is", sum_usage, "liters.")

if sum_usage > 300:
    print("Warning: You are wasting a lot of water!")
    print("Please follow the advice below to save water!")
    print("Use the laundry machine when you have a full load to limit on usage.")
    print("You should be showering less than 10 minutes.")
    print("Fix any leaky faucet or some sort to save more water.")
elif sum_usage > 150:
    print("You are using moderate amount of water, but you can improve.")
else:
    print( "Good job! You are saving a lot of water. Keep it up!")