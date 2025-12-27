inscritos_iniciais = int(input("Começa com quantos inscritos? "))
dias = int(input("Quantos dias? "))

crescimento = 1.5

inscritos = inscritos_iniciais * (crescimento ** dias)

print(f"Depois de {dias} dias:")
print(f"Total de inscritos: {int(inscritos)}")

if inscritos >= 100000:
    print("PLACA DE PRATA DESBLOQUEADA!!!")
else:
    faltam = 100000 - int(inscritos)
    print(f"Faltam {faltam} inscritos pra placa. Continua firme!!!")
