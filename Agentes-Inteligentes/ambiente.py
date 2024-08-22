class Ambiente():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.local = []
        self.__agente_x = 1
        self.__agente_y = 1

    def carregar_ambiente(self):
        pass

    def atualizar_ambiente(self):
        pass

    def mover_norte(self):

        if self.__agente_x == 0:
            return True
        self.__agente_x -= 1

        return False

    def mover_sul(self):
        if self.__agente_x == self.x:
            return True

        self.__agente_x += 1

        return False

    def mover_leste(self):
        if self.__agente_y == self.y:
            return True

        self.__agente_y += 1

        return False

    def mover_oeste(self):
        if self.__agente_y == 0:
            return True

        self.__agente_y -= 1

        return False
