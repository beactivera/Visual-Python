from main import data
import numpy as np
import matplotlib.pyplot as plt

dzieciLabels = list()
dzieciValues = list()

for i in range(3):
    dzieciLabels.append(data['Afryka'][i]['kraj'])
    dzieciLabels.append(data['AmerykaPld'][i]['kraj'])
    dzieciLabels.append(data['AmerykaPln'][i]['kraj'])
    dzieciLabels.append(data['Australia'][i]['kraj'])
    dzieciLabels.append(data['Azja'][i]['kraj'])
    dzieciLabels.append(data['Europa'][i]['kraj'])

for i in range(3):
    dzieciValues.append(data['Afryka'][i]['dzieci nie chodzace do szkoly'])
    dzieciValues.append(data['AmerykaPld'][i]['dzieci nie chodzace do szkoly'])
    dzieciValues.append(data['AmerykaPln'][i]['dzieci nie chodzace do szkoly'])
    dzieciValues.append(data['Australia'][i]['dzieci nie chodzace do szkoly'])
    dzieciValues.append(data['Azja'][i]['dzieci nie chodzace do szkoly'])
    dzieciValues.append(data['Europa'][i]['dzieci nie chodzace do szkoly'])

# print(dzieciLabels)
# print(dzieciValues)

y_pos = np.arange(len(dzieciLabels))
plt.barh(y_pos, dzieciValues)
plt.title('Ilość dzieci nie chodząca do szkoły')
plt.xlabel('liczba')
plt.yticks(y_pos, dzieciLabels)

# plt.show()
plt.savefig('plot-dzieci/dzieci.svg')