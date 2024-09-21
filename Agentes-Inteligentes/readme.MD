# Atividade 01 - IC 2024.1

Aluno: Davi de Paula Coelho Raia dos Santos  
Curso Ciência da Computação  
NOTA: READAÇÃO JÁ ENVIADA

## Introdução

Foi utilizado a linguagem Python para desenvolver os agentes e o ambiente.  
A arquitetura usada no projeto foi a seguinte:  

Foi criado 2 Classes de Alto Nível (Agente e Ambiente):

- a classe Agente é uma classe que contém as funções que são compartilhadas entre os agentes. (agente.py)
- a classe Ambiente é uma classe que contém as leituras do ambiente junto com as variáveis que os definem. (ambiente.py)

A Classe Agente tem 2 classes filhas a classe AgenteReativo1 e a classe AgenteModelo1:

- A classe AgenteReativo1 contém um agente reativo baseado no agente reativo contido no projeto java AI indicado na atividade. Possue chances diferentes de executar ações. (Arquivo reativo_agente.py)
- A classe AgenteModelo1 contém um agente baseado em modelos, foi definido um modelo de ações que o agente deve seguir. (Arquivo b_modelo_agente.py)

## Decisões

### Classe Agente

Para auxiliar a implementação foi criado uma classe basica de agente que pode ser extendida para alcançar o objeto, essa classe é a Agente (agente.py) que contém os Métodos abstratos

``` python
def definir_acao():
    'responsável por definir a ação do agente e executá-la'

def criar_modelo():
    'Utilizada apenas por agentes baseados em modelos, para conter a       função responsável por alterar as ações.'
```

Os métodos pré implementadas da classe Agente são as seguintes:

```python
def salvar_historico(self, acao, parametro):
    'responsável por salvar o histórico para coletar resultados'
    return  [(posiçãox, posiçãoy), sentido, pontuacao_simples, pontuação_composta, acao, parametro]

def perceber(self):
    'Função importante!!!'
    'Lê o estado atual da celula em que o agente está contido'
    'Chama um método da Classe Ambiente'

def limpar(self):
    'Alterar o estado do ambiente'
    'Chama um método da Classe Ambiente'

def alterar_sentido(self, direcao):
    'Alterar o sentido, Norte, Sul, Leste, Oeste'

def andar(self):
    'Alterar posição do agente'
    'Chama um método da Classe Ambiente'

```

E a classe possue esses Atributos para guardar informações.

```python
def __init__(self, ambiente: Ambiente):
        # Sensor atual [É Home?, Sujo ou Limpo?, Obstáculo?]
        self.vsensor = [True, False, False]
        self.pontuacao = 0  # Guarda o histórico de pontuação
        self.pontuacao_v2 = 0  # Guarda o histórico de pontuação
        self.histmov = []  # Guarda o histórico de movimentos
        self.ambiente = ambiente  # Inicia o Ambiente
        self.head_pointer = "s"  # Inicia apontando para o Sul (Baixo)
        self.counter = 0  # Usado no agente baseado em modelo para contar ações
```

### Classe Ambiente

Uma decisão importante foi que cada Instancia de uma classe Agente precisa ter um ambiente associado a ela. Isso foi feito pois a classe Ambiente (Que será tratada logo abaixo) guarda a informação do tamanho do ambiente, posição do agente no ambiente, e se a célula atual está suja ou limpa.  
O Ambiente armazena os dados se sujeira por meio de uma Matriz.  

Os atributos da classe são os seguintes:

``` python
def __init__(self, x, y, caminho_ambiente):
        self.x = x # tamanho x
        self.y = y # tamanho y
        self.caminho_ambiente = caminho_ambiente # Path do arquivo
        self.local = [] # ambiente (Dinamico)
        self.__agente_x = 0 # Posição agente
        self.__agente_y = 0 # Posição agente
        self.carregar_ambiente() # Chamada para ler o arquivo .txt que contem o ambiente.
```

Essa classe não possue métodos abstratos. Porém, contem os seguintes Métodos.

``` python
def getAgenteX(self):
        return self.__agente_x

def getAgenteY(self):
    return self.__agente_y

def carregar_ambiente(self):
    """Carrega o ambiente de um arquivo para a variavel local"""

def atualizar_ambiente(self):
    '''Usado na função limpar da classe agente, atualiza o ambiente'''

def recuperar_informacao_local(self):
    '''Recupera a informação de HOME e SUJEIRA da celula atual do agente'''

# As seguintes são utilizas na função andar
# Motivo: a classe Ambiente armazena a posição do agente no ambiente
def mover_norte(self):
def mover_sul(self):
def mover_leste(self):
def mover_oeste(self):
 
```

### Classe AgenteReativo1

### Classe AgenteModelo1

## Como foi realizado os testes?

## Resultados

## Conclusões
