""" 
    * Classe Produto e método desconto
    
    Desenvolva uma classe em Python para atender as seguintes especificidades de um produto:
    
    1 - Cada produto deve ter preço e um nome
    
    2 - A classe deve ter um método construtor e o método dundlu str.
    
    3 - A classe deve ter um método para desconto. 
    O método deve receber o desconto em percentual e realizar o cálculo de quanto ficaria o preço final com o desconto.

"""

class Produto:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self) -> str:
        return f'Produto {self.name} - R$ {self.price} reais'
    
    def desconto(self, perc_desconto):
        valor_desconto = (self.price / 100) * perc_desconto
        final_prince = self.price - valor_desconto
        return int(final_prince)
    
xbox = Produto('Xbox Series X', 4500)
iphone = Produto('Iphone 14 Pro', 7500)

print(xbox)
print(iphone)

print(xbox.desconto(10))
print(iphone.desconto(15))