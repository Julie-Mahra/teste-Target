print('Exercício 01: Valor da variável SOMA')

num = 13
Soma = 0
k = 0

while k < num:
    
        k = k+1
        Soma = Soma+k

print(Soma)
print('O valor da variável SOMA será 91')


print('=='*30)


print('Exercício 02: Sequência de Fibonacci')
print('=='*30)

n1 = int(0)
n2 = int(1)
n3 = int(2)

Valor = int(input('Digite um número: '))
while Valor > n3:
    n3 = n1 + n2
    n1 = n2
    n2 = n3
if Valor == 0 or Valor == 1:
    print ('O número faz parte da sequência de Fibonacci.')
elif Valor == n3:
    print ('O número faz parte da sequência de Fibonacci.')
else:
    print ('O número digitado não faz parte da sequência de Fibonacci.')

print('=='*30)

print('Exercício 03: Complete o Próximo Elemento')

print(' a) 1, 3, 5, 7,                      => 9')
print(' b) 2, 4, 8, 16, 32, 64,             => 128')
print(' c) 0, 1, 4, 9, 16, 25, 36,          => 49')
print(' d) 4, 16, 36, 64,                   => 100')
print(' e) 1, 1, 2, 3, 5, 8,                => 13')
print(' f) 2,10, 12, 16, 17, 18, 19,        => 200')

print('=='*30)

print('Exercício 04: Ribeirão Preto <-> Franca')

print('Levando em consideração as observações, quando os veículos se cruzarem na rodovia, ambos estarão com a mesma \ndistância de Ribeirão Preto, pois estarão no mesmo ponto.')

print('=='*30)

print('Exercício 05: Invertendo Caracteres de um String')

frase = "Irei, Lutarei, Não! Morrerei!"
print(frase[::-1])
frase = "Irei, Lutarei, Não! Morrerei!"
print(frase[::-2])
frase = "Irei, Lutarei, Não! Morrerei!"
print(frase[::-3])

print('=='*30)