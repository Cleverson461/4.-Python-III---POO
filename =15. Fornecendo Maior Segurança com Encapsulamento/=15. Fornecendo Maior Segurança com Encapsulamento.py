class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
        
    def show(self):
        print(f'Nome {self.name} - Salário {self.__salary}')

fulano = Employee("Fulano", 4000)
sicrano = Employee("Sicrano", 5000)

fulano.show()
sicrano.show()

fulano.__salary = 40000
fulano.show()