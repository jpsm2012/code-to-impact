print("medidor de commits")

commits = int(input("Quantos commits você fez na semana? "))

if commits <= 2:
    nivel = "Noob"
    multiplicador = 0
elif commits <= 6:
    nivel = "Casca Grossa"
    multiplicador = 1
elif commits <= 13:
    nivel = "Pro Player"
    multiplicador = 1.5
else:
    nivel = "Lenda Viva"
    multiplicador = 2

print(f"Nível desbloqueado: {nivel}")
print(f"Multiplicador: {multiplicador}x")
