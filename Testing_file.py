#Testing file
import Protagonist_class as prot
import UI as ui
import Activity as activity
import ScheduledEvent as event

activities = activity.addActivities("activities.csv")
name = input('Please input your name: ')
major = input('Please input your major: ')
protagonist = prot.Protagonist(name, major)

protagonist.printStats()


