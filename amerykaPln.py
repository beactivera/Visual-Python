from main import listaAmerykaPln
# print(listaAmerykaPln)

krajUSA = listaAmerykaPln[0]
krajGwatemala = listaAmerykaPln[1]
krajBarbados = listaAmerykaPln[2]

# krajUSA['kraj'] -- nazwy krajow

# umieralnosc na raka i choroby [PROCENTY]
rakUSAWartosci = list(krajUSA['umieralnosc']['rak'].values())
chorobyUSAWartosci = list(krajUSA['umieralnosc']['choroby ukladu sercowo-naczyniowego'].values())
rakGwatemalaWartosci = list(krajGwatemala['umieralnosc']['rak'].values())
chorobyGwatemalaWartosci = list(krajGwatemala['umieralnosc']['choroby ukladu sercowo-naczyniowego'].values())
rakBarbadosWartosci = list(krajBarbados['umieralnosc']['rak'].values())
chorobyBarbadosWartosci = list(krajBarbados['umieralnosc']['choroby ukladu sercowo-naczyniowego'].values())

# woda [PROCENTY]
dostepWodaUSAWartosci = list(krajUSA['woda']['dostep do wody pitnej'].values())
dostepWodaGwatemalaWartosci = list(krajGwatemala['woda']['dostep do wody pitnej'].values())
dostepWodaBarbadosWartosci = list(krajBarbados['woda']['dostep do wody pitnej'].values())

# warunki sanitarne [NA OSOBE]
sanitarneUSAWartosci = krajUSA['woda']['podstawowe warunki sanitarne']
sanitarneGwatemalaWartosci = krajGwatemala['woda']['podstawowe warunki sanitarne']
sanitarneBarbadosWartosci = krajBarbados['woda']['podstawowe warunki sanitarne']

# PKB
pkbUSA = krajUSA['PKB']['per capita']
pkbGwatemala = krajGwatemala['PKB']['per capita']
pkbBarbados = krajBarbados['PKB']['per capita']

# zdrowie /pielegniarka, psycholog, socjal/ [ILOSC na 100 tys ludzi]
zdrowieUSAWartosci = list(krajUSA['zdrowie'].values())
zdrowieGwatemalaWartosci = list(krajGwatemala['zdrowie'].values())
zdrowieBarbadosWartosci = list(krajBarbados['zdrowie'].values())

# edukacja [ilosc]
dzieciUSA = krajUSA['dzieci nie chodzace do szkoly']
dzieciGwatemala = krajGwatemala['dzieci nie chodzace do szkoly']
dzieciBarbados = krajBarbados['dzieci nie chodzace do szkoly']


