## Kobe McManus #-# Last Updated 11/19/19 ##
import string
import random
import time
from decimal import Decimal

##################################
##############
###################
############## WORK ON THIS THING!!!!!!!!!!!!! ############################

################################################################################################# READ STUFF AT BOTTOM FOR INFO ###
tvKM = list()
tvMI = list()
tvER = list()
tvAll = list()
error = 0

def main():
    data = open("TruthValues.txt" , "r+")
    truthValues = data.readlines()

    for v in truthValues:
        km = v.split(",")[1]
        mi = v.split(",")[2]
        er = v.split(",")[0]
        tvER.append(er)
        tvKM.append(km)
        tvMI.append(mi)
        tvAll.append(v)
    
    i = 0
    print("Items in TruthValues.txt: " + str(len(tvKM)))
  #  while i < len(tvKM):
    #    print(tvKM[i] + " KM | " + tvMI[i] + " MI")
    #    i += 1
    
        
    userValueKM = input("Enter a value (KM): ")
    previousError = list()
    previousValue = list()
    iter = 0
    firstGo = True
    increment = 1.0
    enteredCorrect = False
    direction = 0
    isCorrect = 0
    valueTried = 0
    waitTime = 0.0
    initialError = 0
    errorInitGo = True

    while True:
        
        if firstGo:
            #figure this one out
            
            
        
            valueTried = float(random.randrange(0,1000,1)/100)
            output = float(round(float(valueTried) * float(userValueKM),2))
            previousError.append(0.0)
            firstGo = False
            for v in tvAll:
                if(float(v.split(",")[1]) == float(userValueKM)):
                    output = float(v.split(",")[2])
                    ##don't use previously saved value, but instead randomly guess with
                    # more precision (based on saved previous error and initialrandom)
                    
                
            
            print("Starting run with " + str(waitTime) + "s pauses")
        else:
            if(float(previousError[len(previousError)-1]) < 0.0):
                output = float(round(float(previousValue[len(previousValue)-1]) - float(increment),2))
                if(direction == int(2)):
                   increment = float(increment/10)
                direction = int(1)
            else:
                output = float(round(float(previousValue[len(previousValue)-1]) + float(increment),2))
                if(direction == int(1)):
                    increment = float(increment/10)
                direction = int(2)

        print("Output MI: " + str(output))
        if(False == enteredCorrect):
            isCorrect = input("Please enter correct value.")
            enteredCorrect = True
        
        if(float(isCorrect) != float(output)):
            error = (float(isCorrect) - float(output))
            #if(abs(float(error)) > abs(float((previousError[len(previousError)-1])))):
            if(errorInitGo):
                initialError = error
                errorInitGo = False
            previousError.append(error)
            previousValue.append(output)
        else:
            break
            error = 0
        iter += 1
        time.sleep(waitTime)
    print("Successfully found | Initial Random: " + str(valueTried))
    if(initialError < 0):
        writeOutError =  "+" + str(round(-initialError,2))
    if(initialError > 0):
        writeOutError = str(round(-initialError, 2))
    
    data.write(writeOutError + "," + str(userValueKM) + "," + str(output) +  "," + str(valueTried) + "\n")



######| Stuff to look into |######---------------------------------------------------------------------------------------------------------
## read from TruthValues.txt -- if the entered number is found already, give the answer from before !*
## check if entered number is greater than or less than the value in TruthValues.txt
## also save initialrandom to TruthValues.txt
## if number entered is greater than the one in truthvalues.txt, and the truthvalues.txt error for the previous was negative, we definitely
## want a larger factor for the initialValue. If the value in the text file for error was positive, then there's either
## the possiblity that we should find a greater factor, or lesser factor, since the previous error could have been due
## to a large overshoot which could also cause problems this time.
## In that case, ignore the possibility of an overshoot larger than the previous, and just be sure not to undershoot it, as long
## as there is no new data that states something else should be done. 
## Comparing with multiple past values in this way could help narrow down the initialrandom, making the first guess more 
## and more accurate with use. The idea isn't to always reuse previously saved answers, but to be able to locate new answers
## based on the data from other numbers and answers - no algebra involved. 
############################################################################################################################################




    


    ### not using TruthValues.txt for now

if __name__ == "__main__":
    main()

