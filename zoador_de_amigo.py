import random

print("Vamos brincar de zoar o amigo")

brincadeiras = (" é mendigo", " é chato", " é vacilão", " é burro")

numero_secreto = random.choice(brincadeiras)

pessoa = input("Nome: ")

print(pessoa + numero_secreto)
