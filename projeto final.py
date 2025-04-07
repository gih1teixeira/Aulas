nome = input('digite seu nome')
idade = int(input('digite sua idade'))
if idade >= 18:
    print('cadastro permitido')
else:
    print('cadastro negado')
saldo = float(input('digite seu saldo'))
saque = float(input('digite o valor do seu saque'))
if saque >= saldo:
    print('transação aprovada')
else:
    print('saldo insuficiente')