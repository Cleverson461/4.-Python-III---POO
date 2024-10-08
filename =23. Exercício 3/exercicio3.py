""" 
    * Cadastro de Viagem
    Desenvolva um mini cadastro de viagem que tenha os seguintes requisitos:
    
    1 - Usuário deve informar o seu nome para cadastrar um viagem
    
    2 - Usuário deve selecionar um destino com base nas instancias de objetos da classe viagem.
    
    3 - Deve ser apresentado uma mensagem indicando que o cadastro da viagem no destino especifico foi feito com sucesso.

"""

class Trip:
    def __init__(self, destiny):
        self.destiny = destiny