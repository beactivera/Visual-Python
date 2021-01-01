from amerykaPld import krajArgentyna
from amerykaPld import krajUrugwaj
from amerykaPld import krajBoliwia
from amerykaPld import zdrowieArgentynaWartosci
from amerykaPld import zdrowieUrugwajWartosci
from amerykaPld import zdrowieBoliwiaWartosci

import matplotlib.pyplot as plt
import numpy as np

labels = [krajArgentyna['kraj'], krajUrugwaj['kraj'], krajBoliwia['kraj']]
pielegniarka = [zdrowieArgentynaWartosci[0], zdrowieUrugwajWartosci[0], zdrowieBoliwiaWartosci[0]]
psycholog = [zdrowieArgentynaWartosci[1], zdrowieUrugwajWartosci[1], zdrowieBoliwiaWartosci[1]]
socjal = [zdrowieArgentynaWartosci[2], zdrowieUrugwajWartosci[2], zdrowieBoliwiaWartosci[2]]

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
plt.savefig('plots-zdrowie/zdrowie-AmerykaPld.svg')

# https://python-graph-gallery.com/11-grouped-barplot/
