import random

print("Vamos brincar de adivinhar o número")

numero_secreto = random.randint (1, 100)

while True:
    chute = int(input("Tente um número de 1 a 100 =>: "))

    if chute == numero_secreto:
        print("Acertou! Você é bom mesmo 😎")
        break
    elif chute > numero_secreto:
        print("Muito alto!")
    else:
        print("Muito baixo!")
