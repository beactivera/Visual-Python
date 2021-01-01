from main import listaEuropa
# print(listaEuropa)

krajSzwajcaria = listaEuropa[0]
krajUkraina = listaEuropa[1]
krajMoldawia = listaEuropa[2]

# krajSzwajcaria['kraj'] -- nazwy krajow

# umieralnosc na raka i choroby [PROCENTY]
rakSzwajcariaWartosci = list(krajSzwajcaria['umieralnosc']['rak'].values())
chorobySzwajcariaWartosci = list(krajSzwajcaria['umieralnosc']['choroby ukladu sercowo-naczyniowego'].values())
rakUkrainaWartosci = list(krajUkraina['umieralnosc']['rak'].values())
chorobyUkrainaWartosci = list(krajUkraina['umieralnosc']['choroby ukladu sercowo-naczyniowego'].values())
rakMoldawiaWartosci = list(krajMoldawia['umieralnosc']['rak'].values())
chorobyMoldawiaWartosci = list(krajMoldawia['umieralnosc']['choroby ukladu sercowo-naczyniowego'].values())

# woda [PROCENTY]
dostepWodaSzwajcariaWartosci = list(krajSzwajcaria['woda']['dostep do wody pitnej'].values())
dostepWodaUkrainaWartosci = list(krajUkraina['woda']['dostep do wody pitnej'].values())
dostepWodaMoldawiaWartosci = list(krajMoldawia['woda']['dostep do wody pitnej'].values())

# warunki sanitarne [NA OSOBE]
sanitarneSzwajcariaWartosci = krajSzwajcaria['woda']['podstawowe warunki sanitarne']
sanitarneUkrainaWartosci = krajUkraina['woda']['podstawowe warunki sanitarne']
sanitarneMoldawiaWartosci = krajMoldawia['woda']['podstawowe warunki sanitarne']


# zdrowie /pielegniarka, psycholog, socjal/ [ILOSC na 100 tys ludzi]
zdrowieSzwajcariaWartosci = list(krajSzwajcaria['zdrowie'].values())
zdrowieUkrainaWartosci = list(krajUkraina['zdrowie'].values())
zdrowieMoldawiaWartosci = list(krajMoldawia['zdrowie'].values())



