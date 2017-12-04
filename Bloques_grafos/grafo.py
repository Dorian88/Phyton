#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys

class Grafo(object):

    def __init__(self, dic_grafo=None):
        if dic_grafo == None:
            dic_grafo = {}
        self.__dic_grafo = dic_grafo

    def vertices(self):
        return list(self.__dic_grafo.keys())

    def aristas (self):
        return self.__generar_aristas()

    def agregar_vertice(self, vertice):
        if vertice not in self.__dic_grafo:
            self.__dic_grafo[vertice] = []

    def agregar_arista(self, arista):
        (vertice1, vertice2) = tuple(arista)
        if vertice1 in self.__dic_grafo:
            self.__dic_grafo[vertice1].append(vertice2)
        else:
            self.__dic_grafo[vertice1] = [vertice2]

    def __generar_aristas(self):
        aristas = []
        for nodo in  self.__dic_grafo:
            for vecino in  self.__dic_grafo[nodo]:
                if {vecino, nodo} not in aristas:
                    aristas.append({nodo, vecino})
        return aristas

    def encontrar_vertices_aislados(self):
        grafo = self.__dic_grafo
        aislado = []
        for vertice in grafo:
            if not grafo[vertice]:
               aislado += [vertice]
        return aislado

    def __str__(self):
        res = "vertices: "
        for k in self.__dic_grafo:
            res += str(k)+" "
        res += "\naristas: "
        for arista in self.__generar_aristas():
            res += str(arista) + " "
        return res



    def encontrar_camino(self, vertice_ini, vertic_fin, camino = None):
        #Encuentra un camino desde el vertice inicial hasta el vertice final#

        if camino == None:
            camino = []

        grafo = self.__dic_grafo
        camino = camino + [vertice_ini]

        if vertice_ini == vertic_fin:
            return camino
        if vertice_ini not in grafo:
            return None

        for vertice in grafo[vertice_ini]:
            if vertice not in camino:
                camino_extendido = self.encontrar_camino(vertice, vertic_fin, camino)
                if camino_extendido:
                    return camino_extendido

        return None


    i = 1  # Variable para usar como contador

    #Halla los bloques de un grafo
    def dfs_bloques(grafo, inicial, visitado = [], orden_visita = {}, Pmin = {}, padre = {}, pila = []):
        visitado.append(inicial)
        orden_visita[inicial] = [grafo.i]
        Pmin[inicial] = [grafo.i]
        grafo.i += 1

        for vecino in grafo.__dic_grafo[inicial]:
            if set([inicial, vecino]) not in pila:
                pila.append(set([inicial, vecino]))

            #Digo cual es el vértice padre
            if vecino not in visitado:
                padre[vecino] = [inicial]
                grafo.dfs_bloques(vecino, visitado, orden_visita, Pmin, padre, pila)
                #Hallo los bloques del grafo
                if Pmin.get(vecino) >= orden_visita.get(inicial):
                    bloque = []
                    while True:
                        bloque.append(pila.pop())
                        if bloque[-1] == set([inicial, vecino]):
                            print(bloque)
                            break
                Pmin[inicial] = min(Pmin[inicial], Pmin[vecino])
            elif (inicial in padre) and (vecino != padre[inicial][0]):
                Pmin[inicial] = min( Pmin[inicial], orden_visita[vecino] )

        return visitado

if __name__=="__main__":
    dic_grafo = {}
    g = Grafo(dic_grafo)    # Grafo principal

    file = open('grafo.txt', 'r')
    lines = [line.rstrip('\n') for line in file]

    for l in lines:
        if l[0] == "p":
            n_and_m = " ".join(l.split())[7:].split(" ")
            n, m = int(n_and_m[0]), int(n_and_m[1])

            for v in range(1, n+1):
                g.agregar_vertice(v)

        if l[0] == "e":
            x_and_y = " ".join(l.split())[2:].split(" ")
            g.agregar_arista((int(x_and_y[0]), int(x_and_y[1])))
            g.agregar_arista((int(x_and_y[1]), int(x_and_y[0])))

    print("Los bloques del grafo son:")
    print(g.dfs_bloques(1))