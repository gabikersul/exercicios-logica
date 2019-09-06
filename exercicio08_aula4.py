'''
nome = str(input('Informe nome do funcionário: '))
codigo = int(input('Informe o código do funcionário: '))
salario_fixo = float(input('Informe o salário fixo de ', nome))
produtos_vendidos = int(input('Informe o número de peças vendidas por', nome))
salario_final = salario_fixo + (salario_fixo * produtos_vendidos/100)
print('O código de', nome, 'é', codigo)
print('E seu salário final é R$', salario_final)    
'''
nome = str(input('Informe nome do funcionário: '))
codigo = int(input('Informe o código do funcionário: '))
salario_fixo = float(input('Informe o salário fixo: '))
produtos_vendidos = int(input('Informe o número de peças vendidas: '))
salario_final = salario_fixo + (salario_fixo * produtos_vendidos/100)
print('O código de', nome, 'é', codigo)
print('E seu salário final é R$', salario_final)    


