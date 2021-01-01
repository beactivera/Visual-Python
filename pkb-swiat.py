from main import data
import numpy as np
import matplotlib.pyplot as plt

pkbLabels = list()
pkbValues = list()

for i in range(3):
    pkbLabels.append(data['Afryka'][i]['kraj'])
    pkbLabels.append(data['AmerykaPld'][i]['kraj'])
    pkbLabels.append(data['AmerykaPln'][i]['kraj'])
    pkbLabels.append(data['Australia'][i]['kraj'])
    pkbLabels.append(data['Azja'][i]['kraj'])
    pkbLabels.append(data['Europa'][i]['kraj'])

for i in range(3):
    pkbValues.append(data['Afryka'][i]['PKB']['per capita'])
    pkbValues.append(data['AmerykaPld'][i]['PKB']['per capita'])
    pkbValues.append(data['AmerykaPln'][i]['PKB']['per capita'])
    pkbValues.append(data['Australia'][i]['PKB']['per capita'])
    pkbValues.append(data['Azja'][i]['PKB']['per capita'])
    pkbValues.append(data['Europa'][i]['PKB']['per capita'])

# print(pkbLabels)
# print(pkbValues)

y_pos = np.arange(len(pkbLabels))

# Create horizontal bars
plt.barh(y_pos, pkbValues)

# Create names on the y-axis
plt.yticks(y_pos, pkbLabels)

plt.title("PKB w danym kraju [per capita]")
# Show graphic
# plt.show()
plt.savefig('plot-PKB/PKB.svg')