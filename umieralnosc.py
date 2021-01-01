from main import data
import matplotlib.pyplot as plt

# NA RAKA :
# --------------------------------------------------------------------
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = '<4', '5-24', '25-54', '>54'
rakValues = list()

for i in range(3):
    rakValues.append(list(data['Afryka'][i]['umieralnosc']['rak'].values()))
    rakValues.append(list(data['AmerykaPld'][i]['umieralnosc']['rak'].values()))
    rakValues.append(list(data['AmerykaPln'][i]['umieralnosc']['rak'].values()))
    rakValues.append(list(data['Australia'][i]['umieralnosc']['rak'].values()))
    rakValues.append(list(data['Azja'][i]['umieralnosc']['rak'].values()))
    rakValues.append(list(data['Europa'][i]['umieralnosc']['rak'].values()))

rak_length = len(rakValues)

for j in rak_length:
    sizeRak = rakValues[j]
    fig, ax = plt.subplots()
    ax.pie = (sizeRak, autopct='% 1.1f %%', startangle=90)
    ax.axis('equal')
    ax.set_title("Umieralność na raka: ")
    ax.legend(labels, title="Wiek", title_fontsize='large', loc='best', bbox_to_anchor=(0.5, 0., 0.5, 0.5), fontsize='large')

    if j == 0: plt.savefig('plots-umieralnosc/rak-Szeszele.svg')
    if j == 1: plt.savefig('plots-umieralnosc/rak-Egipt.svg')
    if j == 2: plt.savefig('plots-umieralnosc/rak-Burkina.svg')
    if j == 3: plt.savefig('plots-umieralnosc/rak-Argentyna.svg')
    if j == 4: plt.savefig('plots-umieralnosc/rak-Urugwaj.svg')
    if j == 5: plt.savefig('plots-umieralnosc/rak-Boliwia.svg')
    if j == 6: plt.savefig('plots-umieralnosc/rak-USA.svg')
    if j == 7: plt.savefig('plots-umieralnosc/rak-Gwatemala.svg')
    if j == 8: plt.savefig('plots-umieralnosc/rak-Barbados.svg')
    if j == 9: plt.savefig('plots-umieralnosc/rak-Australia.svg')
    if j == 10: plt.savefig('plots-umieralnosc/rak-Fidzi.svg')
    if j == 11: plt.savefig('plots-umieralnosc/rak-Kiribati.svg')
    if j == 12: plt.savefig('plots-umieralnosc/rak-Singapur.svg')
    if j == 13: plt.savefig('plots-umieralnosc/rak-Filipiny.svg')
    if j == 14: plt.savefig('plots-umieralnosc/rak-Uzbekistan.svg')
    if j == 15: plt.savefig('plots-umieralnosc/rak-Szwajcaria.svg')
    if j == 16: plt.savefig('plots-umieralnosc/rak-Ukraina.svg')
    if j == 17: plt.savefig('plots-umieralnosc/rak-Moldawia.svg')



# NA CHOROBY :
# --------------------------------------------------------------------
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels2 = '<4', '5-24', '25-54', '>54'
chorobyValues = list()

for i in range(3):
    chorobyValues.append(list(data['Afryka'][i]['umieralnosc']['choroby ukladu sercowo-naczyniowego'].values()))
    chorobyValues.append(list(data['AmerykaPld'][i]['umieralnosc']['choroby ukladu sercowo-naczyniowego'].values()))
    chorobyValues.append(list(data['AmerykaPln'][i]['umieralnosc']['choroby ukladu sercowo-naczyniowego'].values()))
    chorobyValues.append(list(data['Australia'][i]['umieralnosc']['choroby ukladu sercowo-naczyniowego'].values()))
    chorobyValues.append(list(data['Azja'][i]['umieralnosc']['choroby ukladu sercowo-naczyniowego'].values()))
    chorobyValues.append(list(data['Europa'][i]['umieralnosc']['choroby ukladu sercowo-naczyniowego'].values()))

for j in chorobyValues:
    sizesChoroby = chorobyValues[j]
    fig, ax = plt.subplots()
    ax.pie(sizesChoroby1, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    ax.set_title("Umieralność na choroby serca: ")
    ax.legend(labels2, title="Wiek", title_fontsize='large', loc='best', bbox_to_anchor=(0.5, 0., 0.5, 0.5), fontsize='large')

    if j == 0: plt.savefig('plots-umieralnosc/choroby-Szeszele.svg')
    if j == 1: plt.savefig('plots-umieralnosc/choroby-Egipt.svg')
    if j == 2: plt.savefig('plots-umieralnosc/choroby-Burkina.svg')
    if j == 3: plt.savefig('plots-umieralnosc/choroby-Argentyna.svg')
    if j == 4: plt.savefig('plots-umieralnosc/choroby-Urugwaj.svg')
    if j == 5: plt.savefig('plots-umieralnosc/choroby-Boliwia.svg')
    if j == 6: plt.savefig('plots-umieralnosc/choroby-USA.svg')
    if j == 7: plt.savefig('plots-umieralnosc/choroby-Gwatemala.svg')
    if j == 8: plt.savefig('plots-umieralnosc/choroby-Barbados.svg')
    if j == 9: plt.savefig('plots-umieralnosc/choroby-Australia.svg')
    if j == 10: plt.savefig('plots-umieralnosc/choroby-Fidzi.svg')
    if j == 11: plt.savefig('plots-umieralnosc/choroby-Kiribati.svg')
    if j == 12: plt.savefig('plots-umieralnosc/choroby-Singapur.svg')
    if j == 13: plt.savefig('plots-umieralnosc/choroby-Filipiny.svg')
    if j == 14: plt.savefig('plots-umieralnosc/choroby-Uzbekistan.svg')
    if j == 15: plt.savefig('plots-umieralnosc/choroby-Szwajcaria.svg')
    if j == 16: plt.savefig('plots-umieralnosc/choroby-Ukraina.svg')
    if j == 17: plt.savefig('plots-umieralnosc/choroby-Moldawia.svg')




