#Github: CaptainCluster | https://github.com/CaptainCluster

#Due to this program being designed to work as automatically as possible, if the 
#endtimer is enabled, we want to end the program based on the fixed time the user 
#has inserted.
import schedule
import sys
from ..settings import SETTINGS

#Determining the specifics for when the program should end
def createSchedule():
    settingsObject = SETTINGS()
    schedule.every().day.at(settingsObject.endTime).do(endProgram)

def checkEndTimer():
    schedule.run_pending() 

def endProgram():
    print("Time is up. Ending the program now!")
    sys.exit(0)