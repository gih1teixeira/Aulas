rendaAnual = float(input("digite a sua renda anual:"))
credito = int(input("digite o credito do cliente:"))
dividaspendentes = int(input("digite a quantidade de dividas pendentes:"))

if rendaAnual >= 60000 and credito >= 720 and dividaspendentes == 0:
    print("taxa de juros baixa!")

elif rendaAnual >= 40000 and credito >= 680 and dividaspendentes <= 1:
    print("taxa de juros moderada! ")

elif rendaAnual >= 30000 and credito >= 650 and dividaspendentes <= 2:
    print("taxa de juros altas! ")
else:
    print("nao atende nenhum dos creditos")
for i in range(5):
    print("ola mundo", i )