from ambiente import Ambiente


class Agente():
    def __init__(self, ambiente: Ambiente):
        # Sensor atual [É Home?, Sujo ou Limpo?, Obstáculo?]
        self.vsensor = [True, False, False]
        self.pontuacao = 0  # Guarda o histórico de pontuação
        self.histmov = []  # Guarda o histórico de movimentos
        self.ambiente = ambiente  # Inicia o Ambiente
        self.head_pointer = "s"  # Inicia apontando para o Sul (Baixo)

    def definir_acao(self):
        """ABSTRACT

        Definir stand-by, Virar (Esquerda, direita), ir para frente
        """
        pass

    def salvar_historico(self):
        """ABSTRACT"""
        pass

    def perceber(self):
        """Buscar informação do objeto ambiente"""
        pass

    def limpar(self):
        """
        Alterar Estado do ambiete
        """
        pass

    def alterar_direcao(self):
        """
        altera direção baseado em um parametro.
        1 = n (Norte)
        2 = s (Sul)
        3 = l (Leste)
        4 = o (Oeste)
        """
        pass

    def mover(self):
        if self.head_pointer == "s":
            obstaculo = self.ambiente.mover_sul()

        self.vsensor[2] = obstaculo
