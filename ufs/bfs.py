labirinto_exemplo = [
        [2, 0, 0, 0, 1],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 1, 0, 0, 1],
        [0, 0, 0, 3, 1]
    ]

def graphStructure(maze_matrix):
    """Cria a estrutura de vértices do grafo e os estados de fronteira do BFS"""
    state = []
    vertices = []
    goal = None

    for i in range(0, len(maze_matrix)):
        for j in range(0, len(maze_matrix[i])):
            if maze_matrix[i][j] == 0:
                state.append(False)
                vertices.append((i, j))
            if maze_matrix[i][j] == 2:
                state.append(True)
                vertices.append((i, j))
            if maze_matrix[i][j] == 3:
                state.append(False)
                vertices.append((i, j))
                goal = (i, j)

    visited = state.copy()

    return vertices, state, visited, goal

def sucessor(vertice, vertices):
    linhas, colunas = vertice

    paths = [
        (linhas+1, colunas),
        (linhas-1, colunas),
        (linhas,colunas+1),
        (linhas,colunas-1)
    ]

    sucessores = []

    for path in paths:
        if path in vertices:
            sucessores.append(path)

    return sucessores

def testeObjetivo(vertice, goal):
    return vertice == goal

def adjacencyMatrix(vertices):
    """Cria a matriz de adjacência do labirinto"""

    adj_matrix = [[0 for _ in range(len(vertices))] for _ in range(len(vertices))]

    for i in range(0, len(vertices)):
        sucessores = sucessor(vertices[i], vertices)

        for k in range(0, len(vertices)):
            if vertices[k] in sucessores:
                adj_matrix[i][k] = 1

    return adj_matrix

def boleanDotProduct(adj_matrix, states):
    """Implementação do produto escalar em um semianel booleano"""
    raw_vec = [0 for _ in range(len(states))]

    for i in range(0, len(adj_matrix)):
        search_and = False
        for j in range(0, len(states)):
            search_and = search_and or (adj_matrix[i][j] and states[j])

        raw_vec[i] = search_and

    return raw_vec

def visitedCheck(raw_vec, visited):
    """Atualiza o vetor que verifica os vértices que já foram visitados e aplica uma máscara para não retornarem"""

    new_state = [0 for _ in range(0, len(raw_vec))]
    mask = [0 for _ in range(0, len(raw_vec))]

    for i in range(0, len(raw_vec)):
        mask[i] = not(visited[i])
        new_state[i] = raw_vec[i] and mask[i]
        visited[i] = visited[i] or new_state[i]
        
    return visited, new_state

def bfs(maze_matrix):

    vertice, state, visited, goal = graphStructure(maze_matrix)
    adj_matrix = adjacencyMatrix(vertice)
    parent = [None for _ in range(len(vertice))]

    while any(state):

        for i in range(0, len(state)):
            if state[i] and testeObjetivo(vertice[i], goal):

                path = []
                current = i

                while current != None:
                    path.append(vertice[current])
                    current = parent[current]
                path.reverse()

                return path

        raw_vec = boleanDotProduct(adj_matrix, state)
        visited, new_state = visitedCheck(raw_vec, visited)

        for i in range(0, len(new_state)):
            if new_state[i]:
                for j in range(0, len(state)):
                    if state[j] and adj_matrix[i][j]:
                        parent[i] = j
                        break
        state = new_state
    return None

path = bfs(labirinto_exemplo)
if path == None:
    print("Não existe caminho")
else:
    print(f"\nBFS: Caminho encontrado com sucesso\n{path}")