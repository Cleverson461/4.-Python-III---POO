""" 
    * Avaliação e Média de Nota dos Filmes
    
    Desenvolva novas funcionalidades para complementar o nosso gerenciamento da classe Filmes. Segue o escopo das funcionalidades:
    
    1 - Uma das funcionalidades requeridas é que o usuário possa realizar a avaliação de um filme passando uma nota com parâmetro e que essa nota seja salva no atributo específico da classe.
    
    2 - Assim que uma avaliação for realizada, deve ser incrementado o total de avaliadores daquele filme. Obs: Considere criar um atributo específico para esse fim. 
    
    3 - Para cada filme ter uma nota de avaliação média que consiste na divisão do total de avaliação pelo total de avaliadores.
"""

class Movie:
    def __init__(self, name, year_launch, included_plan, duration_minutes):
        self.name = name
        self.year_launch = year_launch
        self.included_plan = included_plan
        self.total_evaluation = 0
        self.duration_minutes = duration_minutes
        self.evaluators = 0
    
    def __str__(self) -> str:
        return f'Filme: {self.name}'

    def techinal_sheet(self):
        print('## Dados do Filme ##')
        print(f'Nome do Filme: {self.name}')
        print(f'Ano do Lançamento: {self.year_launch}')
        print(f'Está no plano? {self.included_plan}')
        print(f'Duração do Filme: {self.duration_minutes}')
        print(f'Avaliação do Filme: {self.total_evaluation:.2f}')
        print(f'Total Avaliadores: {self.evaluators}')
        

    def evaluate(self, note):
        self.total_evaluation += note # total_evaluantion = total_evaluantion + note
        self.evaluators += 1
        
    def average(self):
        print(f'Média do Filme {self.name}: {(self.total_evaluation / self.evaluators):.2f}')
        print()
        
mario = Movie('Super Mario Bros', 2023, False, 125)
avatar =Movie('Avatar', 2023, False, 180)
top_gun = Movie('Top Gun Maverick', 2022, True, 160)

mario.evaluate(9.5)
mario.evaluate(10.0)
mario.techinal_sheet()
mario.average()

avatar.evaluate(8.5)
avatar.evaluate(9)
avatar.evaluate(3.8)
avatar.evaluate(5.8)
avatar.techinal_sheet()
avatar.average()

top_gun.evaluate(10.0)
top_gun.techinal_sheet()
top_gun.average()