from main import listaAfryka
# print(listaAfryka)

krajSeszele = listaAfryka[0]
krajEgipt = listaAfryka[1]
krajBurkina = listaAfryka[2]

# krajSeszele['kraj'] -- nazwy krajow

# umieralnosc na raka i choroby [PROCENTY]
rakSeszeleWartosci = list(krajSeszele['umieralnosc']['rak'].values())
chorobySeszeleWartosci = list(krajSeszele['umieralnosc']['choroby ukladu sercowo-naczyniowego'].values())
rakEgiptWartosci = list(krajEgipt['umieralnosc']['rak'].values())
chorobyEgiptWartosci = list(krajEgipt['umieralnosc']['choroby ukladu sercowo-naczyniowego'].values())
rakBurkinaWartosci = list(krajBurkina['umieralnosc']['rak'].values())
chorobyBurkinaWartosci = list(krajBurkina['umieralnosc']['choroby ukladu sercowo-naczyniowego'].values())

# woda [PROCENTY]
dostepWodaSeszeleWartosci = list(krajSeszele['woda']['dostep do wody pitnej'].values())
dostepWodaEgiptWartosci = list(krajEgipt['woda']['dostep do wody pitnej'].values())
dostepWodaBurkinaWartosci = list(krajBurkina['woda']['dostep do wody pitnej'].values())

# warunki sanitarne [NA OSOBE]
sanitarneSeszeleWartosci = krajSeszele['woda']['podstawowe warunki sanitarne']
sanitarneEgiptWartosci = krajEgipt['woda']['podstawowe warunki sanitarne']
sanitarneBurkinaWartosci = krajBurkina['woda']['podstawowe warunki sanitarne']

# zdrowie /pielegniarka, psycholog, socjal/ [ILOSC na 100 tys ludzi]
zdrowieSeszeleWartosci = list(krajSeszele['zdrowie'].values())
zdrowieEgiptWartosci = list(krajEgipt['zdrowie'].values())
zdrowieBurkinaWartosci = list(krajBurkina['zdrowie'].values())



