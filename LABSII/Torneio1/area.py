"""
--Torneio 1 Laboratórios Algorítmia II - 2022/2023
--Realizado por: A100054 - João Barbosa (Github:JPB02); A100092 - Diogo Silva (Github:diogokeeper12)
--Nota: 90%
--Exercício Área:
    Defina uma função que calcula a área de uma figura desenhada com pecas
    lineares. A função recebe uma lista de pecas, onde para cada peça se indica
    a sua localização no plano, a orientação (True significa horizontal e False
    vertical), e a dimensão.
"""

def rem_iguais(list):
    res = []
    for elem in list:
        if elem not in res:
            res.append(elem)
    return res

def area(pecas):
    areas = []
    for peca in pecas:
        if peca[2] == True:
            idx = 1
            while(idx <= peca[3]):
                areas.append((peca[0]+idx,peca[1]))
                idx += 1
        else:
            idx = 1
            while(idx <= peca[3]):
                areas.append((peca[0],peca[1]+idx))
                idx += 1
    return len(rem_iguais(areas))