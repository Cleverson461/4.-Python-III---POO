class Movie:
    def __init__(self, name, year_launch, included_plan, note, duration_minutes):
        self.name = name
        self.year_launch = year_launch
        self.included_plan = included_plan
        self.note = note
        self.duration_minutes = duration_minutes
    
    def __str__(self) -> str:
        return f'Filme: {self.name}'

    def techinal_sheet(self):
        print('## Dados do Filme ##')
        print(f'Nome do Filme: {self.name}')
        print(f'Ano do Lançamento: {self.year_launch}')
        print(f'Está no plano? {self.included_plan}')
        print(f'Avaliação do Filme: {self.note}')
        print(f'Duração do Filme: {self.duration_minutes}')
        print()

mario = Movie('Super Mario Bros', 2023, False, 5.0, 125)
top_gun = Movie('Top Gun Maverick', 2022, True, 4.5, 160)



mario.techinal_sheet()
top_gun.techinal_sheet()