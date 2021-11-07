from ClassActivity import ClassActivity
import csv

class ClassActivities:
    def __init__(self, fileName):
        self.activities = {}
        self.fileName = fileName

    def addActivities(self):
        # open the csv file fileName and read from it
        with open(self.fileName, newline = '') as csvfile:
            r = csv.DictReader(csvfile, delimiter=',')
            i = 0
            for row in r:
                # for each row in csvFile, append the class activity to the array activities
                self.activities[row["name"]] = ClassActivity(
                    str(row["name"]), 
                    str(row["description"]), 
                    int(row["timeCost"]), 
                    str(row["statModifiers"]), 
                    str(row["resourceModifiers"]),
                    str(row["flavor"])
                )
                i += 1

test = ClassActivities('testFile.csv')
test.addActivities()
print(test.activities)


# self.activities.append(ClassActivity(
#     str(row["name"]), 
#     str(row["description"]), 
#     int(row["timeCost"]), 
#     str(row["statModifiers"]), 
#     str(row["resourceModifiers"]),
#     str(row["flavor"])
# ))