100
salario = int(input('Qual é o seu salário'))

if(salario<280 or salario == 280):
    valorSalarioAnterior = salario

    resultado =  salario + (salario * 0.20)

    print("Salario pos reajuste", resultado)
    print("Salario antes do reajuste", valorSalarioAnterior)
    print("Aumento de 20%")

elif(salario>280 and salario<700):
    valorSalarioAnterior = salario
    resultado = salario + (salario * 0.15)
    print("Salario pos reajuste", resultado)
    print("Salario antes do reajuste", valorSalarioAnterior)
    print("Aumento de 15%")

elif(salario>700 and salario<1500):
    valorSalarioAnterior = salario
    resultado = salario + (salario * 0.10)
    print("Salario pos reajuste", resultado)
    print("Salario antes do reajuste", valorSalarioAnterior)
    print("Aumento de 10%")

elif(salario>1500):
    valorSalarioAnterior = salario
    resultado = salario + (salario * 0.05)
    print("Salario pos reajuste", resultado)
    print("Salario antes do reajuste", valorSalarioAnterior)
    print("Aumento de 5%")

