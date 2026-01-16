print ("===MEDIDOR DE PERSONAGEM===")

nome = input("Digite o nome do personagem: ")
forca = int(input("Digite a força (0 a 10): "))
velocidade = int(input("Digite a velocidade (0 a 10): "))
inteligencia = int(input("Digite a inteligência (0 a 10): "))

poder = (forca + velocidade + inteligencia )/ 3

print("\nPersonagem:", nome)
print("Poder total:", poder,"de 10")

if poder >= 10:
    print("Nível: LENDÁRIO")
elif poder >= 7:
    print("Nível: FORTE")
else:
    print("Nível: FRACO")
