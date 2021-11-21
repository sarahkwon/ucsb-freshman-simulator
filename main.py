import Protagonist_class as prot
from UI import ui
import Activity as activity
import ScheduledEvent as event

#game starts with menu - menu loop
#mainloop - time system; player choices - , protag stats and resource changes
#exit - starts saving: record attributes of properties of all objects [save(<object.attribute>)]; break mainloop; exit application

ui = ui()
activities = activity.addActivities("Activities.csv")

def menu():

    return None

#    event.addEvents()
prot.name_major_input()


def main_loop():
    while True:
        #Exiting:
        u_inp = input()
        if u_inp == 'end':
            break

        activities_list = []
        for i in activities:
            activities_list.append(activities[i].name)

        choice = ui.option_selection(activities_list)
        if choice == 'e':
            break
        elif choice == None:
            pass
        elif choice == 0:
            prot.protagonist.printStats()
        else:
            print(activities[choice - 1].code)
            prot.protagonist.printStatsUpdates(choice -1)



    return None


main_loop()