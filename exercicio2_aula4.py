imposto = 30/100
revenda = 10/100

factory_price = float(input('Preço de Fábrica do Computador:R$'))

imp = float(factory_price*imposto)
rev = float(factory_price*revenda)

final_price = float(factory_price+imp+rev)
print('O preço final do computador é R$', final_price)
