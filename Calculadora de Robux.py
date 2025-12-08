robux = int(input("Quantos Robux você possui atualmente? "))
print(f"Este é o número colocado => {robux}, continue.")

valor = int(input("Qual é o custo do bem que você quer adquirir? "))

quanto_falta = valor - robux

print(f"Faltam {quanto_falta} Robux para você conseguir comprar.")
