#Testing file
import Protagonist_class as prot
import UI as ui
import ClassActivity as activity
import ClassEvent as event

activities = activity.addActivities("activities.csv")
name = input('Please input your name: ')
major = input('Please input your major: ')
protagonist = prot.Protagonist(name, major)

protagonist.printStats()


