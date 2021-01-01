from europa import dostepWodaSzwajcariaWartosci
from europa import dostepWodaUkrainaWartosci
from europa import dostepWodaMoldawiaWartosci
from europa import sanitarneSzwajcariaWartosci
from europa import sanitarneUkrainaWartosci
from europa import sanitarneMoldawiaWartosci

import matplotlib.pyplot as plt

# DOSTEP DO WODY PITNEJ:
# --------------------------------------------------------------------
# 3 pie chart - pierwszy z title / pierwszy ,drugi i trzeci z legend
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'TAK', 'NIE'

sizesWoda1 = dostepWodaSzwajcariaWartosci
fig1, ax1 = plt.subplots()
ax1.pie(sizesWoda1, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
ax1.legend(labels, loc='best', bbox_to_anchor=(0.5, 0., 0.5, 0.5), fontsize='large')
ax1.set_title("Dostęp do wody pitnej: ")
plt.show()


sizesWoda2 = dostepWodaUkrainaWartosci
fig2, ax2 = plt.subplots()
ax2.pie(sizesWoda2, autopct='%1.1f%%', startangle=90)
ax2.axis('equal')
ax2.legend(labels, loc='best', bbox_to_anchor=(0.5, 0., 0.5, 0.5), fontsize='large')
plt.show()

sizesWoda3 = dostepWodaMoldawiaWartosci
fig3, ax3 = plt.subplots()
ax3.pie(sizesWoda3, autopct='%1.1f%%', startangle=90)
ax3.axis('equal')
ax3.legend(labels, loc='best', bbox_to_anchor=(0.5, 0., 0.5, 0.5), fontsize='large')
plt.show()

# PODSTAWOWE WARUNKI SANITARNE :
# --------------------------------------------------------------------
# Bar chart

labelsKraje = ['Szwajcaria', 'Ukraina', 'Moldawia']
sizesWarunki = [sanitarneSzwajcariaWartosci, sanitarneUkrainaWartosci, sanitarneMoldawiaWartosci]
fig, ax = plt.subplots()
ax.bar(labelsKraje, sizesWarunki)
ax.set_ylabel('Procent')
ax.set_title('Podstawowe warunki sanitarne')

plt.show()


