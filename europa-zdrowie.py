from europa import krajSzwajcaria
from europa import krajUkraina
from europa import krajMoldawia
from europa import zdrowieSzwajcariaWartosci
from europa import zdrowieUkrainaWartosci
from europa import zdrowieMoldawiaWartosci

import matplotlib.pyplot as plt
import numpy as np

labels = [krajSzwajcaria['kraj'], krajUkraina['kraj'], krajMoldawia['kraj']]
pielegniarka = [zdrowieSzwajcariaWartosci[0], zdrowieUkrainaWartosci[0], zdrowieMoldawiaWartosci[0]]
psycholog = [zdrowieSzwajcariaWartosci[1], zdrowieUkrainaWartosci[1], zdrowieMoldawiaWartosci[1]]
socjal = [zdrowieSzwajcariaWartosci[2], zdrowieUkrainaWartosci[2], zdrowieMoldawiaWartosci[2]]

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
plt.savefig('plots-zdrowie/zdrowie-Europa.svg')

# https://python-graph-gallery.com/11-grouped-barplot/
