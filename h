horas = float(input("Quantas horas finais você fez? "))

status = ""

if horas == 0:
    status = "ZERADO - commita mais na próxima semana"
elif horas > 0 and horas < 1.5:
    status = "LIBERADO COM RESTRIÇÃO - dá pra melhorar"
elif horas >= 1.5 and horas < 3:
    status = "LIBERADO PADRÃO - tá indo bem"
else:
    status = "MODO DEUS ATIVADO - dominou a semana"

print(status)

if horas >= 3:
    print("[STATUS: LENDA VIVA - seu irmão tá olhando com inveja]")  
