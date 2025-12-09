print("QUANTO FALTA PARA VOCÊ FAZER 14 ANOS?")

anos = int(input("Anos: "))
meses = int(input("Meses: "))
dias = int(input("Dias: "))

idade_dias = anos * 365 + meses * 30 + dias
quatorze_dias = 14 * 365

if idade_dias < quatorze_dias:
    falta = quatorze_dias - idade_dias

    faltam_anos = falta // 365
    falta %= 365

    faltam_meses = falta // 30
    falta %= 30

    faltam_dias = falta

    print("Faltam:")
    print(faltam_anos, "anos")
    print(faltam_meses, "meses")
    print(faltam_dias, "dias")
else:
    print("Você já tem 14 anos ou mais! 🎉")
