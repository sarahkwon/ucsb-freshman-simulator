import Protagonist_class as prot
from UI import ui
from ClassActivity import *
import ClassActivity as activity
import ClassEvent as event

#game starts with menu - menu loop
#mainloop - time system; player choices - , protag stats and resource changes
#exit - starts saving: record attributes of properties of all objects [save(<object.attribute>)]; break mainloop; exit application

ui = ui()

def menu():

    return None

#    event.addEvents()
name = input('Please input your name: ')
major = input('Please input your major: ')
protagonist = prot.Protagonist(name, major)


def main_loop():
    while True:
        #Exiting:
        u_inp = input()
        if u_inp == 'end':
            break

        activities_list = []
        for i in activities:
            activities_list.append(activities[i].name)

        print(activities_list)
        choice = ui.option_selection(activities_list)
        if choice == 0:
            break
        elif choice == None:
            pass
        else:
            print(activities[choice - 1].code)



    return None


main_loop()