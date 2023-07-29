# This program finds the height of a ball after being dropped at a specified time.
# The ball is dropped from a height(meters), the height of a ledge, over time (seconds)
# This program ignores air resistance.
# Peter Menchu - 2023

# definition of gravity
g = 9.81

print("A ball is dropped from the edge of a ledge.")
height = float(input("Enter height of the ledge (meters): "))
time = float(input("Enter time (seconds) to find the height at that time: "))
# find the distance the ball has fallen 1/2(g*t^2)
distance = (g * (time ** 2)) / 2
currentHeight = height - distance

if currentHeight > 0:
    print("The current height at that time is ", currentHeight, " meters")
else:
    print("At ", time, " seconds, the ball has hit the ground after falling ", height, " meters.")

# Peter Menchu - 2023
