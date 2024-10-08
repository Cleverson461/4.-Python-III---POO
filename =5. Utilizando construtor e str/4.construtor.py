class Movie:
    def __init__(self, name, year_launch, included_plan, note, duration_minutes):
        self.name = name
        self.year_launch = year_launch
        self.included_plan = included_plan
        self.note = note
        self.duration_minutes = duration_minutes
    
    def __str__(self) -> str:
        return f'Filme: {self.name}'

# Primeiro Filme #
movie = Movie('Super Mario bros', 2023, False, 5.0, 130)
movie2 = Movie('Avatar', 2023, False, 4.5, 220)
print(movie)
print(movie.name)
print(movie.note)

print()

print(movie2)
print(movie2.name)