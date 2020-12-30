import json

with open('lista.json') as f:
    data = json.load(f)

# print(data)

# pobieranie list poszczegolnych kontynentow
listaAfryka = data['Afryka']
listaAmerykaPld = data['AmerykaPld']
listaAmerykaPln = data['AmerykaPln']
listaAustralia = data['Australia']
listaAzja = data['Azja']
listaEuropa = data['Europa']

f.close()