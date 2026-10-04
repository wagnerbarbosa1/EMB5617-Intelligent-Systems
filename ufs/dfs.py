def teste_objetivo(posicao_atual, labirinto):
    """Verifica se a célula atual é o objetivo (3)."""
    linha, coluna = posicao_atual
    return labirinto[linha][coluna] == 3


def funcao_sucessor(posicao_atual, labirinto):
    """Retorna os vizinhos válidos (cima, baixo, esquerda, direita) dentro dos limites e sem paredes."""
    n = len(labirinto)
    linha, coluna = posicao_atual
    sucessores = []

    # Movimentos: Cima, Baixo, Esquerda, Direita
    movimentos = [
        (-1, 0),  # Cima
        (1, 0),   # Baixo
        (0, -1),  # Esquerda
        (0, 1)    # Direita
    ]

    for ml, mc in movimentos:
        #ml = move linha, mc = move coluna
        nova_linha = linha + ml
        nova_coluna = coluna + mc

        # Confere se está dentro dos limites da matriz e não é parede (1)
        if 0 <= nova_linha < n and 0 <= nova_coluna < n:
            if labirinto[nova_linha][nova_coluna] != 1:
                sucessores.append((nova_linha, nova_coluna))

    return sucessores


def encontrar_posicao(labirinto, valor):
    """Encontra as coordenadas de um número (ex: 2 para início)."""
    for i in range(len(labirinto)):
        for j in range(len(labirinto[i])):
            if labirinto[i][j] == valor:
                return (i, j)
    return None


def busca_em_profundidade(labirinto):
    inicio = encontrar_posicao(labirinto, 2)
    if not inicio:
        return None

    # Pilha guarda: (posicao_atual, caminho_ate_aqui)
    pilha = [(inicio, [inicio])]
    visitados = set()

    while pilha:
        atual, caminho = pilha.pop()

        # 1. Teste de objetivo
        if teste_objetivo(atual, labirinto):
            return caminho

        # 2. Se já foi expandido por outro ramo mais profundo, ignora
        if atual in visitados:
            continue
        visitados.add(atual)

        # 3. Gera sucessores
        for vizinho in funcao_sucessor(atual, labirinto):
            if vizinho not in visitados:
                pilha.append((vizinho, caminho + [vizinho]))

    return print("Não há caminho possível")  # Nenhum caminho encontrado

def descrever_passos(caminho):
    print(f"DFS: Caminho encontrado com sucesso ({len(caminho) - 1} passos):\n")
    print(f"Passo 0: Início na Linha {caminho[0][0]}, Coluna {caminho[0][1]}")

    for i in range(1, len(caminho)):
        l_ant, c_ant = caminho[i - 1]
        l_atual, c_atual = caminho[i]

        dl = l_atual - l_ant
        dc = c_atual - c_ant

        if dl == -1:
            direcao = "CIMA ↑"
        elif dl == 1:
            direcao = "BAIXO ↓"
        elif dc == -1:
            direcao = "ESQUERDA ←"
        else:
            direcao = "DIREITA →"

        print(f"Passo {i}: foi para {direcao:<10} → Linha {l_atual}, Coluna {c_atual}")