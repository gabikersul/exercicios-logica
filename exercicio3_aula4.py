# Maneira legal de fazer

# numero1, numero2, numero3 = list(map(int, input("Enter a multiple value: ").split()))
numero1 = int(input('Digite o primeiro valor:'))
numero2 = int(input('Digite o segundo valor:'))
numero3 = int(input('Digite o terceiro valor:'))

media = float((numero1+numero2+numero3)/3)
print('Os números lidos foram:', numero1, numero2, numero3)
print('E a média é:', media)
