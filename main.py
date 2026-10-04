from ufs import dfs
from ufs import bfs


labirinto_exemplo = [

        [2, 0, 0, 0, 1],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 1, 0, 0, 1],
        [0, 0, 0, 3, 1]

]

#Implementação BFS

bfs.bfs(labirinto_exemplo)

print("\n--------------------------------------------------------------------")

#Implementação DFS

caminho = dfs.busca_em_profundidade(labirinto_exemplo)
dfs.descrever_passos(caminho)


