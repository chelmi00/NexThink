# https://www.geeksforgeeks.org/generate-graph-using-dictionary-python/

import itertools

nodo = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def list_to_dict(graph):
    lista = {}
    for i in range(len(graph)):
#        array = []
#        for j in range(len(graph[0])):
#            if graph[j][i] == 1:
#                array.append(nodo[j])
        array = [nodo[j] for j in range(len(graph[0])) if graph[j][i] == 1]
        lista[nodo[i]] = array
    return lista

def dict_to_list(graph):
    matriz = [[0 for _ in range(len(graph))] for _ in range(len(graph))]
    for i in graph:
        for j in graph[i]:
            for k in range(len(graph)):
                for l in range(len(graph)):
                    if nodo[k] == i and nodo[l] == j:
                        matriz[k][l] = 1
    return matriz

def find(v, visto, parent, graph):
    visto.add(v)
#    for i in range(len(graph)):
#        if graph[v][i]:
#            if i == parent:
#                continue
#            if i != parent and (i in visto or find(i, visto, v, graph)):
#                return True
#    return False
    return any(graph[v][i] and i != parent and (i in visto or find(i, visto, v, graph)) for i in range(len(graph)))

def ciclo(graph):
    if type(graph) == dict:
        graph = dict_to_list(graph)
#    for i in range (len(graph)):
#        for j in range (len(graph[0])):
#            if graph[i][j] == 1 and graph[j][i] == 1:
#                return True
    for i, j in itertools.product(range (len(graph)), range (len(graph[0]))):
        if graph[i][j] == 1 and graph[j][i] == 1:
            return True

    for v in range(len(graph)):
        visto = set()
        if v in visto:
            continue
        if find(v, visto, -1, graph):
            return True
    return False

def find_path(graph, start, end, path = None):
    if type(graph) == list:
        graph = list_to_dict(graph)
    if path is None:
        path = []
    path = path + [start]
    if start == end:
        return path
    for node in graph[start]:
        if node not in path:
            if newpath := find_path(graph, node, end, path):
                return newpath

def main():
    list_1 = [
        [0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0],
        [0,1,0,0,0,0,0],
        [0,0,1,0,0,0,0],
        [0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0],
        [1,0,0,0,0,0,0]
    ]
    dict_1 = {
        'A' : ['B','G'],
        'B' : ['C'],
        'C' : ['D'],
        'D' : ['E','F'],
        'E' : [],
        'F' : [],
        'G' : ['A']
    }

    print(f'list_1: {"Cycle detected" if ciclo(list_1) else "No cycle detected"}')
    print(f'dict_1: {"Cycle detected" if ciclo(dict_1) else "No cycle detected"}')
    return 0

def main2():
    list_2 = [
        [0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0],
        [0,1,0,0,0,0,0],
        [0,0,1,0,0,0,0],
        [0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0],
        [0,0,0,0,0,0,0]
    ]
    dict_2 = {
        'A' : ['B'],
        'B' : ['C'],
        'C' : ['D'],
        'D' : ['E','F'],
        'E' : [],
        'F' : [],
        'G' : ['A']
    }

    print("list_2, path from G to E: " + str(find_path(list_2, 'G', 'E')))
    print("dict_2, path from G to E: " + str(find_path(dict_2, 'G', 'E')))
    return 0

if __name__ == '__main__':
    main()
    main2()