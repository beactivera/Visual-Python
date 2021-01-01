from afryka import dostepWodaSeszeleWartosci
from afryka import dostepWodaEgiptWartosci
from afryka import dostepWodaBurkinaWartosci
from afryka import sanitarneSeszeleWartosci
from afryka import sanitarneEgiptWartosci
from afryka import sanitarneBurkinaWartosci

import matplotlib.pyplot as plt

# DOSTEP DO WODY PITNEJ:
# --------------------------------------------------------------------
# 3 pie chart - pierwszy z title / pierwszy ,drugi i trzeci z legend
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'TAK', 'NIE'

sizesWoda1 = dostepWodaSeszeleWartosci
fig1, ax1 = plt.subplots()
ax1.pie(sizesWoda1, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
ax1.legend(labels, loc='best', bbox_to_anchor=(0.5, 0., 0.5, 0.5), fontsize='large')
ax1.set_title("Dostęp do wody pitnej: ")
# plt.show()
plt.savefig('plots-woda/woda-Seszele.svg')


sizesWoda2 = dostepWodaEgiptWartosci
fig2, ax2 = plt.subplots()
ax2.pie(sizesWoda2, autopct='%1.1f%%', startangle=90)
ax2.axis('equal')
ax2.legend(labels, loc='best', bbox_to_anchor=(0.5, 0., 0.5, 0.5), fontsize='large')
# plt.show()
plt.savefig('plots-woda/woda-Egipt.svg')


sizesWoda3 = dostepWodaBurkinaWartosci
fig3, ax3 = plt.subplots()
ax3.pie(sizesWoda3, autopct='%1.1f%%', startangle=90)
ax3.axis('equal')
ax3.legend(labels, loc='best', bbox_to_anchor=(0.5, 0., 0.5, 0.5), fontsize='large')
# plt.show()
plt.savefig('plots-woda/woda-Burkina.svg')

# PODSTAWOWE WARUNKI SANITARNE :
# --------------------------------------------------------------------
# Bar chart

labelsKraje = ['Seszele', 'Egipt', 'Burkina']
sizesWarunki = [sanitarneSeszeleWartosci, sanitarneEgiptWartosci, sanitarneBurkinaWartosci]
fig, ax = plt.subplots()
ax.bar(labelsKraje, sizesWarunki)
ax.set_ylabel('Procent')
ax.set_title('Podstawowe warunki sanitarne')

# plt.show()
plt.savefig('plots-woda/sanitarne-Afryka.svg')


