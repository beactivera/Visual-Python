from afryka import krajSeszele
from afryka import krajEgipt
from afryka import krajBurkina
from afryka import zdrowieSeszeleWartosci
from afryka import zdrowieEgiptWartosci
from afryka import zdrowieBurkinaWartosci

import matplotlib.pyplot as plt
import numpy as np

labels = [krajSeszele['kraj'], krajEgipt['kraj'], krajBurkina['kraj']]
pielegniarka = [zdrowieSeszeleWartosci[0], zdrowieEgiptWartosci[0], zdrowieBurkinaWartosci[0]]
psycholog = [zdrowieSeszeleWartosci[1], zdrowieEgiptWartosci[1], zdrowieBurkinaWartosci[1]]
socjal = [zdrowieSeszeleWartosci[2], zdrowieEgiptWartosci[2], zdrowieBurkinaWartosci[2]]

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
plt.savefig('plots-zdrowie/zdrowie-Afryka.svg')

# https://python-graph-gallery.com/11-grouped-barplot/
