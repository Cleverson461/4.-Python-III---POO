from exercicio3 import Trip

trip0 = Trip("Lençóis Maranhense")
trip1 = Trip("Florianópolis")
trip2 = Trip("Gramado")
trip3 = Trip("Campos do Jordão")
trip4 = Trip("Caldas Novas")

print("E aí viajante. Temos algumas ofertas para você.")
traveler = input("Digite seu nome para começar: ")
print(f"{traveler} Temos 5 destinos que combinam com você."
      '''
      [0] - Lençóis Maranhense
      [1] - Florianópolis
      [2] - Gramado
      [3] - Campos do Jordão
      [4] - Caldas Novas
      '''
      )

choice = int(input("Selecione o destino da viagem: "))
list_trip = [trip0, trip1, trip2, trip3, trip4]

for option in list_trip:
    if choice >= 5:
        print('Esta opção não esta incluída em nossos destinos')
        break
    else:
        print(f'{traveler} sua viagem para {list_trip[choice].destiny} está marcada')
        print('Boa viagem')
        break