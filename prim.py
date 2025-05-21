import heapq

# Grafo valorado representando as conexões entre as cidades
grafo = {
    'BA': [('AV', 10), ('CA', 33), ('BO', 27), ('AC', 14), ('SR', 40)],
    'AV': [('BA', 10), ('CA', 25), ('SR', 38)],
    'CA': [('BA', 33), ('AV', 25)],
    'BO': [('BA', 27), ('SR', 55), ('IB', 48)],
    'AC': [('BA', 14), ('SR', 45), ('IB', 22)],
    'SR': [('BA', 40), ('AV', 38), ('AC', 45), ('IB', 35), ('BO', 55)],
    'IB': [('AC', 22), ('SR', 35), ('BO', 48)],
}

def prim(grafo, inicio):
    visitado = set()
    mst = []
    custo_total = 0
    fila = [(0, inicio, None)]  # (peso, destino, origem)

    while fila:
        peso, atual, origem = heapq.heappop(fila)

        if atual not in visitado:
            visitado.add(atual)
            if origem:
                mst.append((origem, atual, peso))
                custo_total += peso

            for vizinho, custo in grafo[atual]:
                if vizinho not in visitado:
                    heapq.heappush(fila, (custo, vizinho, atual))

    return mst, custo_total

# Executando o algoritmo
mst_resultado, custo_total = prim(grafo, 'BA')

print("Arestas da Árvore Geradora de Custo Mínimo:")
for origem, destino, peso in mst_resultado:
    print(f"{origem} — {destino} = {peso} km")

print(f"\nCusto total: {custo_total} km")
