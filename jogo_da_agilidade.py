import random
import time

print("DESAFIO DO REFLEXO")
print("Quando aparecer 'AGORA!', aperte ENTER o mais rápido possível.")
print("sem robalheira!!!")

input("\nPressione ENTER quando estiver pronto...")

time.sleep(random.randint(2, 5))

print("\nAGORA!!!")

inicio = time.time()
input()
fim = time.time()

tempo = fim - inicio

if tempo < 0.05:
    print("\nIsso foi rápido demais.")
    print("Nada de truques por aqui.")
else:
    print(f"\nSeu tempo: {tempo:.3f} segundos")

    if tempo < 0.3:
        print("Reflexo excelente.")
    elif tempo < 0.6:
        print("Muito bom.")
    elif tempo < 1:
        print("Dá para melhorar.")
    else:
        print("Precisa treinar mais.")
