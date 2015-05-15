"""
Intended for Python 2.7.9

- Calculates the optimal number of disks and the time required for each step
- considers start and end date of puzzle, as well as feasability of step times

Author: Matthew Balshaw
E-mail: matt@mbm.space
Updated: 16/May/2015
"""


import datetime
import math

def GatherInputs():
    print "Hello! Welcome to the Python Hanoi Calculator\n"
    
    invalid = True
    while invalid:
        currDate = raw_input("What is the date today? (DD-MM-YYYY)\n")
        currTime = raw_input("What is the time? (24hr ##:##)\n")
        #currDate = "01-01-2000"
        #currTime = "12:00"
        
        strCurrDateTime = currDate + currTime
        try:
            currDateTime = datetime.datetime.strptime(strCurrDateTime, '%d-%m-%Y%H:%M')
            print "Does", currDateTime, "Look right?\n"
            invalid = False
        except:
            print "Invalid date/time configuration. Please try again\n\n"

    invalid = True
    while invalid:
        endDate = raw_input("What date would you like the puzzle to be solved? (DD/MM/YYYY)\n")
        endTime = raw_input("What time would you like the puzzle to be solved? (24hr ##:##)\n")
        #endDate = "01-01-2060"
        #endTime = "12:00"
        
        strEndDateTime = endDate + endTime
        try:
            endDateTime = datetime.datetime.strptime(strEndDateTime, '%d-%m-%Y%H:%M')
            print "Does", endDateTime, "Look right?\n"
            invalid = False
        except:
            print "Invalid date/time configuration. Please try again\n\n"

    invalid = True
    while invalid:
        print "Remember, the more time between the fastest step time and the desired step time, the quicker robot will be able to catch up after a break!"
        fastestStepTime = raw_input("Fastest time for the longest step?\n")
        desiredStepTime = raw_input("Desired step time?\n")
        #fastestStepTime = 5
        #desiredStepTime = 10.0
        
        try:
            fastestStepTime
            desiredStepTime

            minStepTime = float(desiredStepTime) * 0.75

            if float(fastestStepTime) < minStepTime:
                
                invalid = False
            else:
                print fastestStepTime, minStepTime
                print "Picked invalid step times!\n\n"
        except:
            print "Bad Input\n\n"


    print "Successful Input!\n\n"

    print "####################DATA####################"
    
    timeBetween = (endDateTime-currDateTime).total_seconds()
    print "The time between the dates is", timeBetween, "Seconds"
    print "Which is", ((((timeBetween)/60)/60)/24)/365, "Years"
    
    stepsApprox = timeBetween/minStepTime

    approxDisks = int((math.log(stepsApprox+1))/(math.log(2)))
    print "Requires around", approxDisks, "Disks"

    stepsNeeded = (math.pow(2, approxDisks)) - 1

    print "To solve for", approxDisks, "disks we need", int(stepsNeeded), "steps to complete"

    timePerStep = timeBetween/stepsNeeded

    print "Each step should take", timePerStep, "Seconds"
    print "\n\n\n"

    
if __name__ == '__main__':
    running = True
    while running:
        GatherInputs()
        runAgain = raw_input("Press Enter to run again\n\n")
        if runAgain != "":
            running = False
            








    
