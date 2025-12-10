print("Vamos brincar de adivinha o numero")
numero_secreto = 42

chute = int(input("tente um numero =>: "))

if chute > numero_secreto:
    print("Muito alto!")
elif chute < numero_secreto:
    print("Muito baixo!")
else:
    print("Acertou! Voce e bom mesmo => ;-)")
