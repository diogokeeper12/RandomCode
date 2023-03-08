notas = [('Pedro', 5), ('Maria', 3), ('Carla', 5),
('Jose', 2), ('Pedro', 4), ('Maria', 5),
('Carla', 5), ('Jose', 3), ('Pedro', 3),
('Maria', 5), ('Carla', 5), ('Jose', 4),
('Pedro', 2), ('Maria', 2), ('Carla', 5),
('Jose', 3), ('Pedro', 5), ('Maria', 1),
('Carla', 3), ('Jose', 4)]


def junta(notas):
	pauta = {}
	for nome,nota in notas:
		if nome not in pauta:
			pauta[nome] = []
		pauta[nome].append(nota)
	return list(pauta.items())

print(junta(notas))
