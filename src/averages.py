#
# File to display plots of averages
#
#

# Dependencies
import os, sys
import csv
import matplotlib.pyplot as plt

def displayAverages(noOfDays, baseLogDir):
    # Initialise arrays to hold data
    data = {
        "days" : [],
        "maximumSteps" : [],
        "visionRadius" : [],
        "rechargeDuration" : [],
        "population" : []
    }

    # Iterate over each day
    for i in range(int(noOfDays)):
        # Read file
        file = open(os.path.join(baseLogDir, "day"+str(i), "playerConfig"))
        reader = csv.reader(file)
        # Initialise variable to hold daily averages
        avgMaxSteps = 0
        avgVisionRadius = 0
        avgRechargeDuration = 0
        pop = 0
        # Iterate over each player
        for row in reader:
            pop = pop + 1
            avgMaxSteps = avgMaxSteps + float(row[1])
            avgVisionRadius = avgVisionRadius + float(row[2])
            avgRechargeDuration = avgRechargeDuration + float(row[3])
        # Calculate current day's averages
        avgMaxSteps = avgMaxSteps / pop
        avgVisionRadius = avgVisionRadius / pop
        avgRechargeDuration = avgRechargeDuration / pop
        # Append data to array
        data["days"].append(i)
        data["population"].append(pop)
        data["maximumSteps"].append(avgMaxSteps)
        data["visionRadius"].append(avgVisionRadius)
        data["rechargeDuration"].append(avgRechargeDuration)

    # Iterate over attributes
    for attribute in ["maximumSteps", "visionRadius", "rechargeDuration", "population"]:
        # Display plot
        plt.clf()
        plt.scatter(x=data["days"], y=data[attribute])
        plt.xlabel("iteration")
        plt.ylabel(attribute)
        plt.show()

# Check if module is used as script
if __name__ == "__main__":
    # Call function to display averages plot
    displayAverages(sys.argv[1], sys.argv[2])
