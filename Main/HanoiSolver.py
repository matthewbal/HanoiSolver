"""

Prototype code to be converted into C for use on an Arduino Uno

Calculates the optimal number of disks and the time for each step
based on how long the user would like the tower of hanoi puzzle to last for

Author: Matthew Balshaw
E-mail: matt@mbm.space
Updated: 16/May/2015

"""


import time
import datetime
import math

def GatherInputs():
    print "Hello! Welcome to the Python Hanoi Calculator\n"
    invalid = True

    while invalid:
        #currDate = raw_input("What is the date today? (DD-MM-YYYY)\n")
        #currTime = raw_input("What is the time? (24hr ##:##)\n")
        currDate = "01-01-2000"
        currTime = "12:00"
        strCurrDateTime = currDate + currTime
        try:
            currDateTime = datetime.datetime.strptime(strCurrDateTime, '%d-%m-%Y%H:%M')
            print "Does ", currDateTime, " Look right?\n"
            invalid = False
        except:
            print "Invalid date/time configuration. Please try again\n\n"

    invalid = True
    while invalid:
        #endDate = raw_input("What date would you like the puzzle to be solved? (DD/MM/YYYY)\n")
        #endTime = raw_input("What time would you like the puzzle to be solved? (24hr ##:##)\n")
        endDate = "01-01-2060"
        endTime = "12:00"
        strEndDateTime = endDate + endTime
        try:
            endDateTime = datetime.datetime.strptime(strEndDateTime, '%d-%m-%Y%H:%M')
            print "Does ", endDateTime, " Look right?\n"
            invalid = False
        except:
            print "Invalid date/time configuration. Please try again\n\n"

    print "Successful!\n"
    timeBetween = (endDateTime-currDateTime).total_seconds()
    print "The seconds between the dates is ", timeBetween, " Seconds"


    steptime = 10.0

    stepsApprox = timeBetween/steptime

    approxDisks = int((math.log(stepsApprox+1))/(math.log(2)))
    print "Requires around ", approxDisks, " Disks"

    stepsNeeded = (math.pow(2, approxDisks)) - 1

    print stepsNeeded

    


if __name__ == '__main__':
    GatherInputs()
