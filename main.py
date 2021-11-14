import Protagonist_class as protag

#game starts with menu - menu loop
#mainloop - time system; player choices - , protag stats and resource changes
#exit - starts saving: record attributes of properties of all objects [save(<object.attribute>)]; break mainloop; exit application

activities = []

def menu():

    return None

activities = activity.addActivities("activities.csv")

#    event.addEvents()
name = input('Please input your name: ')
major = input('Please input your major: ')
protagonist = prot(name, major)


def main_loop():
    while True:
        #Exiting:
        u_inp = input()
        if u_inp == 'end':
            break

        activities_list = []
        for i in activites:
            activities_list.append(activities[i].name)

        print(activities_list)
        activity_to_execute = ui.option_selection()
        print(activity_to_execute)



    return None


main_loop()