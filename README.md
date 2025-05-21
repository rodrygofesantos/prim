# 🌐 Árvore Geradora de Custo Mínimo (Prim) – Cidades da Região de Barbacena

Este projeto implementa o **Algoritmo de Prim** em Python para resolver o problema da **Árvore Geradora de Custo Mínimo (MST)**. O grafo representa a interligação entre 7 cidades da região de Barbacena, com arestas ponderadas por distâncias reais aproximadas em quilômetros.

## 🏙️ Cidades Representadas (Vértices)

- BA – Barbacena  
- AV – Alfredo Vasconcelos  
- CA – Carandaí  
- BO – Barroso  
- AC – Antônio Carlos  
- SR – Senhora dos Remédios  
- IB – Ibertioga

## 🧠 Objetivo

Encontrar a **menor malha rodoviária** possível que interliga todas as cidades **sem formar ciclos**, minimizando o total de quilômetros asfaltados.

## 📐 Estrutura do Grafo

O grafo é representado como um dicionário de listas, com as distâncias como pesos:

```python
grafo = {
    'BA': [('AV', 10), ('CA', 33), ('BO', 27), ('AC', 14), ('SR', 40)],
    'AV': [('BA', 10), ('CA', 25), ('SR', 38)],
    'CA': [('BA', 33), ('AV', 25)],
    'BO': [('BA', 27), ('SR', 55), ('IB', 48)],
    'AC': [('BA', 14), ('SR', 45), ('IB', 22)],
    'SR': [('BA', 40), ('AV', 38), ('AC', 45), ('IB', 35), ('BO', 55)],
    'IB': [('AC', 22), ('SR', 35), ('BO', 48)],
}
```

## ⚙️ Execução do Algoritmo

O código aplica o **Algoritmo de Prim**, utilizando uma **fila de prioridade** (`heapq`) para selecionar a aresta de menor custo em cada passo.

```bash
python mst_prim_barbacena.py
```

### Exemplo de saída esperada:

```
Arestas da Árvore Geradora de Custo Mínimo:
BA — AV = 10 km
BA — AC = 14 km
AV — CA = 25 km
BA — BO = 27 km
AC — IB = 22 km
IB — SR = 35 km

Custo total: 133 km
```

## 📦 Requisitos

- Python 3.x (nenhuma biblioteca externa é necessária)

## 📚 Conteúdo Didático

Este projeto pode ser utilizado como recurso educacional para disciplinas de:
- Teoria dos Grafos
- Algoritmos Gulosos
- Estrutura de Dados
- Matemática Discreta

## 📝 Licença

Este projeto é de livre uso acadêmico. Crédito a [Rodrigo Fernandes dos Santos](https://github.com/rodrygofesantos).
