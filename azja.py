from main import listaAzja
# print(listaAzja)

krajSingapur = listaAzja[0]
krajFilipiny = listaAzja[1]
krajUzbekistan = listaAzja[2]

# krajSingapur['kraj'] -- nazwy krajow

# umieralnosc na raka i choroby [PROCENTY]
rakSingapurWartosci = list(krajSingapur['umieralnosc']['rak'].values())
chorobySingapurWartosci = list(krajSingapur['umieralnosc']['choroby ukladu sercowo-naczyniowego'].values())
rakFilipinyWartosci = list(krajFilipiny['umieralnosc']['rak'].values())
chorobyFilipinyWartosci = list(krajFilipiny['umieralnosc']['choroby ukladu sercowo-naczyniowego'].values())
rakUzbekistanWartosci = list(krajUzbekistan['umieralnosc']['rak'].values())
chorobyUzbekistanWartosci = list(krajUzbekistan['umieralnosc']['choroby ukladu sercowo-naczyniowego'].values())

# woda [PROCENTY]
dostepWodaSingapurWartosci = list(krajSingapur['woda']['dostep do wody pitnej'].values())
dostepWodaFilipinyWartosci = list(krajFilipiny['woda']['dostep do wody pitnej'].values())
dostepWodaUzbekistanWartosci = list(krajUzbekistan['woda']['dostep do wody pitnej'].values())

# warunki sanitarne [NA OSOBE]
sanitarneSingapurWartosci = krajSingapur['woda']['podstawowe warunki sanitarne']
sanitarneFilipinyWartosci = krajFilipiny['woda']['podstawowe warunki sanitarne']
sanitarneUzbekistanWartosci = krajUzbekistan['woda']['podstawowe warunki sanitarne']

# PKB
pkbSingapur = krajSingapur['PKB']['per capita']
pkbFilipiny = krajFilipiny['PKB']['per capita']
pkbUzbekistan = krajUzbekistan['PKB']['per capita']

# zdrowie /pielegniarka, psycholog, socjal/ [ILOSC na 100 tys ludzi]
zdrowieSingapurWartosci = list(krajSingapur['zdrowie'].values())
zdrowieFilipinyWartosci = list(krajFilipiny['zdrowie'].values())
zdrowieUzbekistanWartosci = list(krajUzbekistan['zdrowie'].values())

# edukacja [ilosc]
dzieciSingapur = krajSingapur['dzieci nie chodzace do szkoly']
dzieciFilipiny = krajFilipiny['dzieci nie chodzace do szkoly']
dzieciUzbekistan = krajUzbekistan['dzieci nie chodzace do szkoly']


