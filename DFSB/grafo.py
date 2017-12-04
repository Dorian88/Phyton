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
        arista = set(arista)
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

    def dfs(grafo, inicial):
        dfi = [inicial]
        vertice = []
        pila = []
        p=dfi
        inicial = inicial+1
        padre = inicial
        for hijo in grafo.__dic_grafo:
            if hijo != None:
                aux = (inicial, hijo)
                pila.append(aux)
                if hijo not in dfi:
                    #padre=inicial
                    grafo.dfs(hijo)
                    if p(hijo)>=dfi:
                        vertice = pila.pop()
                        p=min(vertice)
                else:
                    if hijo != padre:
                        vertice1 = (inicial, dfi)
                        p=min(vertice1)
        return vertice
        """
        
        pila = [inicial]
        visitado = []

        while pila:
            vertice = pila.pop()

            if vertice not in visitado:
                visitado.append(vertice)
                for vecino in grafo.__dic_grafo[vertice]:
                    if vecino not in visitado:
                        pila.append(vecino)

        return visitado
        """
if __name__=="__main__":
    """
    dic_grafo = {'A': ['B', 'C'],
                 'B': ['A', 'D', 'E'],
                 'C': ['A', 'F'],
                 'D': ['B', 'G', 'H'],
                 'E': ['B', 'G'],
                 'F': ['C'],
                 'G': ['E', 'D', 'I'],
                 'H': ['D'],
                 'I': ['G']
                 }
    """
    dic_grafo = {}
    g = Grafo(dic_grafo)


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
            g.agregar_arista({int(x_and_y[0]), int(x_and_y[1])})

    #print(g.vertices(), g.aristas())
    print(g.dfs(1))