print ('URNA ELETRONICA')
print ('1 - Joao')
print ('2 - Jose')
print ('3 - Jaco')
print ('4 - Jobe')
print ('5 - Voto Nulo')
print ('6 - Voto em Branco')

opcao1 = opcao2 = opcao3 = opcao4 = opcao5 = opcao6 = 0
codigo = 1

while (codigo >= 1 and codigo <= 6):
    codigo = int(input('Informe a opcao ou zero para encerrar: '))
    if (codigo >= 1 and codigo <= 6):
        if (codigo == 1):
            opcao1 += 1
        elif (codigo == 2):
            opcao2 += + 1
        elif (codigo == 3):
            opcao3 += 1
        elif (codigo == 4):
            opcao4 += 1
        elif (codigo == 5):
            opcao5 += 1
        elif (codigo == 6):
            opcao6 += 1
print ('RESULTADO:')
print ('1 - Joao - votos' ,opcao1)
print ('2 - Jose - votos',opcao2)
print ('3 - Jaco - votos',opcao3)
print ('4 - Jobe - votos',opcao4)
print ('5 - votos nulos',opcao5)
print ('6 -  votos em branco',opcao6)