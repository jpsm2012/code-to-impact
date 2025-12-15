print("vamos calcular a sua media:")

b1 = float(input("Nota do 1º bimestre: ").replace(",", "."))
b2 = float(input("Nota do 2º bimestre: ").replace(",", "."))
b3 = float(input("Nota do 3º bimestre: ").replace(",", "."))
b4 = float(input("Nota do 4º bimestre: ").replace(",", "."))

media = (b1 + b2 + b3 + b4) / 4

print(f"Sua média final é: {media}")

if media >= 7:
    print("Parabéns! Você foi aprovado!")
else:
    print("Nao foi dessa vez !!!")
