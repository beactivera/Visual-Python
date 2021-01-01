from amerykaPln import dostepWodaUSAWartosci
from amerykaPln import dostepWodaGwatemalaWartosci
from amerykaPln import dostepWodaBarbadosWartosci
from amerykaPln import sanitarneUSAWartosci
from amerykaPln import sanitarneGwatemalaWartosci
from amerykaPln import sanitarneBarbadosWartosci

import matplotlib.pyplot as plt

# DOSTEP DO WODY PITNEJ:
# --------------------------------------------------------------------
# 3 pie chart - pierwszy z title / pierwszy ,drugi i trzeci z legend
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'TAK', 'NIE'

sizesWoda1 = dostepWodaUSAWartosci
fig1, ax1 = plt.subplots()
ax1.pie(sizesWoda1, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
ax1.legend(labels, loc='best', bbox_to_anchor=(0.5, 0., 0.5, 0.5), fontsize='large')
ax1.set_title("Dostęp do wody pitnej: ")
# plt.show()
plt.savefig('plots-woda/woda-USA.svg')

sizesWoda2 = dostepWodaGwatemalaWartosci
fig2, ax2 = plt.subplots()
ax2.pie(sizesWoda2, autopct='%1.1f%%', startangle=90)
ax2.axis('equal')
ax2.legend(labels, loc='best', bbox_to_anchor=(0.5, 0., 0.5, 0.5), fontsize='large')
# plt.show()
plt.savefig('plots-woda/woda-Gwatemala.svg')

sizesWoda3 = dostepWodaBarbadosWartosci
fig3, ax3 = plt.subplots()
ax3.pie(sizesWoda3, autopct='%1.1f%%', startangle=90)
ax3.axis('equal')
ax3.legend(labels, loc='best', bbox_to_anchor=(0.5, 0., 0.5, 0.5), fontsize='large')
# plt.show()
plt.savefig('plots-woda/woda-Barbados.svg')

# PODSTAWOWE WARUNKI SANITARNE :
# --------------------------------------------------------------------
# Bar chart

labelsKraje = ['USA', 'Gwatemala', 'Barbados']
sizesWarunki = [sanitarneUSAWartosci, sanitarneGwatemalaWartosci, sanitarneBarbadosWartosci]
fig, ax = plt.subplots()
ax.bar(labelsKraje, sizesWarunki)
ax.set_ylabel('Procent')
ax.set_title('Podstawowe warunki sanitarne')

# plt.show()
plt.savefig('plots-woda/sanitarne-amerykaPln.svg')

