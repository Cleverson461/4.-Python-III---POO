class Animal:
    name = ""
    size = ""
    color = ""
    
    def eat(self):
        print("Animal se alimentando")
        print()
    

class Horse(Animal):
    race = ""
    
    def escape(self):
        print("Cavalo Fugindo")


class Lion(Animal):
    mane = True
    
    def hunt(self):
        print("Leão caçando")

horse = Horse()
horse.name = "Carpeado"
horse.color = "Branco"
horse.escape()
horse.eat()

lion = Lion()
lion.name = "Simba"
lion.color = "marron"
lion.hunt()
lion.eat()