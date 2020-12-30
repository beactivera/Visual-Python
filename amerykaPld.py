from main import listaAmerykaPld
# print(listaAmerykaPld)

krajArgentyna = listaAmerykaPld[0]
krajUrugwaj = listaAmerykaPld[1]
krajBoliwia = listaAmerykaPld[2]

# krajArgentyna['kraj'] -- nazwy krajow

# umieralnosc na raka i choroby [PROCENTY]
rakArgentynaWartosci = list(krajArgentyna['umieralnosc']['rak'].values())
chorobyArgentynaWartosci = list(krajArgentyna['umieralnosc']['choroby ukladu sercowo-naczyniowego'].values())
rakUrugwajeWartosci = list(krajUrugwaj['umieralnosc']['rak'].values())
chorobyUrugwajWartosci = list(krajUrugwaj['umieralnosc']['choroby ukladu sercowo-naczyniowego'].values())
rakBoliwiaWartosci = list(krajBoliwia['umieralnosc']['rak'].values())
chorobyBoliwiaWartosci = list(krajBoliwia['umieralnosc']['choroby ukladu sercowo-naczyniowego'].values())

# woda [PROCENTY]
dostepWodaArgentynaWartosci = list(krajArgentyna['woda']['dostep do wody pitnej'].values())
dostepWodaUrugwajWartosci = list(krajUrugwaj['woda']['dostep do wody pitnej'].values())
dostepWodaBoliwiaWartosci = list(krajBoliwia['woda']['dostep do wody pitnej'].values())

# warunki sanitarne [NA OSOBE]
sanitarneArgentynaWartosci = krajArgentyna['woda']['podstawowe warunki sanitarne']
sanitarneUrugwajWartosci = krajUrugwaj['woda']['podstawowe warunki sanitarne']
sanitarneBoliwiaWartosci = krajBoliwia['woda']['podstawowe warunki sanitarne']

# PKB
pkbArgentyna = krajArgentyna['PKB']['per capita']
pkbUrugwaj = krajUrugwaj['PKB']['per capita']
pkbBoliwia = krajBoliwia['PKB']['per capita']

# zdrowie /pielegniarka, psycholog, socjal/ [ILOSC na 100 tys ludzi]
zdrowieArgentynaWartosci = list(krajArgentyna['zdrowie'].values())
zdrowieUrugwajWartosci = list(krajUrugwaj['zdrowie'].values())
zdrowieBoliwiaWartosci = list(krajBoliwia['zdrowie'].values())

# edukacja [ilosc]
dzieciArgentyna = krajArgentyna['dzieci nie chodzace do szkoly']
dzieciUrugwaj = krajUrugwaj['dzieci nie chodzace do szkoly']
dzieciBoliwia = krajBoliwia['dzieci nie chodzace do szkoly']


