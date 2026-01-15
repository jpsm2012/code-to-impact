import random

print("Vamos brincar de zoar o amigo")

brincadeiras = (" é mendigo", " é chato", " é vacilão", " é burro","Você é tão lerdo que o Wi-Fi desiste de você!","Se burrice desse medalha, você era olímpico!")

numero_secreto = random.choice(brincadeiras)

pessoa = input("Nome: ")

print(pessoa + numero_secreto)
