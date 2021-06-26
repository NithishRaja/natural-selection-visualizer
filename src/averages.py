#
# File to display plots of averages
#
#

# Dependencies
import os
import csv
import matplotlib.pyplot as plt

def displayAverages():
    # Initialise number of iterations
    numberOfIterations = 100

    # Initialise arrays to hold data
    days = []
    maximumSteps = []
    visionRadius = []
    rechargeDuration = []
    population = []

    # Iterate over each day
    for i in range(numberOfIterations):
        # Read file
        file = open(os.path.join("logging", "day"+str(i), "playerConfig"))
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
        days.append(i)
        population.append(pop)
        maximumSteps.append(avgMaxSteps)
        visionRadius.append(avgVisionRadius)
        rechargeDuration.append(avgRechargeDuration)

    # Display maximumSteps plot
    plt.clf()
    plt.scatter(x=days, y=maximumSteps)
    plt.xlabel("iteration")
    plt.ylabel("maximum steps")
    plt.show()
    # Display visionRadius plot
    plt.clf()
    plt.scatter(x=days, y=visionRadius)
    plt.xlabel("iteration")
    plt.ylabel("vision radius")
    plt.show()
    # Display rechargeDuration plot
    plt.clf()
    plt.scatter(x=days, y=rechargeDuration)
    plt.xlabel("iteration")
    plt.ylabel("recharge duration")
    plt.show()
    # Display population plot
    plt.clf()
    plt.scatter(x=days, y=population)
    plt.xlabel("iteration")
    plt.ylabel("population")
    plt.show()

# Check if module is used as script
if __name__ == "__main__":
    # Call function to display averages plot
    displayAverages()
