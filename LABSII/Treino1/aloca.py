"""

Implemente uma função que dado um dicionário com as preferências dos alunos
por projectos (para cada aluno uma lista de identificadores de projecto, 
por ordem de preferência), aloca esses alunos aos projectos. A alocação
é feita por ordem de número de aluno, e cada projecto só pode ser feito
por um aluno. A função deve devolver a lista com os alunos que não ficaram
alocados a nenhum projecto, ordenada por ordem de número de aluno.

"""
def aloca(prefs):
    proj_escolhidos = []
    alunos_nalocados = []
    alunos_sorted = sorted(prefs.keys())
   
    for aluno in alunos_sorted:
        projetos = prefs[aluno]
        alocado = False
        for projeto in projetos:
            if projeto not in proj_escolhidos:
                proj_escolhidos.append(projeto)
                alocado = True
                break
        
        if not alocado:
            alunos_nalocados.append(aluno)

    alunos_nao_alocados_sorted = sorted(alunos_nalocados)
    return alunos_nao_alocados_sorted

        
    
