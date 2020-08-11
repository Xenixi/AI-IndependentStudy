#conversion

import string

value = 0

truthValueKm = [1,2,3,4]
truthValueMiles = [1,2,3,4]

promptNumber = 1

while promptNumber < 5:
    truthValueKm[promptNumber-1] = input("Enter truth kilometers (" + str(promptNumber) + ")")
    promptNumber = promptNumber + 1
promptNumber = 1
while promptNumber < 5:
    truthValueMiles[promptNumber-1] = input("Enter truth miles (" + str(promptNumber) + ")")
    promptNumber = promptNumber + 1
    
#value = input("Enter kilometers:")

kilometers = input("Enter km:")



