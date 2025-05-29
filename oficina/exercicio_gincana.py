quantidade_alunos, quantidade_amigos = map(int, input().split())
grafo = [[] for i in range(quantidade_alunos + 1)]
aluno_visitado = [False] * (quantidade_alunos + 1)
def dfs(aluno):
    aluno_visitado[aluno] = True
    for amigo in grafo[aluno]:
        if not aluno_visitado[amigo]:
            dfs(amigo)
for amigos in range(quantidade_amigos):
    alunos_amigo1, alunos_amigo2 = map(int, input().split())
    grafo[alunos_amigo2].append(alunos_amigo1)
    grafo[alunos_amigo1].append(alunos_amigo2) 
times = 0
for aluno in range(1, quantidade_alunos + 1):
    if not aluno_visitado[aluno]:
        dfs(aluno)
        times += 1
print(times)
