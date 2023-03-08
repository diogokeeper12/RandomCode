'''

Implemente uma função que calcula a tabela classificativa de um campeonato de
futebol. A função recebe uma lista de resultados de jogos (tuplo com os nomes das
equipas e os respectivos golos) e deve devolver a tabela classificativa (lista com 
as equipas e respectivos pontos), ordenada decrescentemente pelos pontos. Em
caso de empate neste critério, deve ser usada a diferença entre o número total
de golos marcados e sofridos para desempatar, e, se persistir o empate, o nome
da equipa.

'''

def tabela (jogos):
    res = {}
    sof = {}

    for (e1, a, e2, b) in jogos:
        if e1 not in sof:
            sof[e1] = 0
        if e2 not in sof:
            sof[e2] = 0
        
        sof[e1] += a-b
        sof[e2] += b-a

    for (e1, a, e2, b) in jogos:
        if e1 not in res:
            res[e1] = 0
        if e2 not in res:
            res[e2] = 0
        if a > b:
            res[e1] += 3
        elif a == b:
            res[e1] += 1
            res[e2] += 1
        else:
            res[e2] += 3

    final = list(res.items())

    final.sort(key=lambda x: x[0]) 
    final.sort(key=lambda x: sof[x[0]],reverse=True)
    final.sort(key=lambda x: res[x[0]],reverse=True)

    return final