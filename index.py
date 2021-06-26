#
# Index file
#
#

# Dependencies
import matplotlib.pyplot as plt
import json

# Local dependencies
from src.averages import displayAverages
from src.lifetimes import displayLifetimes

# Open config file
file = open("gridConfig.json")
# Parse JSON
config = json.load(file)
# Close file

# Call function to display plots
displayAverages(config["noOfDays"], config["baseLogDir"])
displayLifetimes(config["noOfDays"], config["baseLogDir"])
