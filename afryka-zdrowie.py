from afryka import krajSeszele
from afryka import krajEgipt
from afryka import krajBurkina
from afryka import zdrowieSeszeleWartosci
from afryka import zdrowieEgiptWartosci
from afryka import zdrowieBurkinaWartosci

import matplotlib.pyplot as plt
import numpy as np

labels = [krajSeszele['kraj'], krajEgipt['kraj'], krajBurkina['kraj']]
pielegniarka = [zdrowieSeszeleWartosci[0],zdrowieEgiptWartosci[0], zdrowieBurkinaWartosci[0]]
psycholog = [zdrowieSeszeleWartosci[1],zdrowieEgiptWartosci[1], zdrowieBurkinaWartosci[1]]
socjal = [zdrowieSeszeleWartosci[2],zdrowieEgiptWartosci[2], zdrowieBurkinaWartosci[2]]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/3, pielegniarka, width, label='pielęgniarka')
rects2 = ax.bar(x + width/3, psycholog, width, label='psycholog')
rects3 = ax.bar(x + width/3, socjal, width, label='pracownik socjalny')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('100 tys mieszkańców')
ax.set_title('Służba zdrowia')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 3, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

fig.tight_layout()

plt.show()



