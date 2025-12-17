print("Bem vindo ao formador de contrato.")
print("Coloque as informações a seguir:")

contratante = input("Nome do CONTRATANTE: ")
contratado = input("Nome do CONTRATADO: ")
servico = input("Descrição do serviço: ")
valor = input("Valor do serviço (R$): ")
data_inicio = input("Data de início: ")
data_fim = input("Data de término: ")
cidade = input("Cidade: ")
data = input("Data de assinatura: ")
 
print("====CONTRATO====")


print(f"""
CONTRATANTE: {contratante}
CONTRATADO: {contratado}

CLÁUSULA 1ª – DO OBJETO
O presente contrato tem como objeto a prestação do seguinte serviço:
{servico}

CLÁUSULA 2ª – DO PRAZO
O serviço será realizado do dia {data_inicio} até {data_fim}.

CLÁUSULA 3ª – DO VALOR
O valor total do serviço será de R$ {valor}.

CLÁUSULA 4ª – DO FORO
Fica eleito o foro da comarca de {cidade} para resolver quaisquer questões.

E, por estarem de acordo, assinam o presente contrato.

Local e data: {cidade}, {data}

Assinatura do CONTRATANTE: __________ {contratante} __________

Assinatura do CONTRATADO: __________ {contratado} __________
""")
