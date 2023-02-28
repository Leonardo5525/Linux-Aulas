sexo = input('Qual o seu sexo M/F? ').upper()
peso = float(input('Qual é o seu peso? '))
altura = float(input('Qual a sua altura? '))

imc = peso / (altura**2)

if sexo == 'F' and imc >= 18.5 and imc <= 24.9 or sexo == 'M' and imc >= 20.7 and imc <= 26.4:
    print ('Peso considerado normal')
else:
    print('Peso acima ou abaixo do normal')
