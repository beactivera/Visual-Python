from azja import rakSingapurWartosci
from azja import rakFilipinyWartosci
from azja import rakUzbekistanWartosci
from azja import chorobySingapurWartosci
from azja import chorobyFilipinyWartosci
from azja import chorobyUzbekistanWartosci

import matplotlib.pyplot as plt

# NA RAKA :
# --------------------------------------------------------------------
# 3 pie chart - pierwszy z title / pierwszy ,drugi i trzeci z legend
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = '<4', '5-24', '25-54', '>54'

sizesRak1 = rakSingapurWartosci
fig1, ax1 = plt.subplots()
ax1.pie(sizesRak1, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
ax1.legend(labels, title="Wiek", title_fontsize='large', loc='best', bbox_to_anchor=(0.5, 0., 0.5, 0.5), fontsize='large')
ax1.set_title("Umieralność na raka: ")
# plt.show()
plt.savefig('plots-umieralnosc/rak-Singapur.svg')


sizesRak2 = rakFilipinyWartosci
fig2, ax2 = plt.subplots()
ax2.pie(sizesRak2, autopct='%1.1f%%', startangle=90)
ax2.axis('equal')
ax2.legend(labels, title="Wiek", title_fontsize='large', loc='best', bbox_to_anchor=(0.5, 0., 0.5, 0.5), fontsize='large')
# plt.show()
plt.savefig('plots-umieralnosc/rak-Filipiny.svg')

sizesRak3 = rakUzbekistanWartosci
fig3, ax3 = plt.subplots()
ax3.pie(sizesRak2, autopct='%1.1f%%', startangle=90)
ax3.axis('equal')
ax3.legend(labels, title="Wiek", title_fontsize='large', loc='best', bbox_to_anchor=(0.5, 0., 0.5, 0.5), fontsize='large')
# plt.show()
plt.savefig('plots-umieralnosc/rak-Uzbekistan.svg')

# NA CHOROBY :
# --------------------------------------------------------------------
# 3 pie chart - pierwszy z title / pierwszy ,drugi i trzeci z legend
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels2 = '<4', '5-24', '25-54', '>54'

sizesChoroby1 = chorobySingapurWartosci
fig4, ax4 = plt.subplots()
ax4.pie(sizesChoroby1, autopct='%1.1f%%', startangle=90)
ax4.axis('equal')
ax4.legend(labels2, title="Wiek", title_fontsize='large', loc='best', bbox_to_anchor=(0.5, 0., 0.5, 0.5), fontsize='large')
ax4.set_title("Umieralność na choroby serca: ")
# plt.show()
plt.savefig('plots-umieralnosc/choroby-Singapur.svg')


sizesChoroby2 = chorobyFilipinyWartosci
fig5, ax5 = plt.subplots()
ax5.pie(sizesChoroby2, autopct='%1.1f%%', startangle=90)
ax5.axis('equal')
ax5.legend(labels2, title="Wiek", title_fontsize='large', loc='best', bbox_to_anchor=(0.5, 0., 0.5, 0.5), fontsize='large')
# plt.show()
plt.savefig('plots-umieralnosc/choroby-Filipiny.svg')

sizesChoroby3 = chorobyUzbekistanWartosci
fig6, ax6 = plt.subplots()
ax6.pie(sizesRak2, autopct='%1.1f%%', startangle=90)
ax6.axis('equal')
ax6.legend(labels, title="Wiek", title_fontsize='large', loc='best', bbox_to_anchor=(0.5, 0., 0.5, 0.5), fontsize='large')
# plt.show()
plt.savefig('plots-umieralnosc/choroby-Uzbekistan.svg')

