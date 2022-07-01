import itertools

nodo = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def matriz(graph):
    matriz = [[0 for _ in range(len(graph))] for _ in range(len(graph))]
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == 1:
                matriz[i][j] = 1
    return matriz

def lista(graph):
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
    if path is None:
        path = []
    for i in range (len(graph[0])):
        if start == nodo[i]:
            start = i
        if end == nodo[i]:
            end = i

    path = path + [start]
    if start == end:
        return path
    for node in graph[start]:
        if node not in path:
            if newpath := find_path(graph, node, end, path):
                for i in range(len(newpath)):
                    newpath[i] = nodo[newpath[i]]
                return newpath

def main():
    matrix_1 = [
        [0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0],
        [0,1,0,0,0,0,0],
        [0,0,1,0,0,0,0],
        [0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0],
        [1,0,0,0,0,0,0]
    ]
    list_1 = {
        'A' : ['B','G'],
        'B' : ['C'],
        'C' : ['D'],
        'D' : ['E','F'],
        'E' : [],
        'F' : [],
        'G' : ['A']
    }
    matrix_1 = matriz(matrix_1)
    list_1 = lista(list_1)

    print(f'matrix_1: {"Cycle detected" if ciclo(matrix_1) else "No cycle detected"}')
    print(f'list_1: {"Cycle detected" if ciclo(list_1) else "No cycle detected"}')
    return 0

def main2():
    matrix_2 = [
        [0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0],
        [0,1,0,0,0,0,0],
        [0,0,1,0,0,0,0],
        [0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0],
        [0,0,0,0,0,0,0]
    ]
    list_2 = {
        'A' : ['B'],
        'B' : ['C'],
        'C' : ['D'],
        'D' : ['E','F'],
        'E' : [],
        'F' : [],
        'G' : ['A']
    }
    matrix_2 = matriz(matrix_2)
    list_2 = lista(list_2)

    print(f'matrix_2: {"Cycle detected" if ciclo(matrix_2) else "No cycle detected"}')
    print(f'list_2: {"Cycle detected" if ciclo(list_2) else "No cycle detected"}')
    print(find_path(matrix_2, 3, 1))
    return 0

if __name__ == '__main__':
    main()
    main2()