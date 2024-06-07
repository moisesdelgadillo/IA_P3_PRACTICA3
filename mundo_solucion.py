# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 00:44:44 2024

@author: moise
"""

import heapq

def dijkstra(graph, start):
    # Inicialización
    # Creamos una cola de prioridad (min-heap)
    queue = []
    # Agregamos el nodo inicial con distancia 0
    heapq.heappush(queue, (0, start))
    # Diccionario para almacenar las distancias mínimas desde el nodo inicial
    distances = {vertex: float('infinity') for vertex in graph}
    # La distancia al nodo inicial es 0
    distances[start] = 0
    # Diccionario para rastrear el camino más corto
    shortest_path = {}

    while queue:
        # Extraemos el nodo con la distancia mínima
        current_distance, current_vertex = heapq.heappop(queue)

        # Si encontramos una distancia mayor, ignoramos este nodo
        if current_distance > distances[current_vertex]:
            continue

        # Recorremos los vecinos del nodo actual
        for neighbor, weight in graph[current_vertex].items():
            # Calculamos la nueva distancia
            distance = current_distance + weight

            # Si la nueva distancia es menor, actualizamos la distancia y el camino más corto
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                shortest_path[neighbor] = current_vertex
                # Agregamos el vecino a la cola con la nueva distancia
                heapq.heappush(queue, (distance, neighbor))

    return distances, shortest_path

# Ejemplo de uso
graph = {
    'O': {'A':3, 'B':2},
    'A': {'C':1, 'D':4},
    'B': {'C':3, 'E':4},
    'C': {'A':1, 'F':2},
    'D': {'A':4, 'T':6},
    'E': {'B':4, 'C':2, 'F':3, 'T':5},
    'F': {'C':2, 'E':3, 'T':4},
    'T': {'D':6, 'E':5, 'F':4}
}
print("En que nodo te encuentras para poder crear la ruta mas cercana a tu destino: ")
start_node = input();
distances, shortest_path = dijkstra(graph, start_node)
print(start_node)
print(f"Camino más corto desde el nodo {start_node}:", shortest_path)
