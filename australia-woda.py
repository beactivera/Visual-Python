from australia import dostepWodaAustraliaWartosci
from australia import dostepWodaFidziWartosci
from australia import dostepWodaKiribatiWartosci
from australia import sanitarneAustraliaWartosci
from australia import sanitarneFidziWartosci
from australia import sanitarneKiribatiWartosci

import matplotlib.pyplot as plt

# DOSTEP DO WODY PITNEJ:
# --------------------------------------------------------------------
# 3 pie chart - pierwszy z title / pierwszy ,drugi i trzeci z legend
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'TAK', 'NIE'

sizesWoda1 = dostepWodaAustraliaWartosci
fig1, ax1 = plt.subplots()
ax1.pie(sizesWoda1, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
ax1.legend(labels, loc='best', bbox_to_anchor=(0.5, 0., 0.5, 0.5), fontsize='large')
ax1.set_title("Dostęp do wody pitnej: ")
# plt.show()
plt.savefig('plots-woda/woda-Australia.svg')

sizesWoda2 = dostepWodaFidziWartosci
fig2, ax2 = plt.subplots()
ax2.pie(sizesWoda2, autopct='%1.1f%%', startangle=90)
ax2.axis('equal')
ax2.legend(labels, loc='best', bbox_to_anchor=(0.5, 0., 0.5, 0.5), fontsize='large')
# plt.show()
plt.savefig('plots-woda/woda-Fidzi.svg')

sizesWoda3 = dostepWodaKiribatiWartosci
fig3, ax3 = plt.subplots()
ax3.pie(sizesWoda3, autopct='%1.1f%%', startangle=90)
ax3.axis('equal')
ax3.legend(labels, loc='best', bbox_to_anchor=(0.5, 0., 0.5, 0.5), fontsize='large')
# plt.show()
plt.savefig('plots-woda/woda-Kiribati.svg')

# PODSTAWOWE WARUNKI SANITARNE :
# --------------------------------------------------------------------
# Bar chart

labelsKraje = ['Australia', 'Fidzi', 'Kiribati']
sizesWarunki = [sanitarneAustraliaWartosci, sanitarneFidziWartosci, sanitarneKiribatiWartosci]
fig, ax = plt.subplots()
ax.bar(labelsKraje, sizesWarunki)
ax.set_ylabel('Procent')
ax.set_title('Podstawowe warunki sanitarne')

# plt.show()
plt.savefig('plots-woda/sanitarne-Australia.svg')

