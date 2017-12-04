print ("Sintaxix: nombreDiccionario={clave:valor, clave:valor,...}")

miDiccionario = {"Colombia":"Bogota",
                 "Argentina":"Buenos Aires",
                 "Brasil":"Brasilia"}

print (miDiccionario["Colombia"])
print (miDiccionario)
miDiccionario["Peru"]="Quito"
print (miDiccionario)
miDiccionario["Peru"]="Lima"
print (miDiccionario)
del miDiccionario["Brasil"]
print (miDiccionario)
otroDiccionario = {"Ecuador":"Quito",
                   10:"James",
                   "Mosqueteros":3}
print (otroDiccionario)

tupla = ("Venezuela", "Paraguay", "Uruguay", "Bolivia")
Diccionario3 = {tupla[0]:"Caracas",
                tupla[1]: "Asuncion",
                tupla[2]: "Montevideo",
                tupla[3]: "La Paz"}
print (Diccionario3)
print (Diccionario3[tupla[2]])
print (Diccionario3["Paraguay"])

Diccionario4 = {23:"Jordan",
                "Nombre": "Jordan",
                "Equipo": "Chicago",
                "Anillos": [1991, 1992, 1993, 1996, 1997, 1998]}
print (Diccionario4)
print (Diccionario4["Equipo"])
print (Diccionario4["Anillos"])

Diccionario5 = {23:"Jordan",
                "Nombre": "Jordan",
                "Equipo": "Chicago",
                "Anillos": {"Temporadas":[991, 1992, 1993, 1996, 1997, 1998]}}
print (Diccionario5)
print (Diccionario5["Anillos"])