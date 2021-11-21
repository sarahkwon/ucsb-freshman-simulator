#Testing file
import random
import Protagonist_class as prot
import UI as ui
import Activity as activity
import ScheduledEvent as event
import PassiveRandomEvent as passiveEvent
import ActiveRandomEvent as activeEvent

# name = input('Please input your name: ')
# major = input('Please input your major: ')
# protagonist = prot.Protagonist(name, major)

# protagonist.printStats()

# code for making random events work 
# since passive and active random events are both in separate lists:
# 1. random.choice( [active, passive, no] ) to see if a random event will trigger 
# (make the odds 50/50? 25/25/50 active/passive/noRandomEvent)
    # if active, random.choice again to choose a random active event in the list and run it
    # if passive, random.choice again to choose a random passive event in the list and run it 
    # if no, move on
# run code for the event, if its active there will probably be more code but worry about it later. 
passiveEvents = passiveEvent.addRandomEvents("Events_random_passive.csv")
passiveEvents = list(passiveEvents.items())

activeEvents = activeEvent.addRandomEvents("testActiveRandomEvent.csv")
activeEvents = list(activeEvents.items())

# see whether or not an active/passive event will occur or not
def passiveEventCheck():
    randomEventTrigger = random.choice(["passive", "noRandomEvent"])
    
    if (randomEventTrigger == "passive"):
        chosenEvent = random.choice(passiveEvents)
        return True
    else:
        print("no random event, move on")
        return False







