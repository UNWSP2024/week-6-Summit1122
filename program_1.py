
# Program #1: Random Dice
# Write a "randDice" function (with no input) that randomly chooses two numbers between 1 and 6 (inclusive) and then adds them (this is to simulate the rolling of 2 dice).  
# The dice sum will be the output of this function.
import random

def randDice():
    # Write your logic to generate 2 numbers between 1 and 6 here
    MIN = 1
    MAX = 6
    num_1 = random.randint(MIN, MAX)
    num_2 = random.randint(MIN, MAX)
    # Sum 2 numbers
    sum = num_1 + num_2
    # return sum to calling function
    return sum
#########
# Then write a mainline that calls the "randDice" function 100 times in a for loop.  
# The mainline then prints the average of the 100 rolls, rounded to the nearest 0.01.
def main():
    total = 0
    for i in range(1,101):
        number_roll = randDice()
        total =  total + number_roll

    average = total/100
    print("This program will show the average of a 100 dice rolls")
    print(f"The average after 100 rolls was: {average}")

main()