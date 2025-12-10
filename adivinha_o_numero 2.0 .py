print("Vamos brincar de adivinha o numero")
numero_secreto = 42

while True:
    chute = int(input("Tente um número =>: "))

    if chute == numero_secreto:
        print("Acertou! Você é bom mesmo 😉")
        break
    elif chute > numero_secreto:
        print("Muito alto!")
    else:
        print("Muito baixo!")
