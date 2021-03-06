from main import listaAustralia
# print(listaAustralia)

krajAustralia = listaAustralia[0]
krajFidzi = listaAustralia[1]
krajKiribati = listaAustralia[2]

# krajAustralia['kraj'] -- nazwy krajow

# umieralnosc na raka i choroby [PROCENTY]
rakAustraliaWartosci = list(krajAustralia['umieralnosc']['rak'].values())
chorobyAustraliaWartosci = list(krajAustralia['umieralnosc']['choroby ukladu sercowo-naczyniowego'].values())
rakFidziWartosci = list(krajFidzi['umieralnosc']['rak'].values())
chorobyFidziWartosci = list(krajFidzi['umieralnosc']['choroby ukladu sercowo-naczyniowego'].values())
rakKiribatiWartosci = list(krajKiribati['umieralnosc']['rak'].values())
chorobyKiribatiWartosci = list(krajKiribati['umieralnosc']['choroby ukladu sercowo-naczyniowego'].values())

# woda [PROCENTY]
dostepWodaAustraliaWartosci = list(krajAustralia['woda']['dostep do wody pitnej'].values())
dostepWodaFidziWartosci = list(krajFidzi['woda']['dostep do wody pitnej'].values())
dostepWodaKiribatiWartosci = list(krajKiribati['woda']['dostep do wody pitnej'].values())

# warunki sanitarne [NA OSOBE]
sanitarneAustraliaWartosci = krajAustralia['woda']['podstawowe warunki sanitarne']
sanitarneFidziWartosci = krajFidzi['woda']['podstawowe warunki sanitarne']
sanitarneKiribatiWartosci = krajKiribati['woda']['podstawowe warunki sanitarne']

# zdrowie /pielegniarka, psycholog, socjal/ [ILOSC na 100 tys ludzi]
zdrowieAustraliaWartosci = list(krajAustralia['zdrowie'].values())
zdrowieFidziWartosci = list(krajFidzi['zdrowie'].values())
zdrowieKiribatiWartosci = list(krajKiribati['zdrowie'].values())



