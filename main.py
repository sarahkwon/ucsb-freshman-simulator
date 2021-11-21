import Protagonist_class as prot
import Activity as activity
import ScheduledEvent as event
from RandomEvent import *
from UI import ui

#game starts with menu - menu loop
#mainloop - time system; player choices - , protag stats and resource changes
#exit - starts saving: record attributes of properties of all objects [save(<object.attribute>)]; break mainloop; exit application

activities = activity.addActivities("Activities.csv")
events = event.addEvents("Events_Scheduled.csv")
ui = ui()

def menu():

    return None

#    event.addEvents()
prot.name_major_input()


def main_loop():
    while True:
        
        u_inp = input("Press Enter to continue.")
        #adds all the activity names to a list so it can be passed through UI    
        activities_list = []
        for i in activities:
            activities_list.append(activities[i].name)
        #adds all the event names to a list so it can be passed through UI 
        events_list = []
        for i in event.events:
            events_list.append(event.events[i].name)

        #creates an UI menu based on the names of activities and events
        #performs the action user has selected
        #returns the choice of user's selection in code form
        choice = ui.option_selection(activities_list, events_list)
        
        #Exits the loop if user choice is "z" or "Z".
        if choice == 'z':
            print("Goodbye.")
            break
        
        
        if passiveEventCheck() == True:
            print("-------An Random Event has Happened-------")



    return None

    
main_loop()