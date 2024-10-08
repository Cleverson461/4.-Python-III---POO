class Movie:
    name = ""
    year_launch = 0
    included_plan = False
    note = 0
    duration_minutes = 0

# Primeiro Filme #
mario = Movie()
mario.name = 'Super Mario Bros'
mario.year_launch = 2023
mario.included_plan = False
mario.note = 5.0
mario.duration_minutes = 130

# Segundo Filme
movie2 = Movie()
print("## Dados do Filme ##")
print(f'Nome do filme: {mario.name} \nAno do Lançamento: {mario.year_launch}')