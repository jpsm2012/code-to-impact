print("ola ,coloque as informaçoes para calcularmos a sua taxa de aproveitamento:")
k = int(input("Kills: "))
p = int(input("Players: "))

print("seu aproveitamento foi =>")
if p == 0:
    print("Não dá ")
elif k*100/p > 80:
    print("MASTER ")
elif k*100/p >= 60:
    print("MARAVILHOSO ")
elif k*100/p > 30:
    print("BOM ")
else:
    print("RUIM ")
