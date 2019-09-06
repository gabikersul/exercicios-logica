tempo = float(input('Informe o tempo gasto na viagem em horas:'))
velocidade_media = float(input('Informe a velocidade média em km/h:'))

dis = float(tempo*velocidade_media)
litros = float(dis/12)

print('Foram gastos:', litros, 'litros na viagem')
