for i in range (1,11):
    print (i)
for i in range (1,6):
    print(i, "ola mundo")
for i in range (1,10,2):
    print(i)
for i in range(10,0,-1):
    print(i)
for i in range(100,4,-25):
    print(i)
for i in range (0,17,4):
    print(i)
for i in range(5,0,-2):
    print(i)
for contador in range (1,10,+1):
    print(contador)
n = 10
soma = 0
for i in range(1, n +1):
    soma+= i
    print(f'a soma dos primeiros {n} numeros naturais é: {soma}')

for i in range (1,11):
    print(i)
for i in range(2,21,2):
    print(i)
for i in range(5,0,-1):
    print(i)
n = 10
soma = 0
for i in range(1, n +1):
    soma += i
print(f'a soma dos primeiros {n} numeros é:{soma}')
for i in range(0,51,5):
    print(i)
n = 10
for i in range(0,n +1):
    print(f'tabuada do 5 x {i} é {5*i}')
palavra = "hello word"
for i in range(len(palavra)):
    print(f"caractereno indice {i}: {palavra[i]}")
frutas = ['maça', 'banana', 'laranja']
for i in range(len(frutas)):
    print(f'fruta no indice {i}: {frutas[i]}')

frutas = ["maça", "banana", "laranja"]
for indece, fruta in enumerate(frutas):
    print(f'indice: {indice}, fruta: {fruta}')
for i in range (10,30):
    if i > 20:
        print(f"o primeiro numero maior que 20 é: {i}")
        break
    alimentos = ["maça", "arroz","salsicha",]