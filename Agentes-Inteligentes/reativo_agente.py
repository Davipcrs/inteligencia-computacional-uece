from random import randint
from agente import Agente


class AgenteReativo1(Agente):
    def definir_acao(self):
        self.perceber()
        self.salvar_historico("perceber", None)

        if self.vsensor[1] == True:
            self.limpar()
            self.pontuacao = self.pontuacao + 1
            self.salvar_historico("limpar", None)

        if self.vsensor[1] == False:
            rand = randint(0, 100)

            if rand <= 20:
                self.alterar_sentido("e")
                self.salvar_historico("alterar sentido", "e")

            if rand > 20 and rand <= 40:
                self.alterar_sentido("d")
                self.salvar_historico("alterar sentido", "d")

            if rand > 40 and rand <= 100:
                self.andar()
                self.salvar_historico("andar", None)

            # Adicionar randomicidade

        return super().definir_acao()
