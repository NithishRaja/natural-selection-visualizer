#
# Test file
#
#

# Dependencies
import os, sys
import csv
import matplotlib.pyplot as plt

def displayLifetimes(noOfDays, baseLogDir):
    # Initialise object to store data
    data = {}

    # Iterate over number of days
    for i in range(int(noOfDays)):
        # Read player config file
        file = open(os.path.join(baseLogDir, "day"+str(i), "playerConfig"))
        reader = csv.reader(file)
        # Iterate over each row
        for row in reader:
            # Check if player already exists in data dict
            if not row[0] in data.keys():
                data[row[0]] = {
                    "lifetime": [],
                    "movementLimit": [],
                    "visionLimit": [],
                    "rechargeDuration": []
                }
            # Update player info on data dict
            data[row[0]]["lifetime"].append(i)
            data[row[0]]["movementLimit"].append(float(row[1]))
            data[row[0]]["visionLimit"].append(float(row[2]))
            data[row[0]]["rechargeDuration"].append(float(row[3]))

    # Iterate over attributes and display lifetime graph
    for attribute in ["movementLimit", "visionLimit", "rechargeDuration"]:
        plt.figure()
        # Iterate over all players
        for player in data.keys():
            plt.plot(data[player]["lifetime"], data[player][attribute], label=player)

        plt.xlabel("lifetime")
        plt.ylabel(attribute)
        plt.legend(bbox_to_anchor=(1, 1), loc='upper left')
        plt.tight_layout()
        plt.show()
        plt.close()

# Check if module is used as script
if __name__ == "__main__":
    # Call function to display lifetimes plot
    displayLifetimes(sys.argv[1], sys.argv[2])
