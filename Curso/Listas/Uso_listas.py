print ("Sintaxis. nombreLista = [elemento1, elemento2,...]")
print ("Posicion en la lista se empieza desde 0")
print ("Para mostrar toda la lista: nombreLista[:], y un elemento especifico: nombreLista[indice de la posicion]")
print ("Para mostrar una porcion de la lista: nombreLista[indiceInicio(Incluye):indiceInicio(Excluye)]")
print ("Maneras abreviadas para mostrar una porcion de la lista: nombreLista[:indiceFinal] y nombreLista[indiceInicio:]")
print ("Para agregar un elemento a la lista se usa la funcion append (Lo agrega al final). Sintaxis: nombreLista.append(elementoAAgregar)")
print ("insert sirve para agregar el elemento en cualquier posicion. Sintaxis: nombreLista.insert(indice, elementoAAgregar)")
print ("extend sirve para agregar otra lista concatenando los elementos a la lista original. Sintaxis: nombreLista.extend([elemento1,...])")
print ("Otras funciones: index(elemento): devuelve la posicion del elemento. in me indoca si un elemento esta o no en una lista (elmeneto in lista)")
print ("remove elimina un elemento de la lista que se encuentra en cualquier posicion: lista.remove(elemento). Para eliminar el ultimo elemento se usa la funcion pop: lista.pop()")

print ("\nEjemplos:")
print ("1. Crear una lista de string y mostrarla en pantalla")
miLista = ["Diana", "Dorian", "Aleja", "Juan"]
print (miLista[:])
print ("\n2. Mostrar en pantalla el elemento 3 de la lista")
print (miLista[2])
print ("\n3. Mostrar en pantalla una porcion de la lista")
print (miLista[0:3])
print ("\n4. Agregar el elemento Carla a la lista")
miLista.append("Carla")
print (miLista[:])
print ("\n5. Agregar Sandra a la lista en la posicion 2")
miLista.insert(2, "Sandra")
print (miLista[:])
print ("\n6. Agregar a la lista los elementos Diego y Lucia")
miLista.extend(["Diego", "Lucia"])
print (miLista[:])
print ("\n7. Elimina de la lista a Diego y al ultimo elemento de la lista")
miLista.remove("Diego")
miLista.pop()
print (miLista[:])