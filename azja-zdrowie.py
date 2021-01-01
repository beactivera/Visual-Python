from azja import krajSingapur
from azja import krajFilipiny
from azja import krajUzbekistan
from azja import zdrowieSingapurWartosci
from azja import zdrowieFilipinyWartosci
from azja import zdrowieUzbekistanWartosci

import matplotlib.pyplot as plt
import numpy as np

labels = [krajSingapur['kraj'], krajFilipiny['kraj'], krajUzbekistan['kraj']]
pielegniarka = [zdrowieSingapurWartosci[0], zdrowieFilipinyWartosci[0], zdrowieUzbekistanWartosci[0]]
psycholog = [zdrowieSingapurWartosci[1], zdrowieFilipinyWartosci[1], zdrowieUzbekistanWartosci[1]]
socjal = [zdrowieSingapurWartosci[2], zdrowieFilipinyWartosci[2], zdrowieUzbekistanWartosci[2]]

barWidth = 0.25
fig, ax = plt.subplots()
# Set position of bar on X axis
r1 = np.arange(len(pielegniarka))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

# Make the plot
plt.bar(r1, pielegniarka, color='#7f6d5f', width=barWidth, edgecolor='white', label='pielegniarka')
plt.bar(r2, psycholog, color='#557f2d', width=barWidth, edgecolor='white', label='psycholog')
plt.bar(r3, socjal, color='#2d7f5e', width=barWidth, edgecolor='white', label='socjal')

# Add xticks on the middle of the group bars
plt.xlabel('kraje', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(pielegniarka))], labels)
ax.set_ylabel('ilość osób na 100 tys mieszkańców')
ax.set_title('Służba zdrowia')

# Create legend & Show graphic
plt.legend()
# plt.show()
plt.savefig('plots-zdrowie/zdrowie-Azja.svg')

# https://python-graph-gallery.com/11-grouped-barplot/
