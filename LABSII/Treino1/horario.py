def overlap(horario):
    aux = []
    for (dia,hora,duracao) in horario:
        for i in range(0,duracao+1):
            aux.append((dia,hora+i))
    for tpl in aux:
        if aux.count(tpl) > 1:
            return True
    return False

def horario (ucs, alunos):
	res = []
	for aluno in alunos:
		hsemanal = []
		sum_ = 0
		invalido = False 
		cadeiras = alunos[aluno]
		for cadeira in cadeiras:
			if cadeira in ucs.keys():
				hsemanal.append(ucs[cadeira])
				sum_ += ucs[cadeira][2]
			else:
				invalido = True
		if (not invalido) and (not overlap(hsemanal)):
			res.append((aluno, sum_))
	res.sort(key=lambda x: x[0])
	res.sort(key=lambda x: x[1],reverse=True)
	return res