# Andrew Olague - Assignment 2
# Program: 100 Bottles of Beer Countdown

def countdown_bottles(bottles):
    for i in range(bottles, 0, -1):
        if i > 1:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer. Take one down and pass it around, {i-1} bottle(s) of beer on the wall.\n")
        else:
            print(f"1 bottle of beer on the wall, 1 bottle of beer. Take one down and pass it around, no more bottles of beer on the wall.\n")

# Main program
num_bottles = int(input("Enter number of bottles: "))
countdown_bottles(num_bottles)
print("Time to buy more beer!")
