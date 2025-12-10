horas = float(input(coloque quantas horas voce joga em media:))
dias = int(input(a quantos dias voce joga:))

total= horas *dias

if total <= 100:
    print("Noob")
elif total<= 500:
    print("Casca Grossa")
elif total<= 1000:
    print("Veterano")
else:
    print("Lenda")
