from ambiente import Ambiente
from reativo_agente import AgenteReativo1
a = Ambiente(4, 4)
a.carregar_ambiente()


agente = AgenteReativo1(a)

for i in range(100):
    agente.definir_acao()

# print(agente.pontuacao)
with open("result.txt", "w") as r:
    i = 0
    for line in agente.histmov:

        r.write("iteração " + str(i)+": "+str(line)+"\n")
        i = i + 1
