"""nome = 'alisson'
peso = '75kg'
idade = '19 anos'

geral = (
    f'Olá {nome},'
    f' você tem {idade},'
    f' e pesa {peso}.'
)
print(geral)"""

nome = input('Qual seu nome? ')
idade = int(input('Qual sua idade?(Só os números ex: 19): '))
peso = float(input('Qual seu peso?(Digite só os números ex: 78 ex: 78.5): '))
altura = float(input('Qual sua altura?(Digite com ponto, ex: 1.75): '))
imc = peso / altura ** 2
if imc < 18.5:
    print('Olá,', nome, '! você está muito magro.')
    print('seu índice de massa corporal é', imc)
    ideal = float(input('Digite o peso que dejesa: '))
    idealc = ideal / altura ** 2
    if idealc < 18.5:
        print('Com esse peso, seu imc seria de', idealc)
        print('Seu imc precisa estar entre 18.5 e 24.9,')
    elif 18.5 >= idealc and idealc <= 24.9:
        print('Com esse peso, seu imc seria de', idealc)
        print('Peso Legal para sua altura')
    elif 25 < idealc:
        print('Seu imc precisa estar entre 18.5 e 24.9, coloque outra meta de peso!')

elif 18.5 <= imc and imc < 24.9:
    print('Olá,', nome, '! seu peso está normal.')
    print('seu índice de massa corporal é', imc)

elif 25 <= imc and imc < 29.9:
    print('Olá,', nome, '! Cuidado, você está com sobrepeso. Seu imc precisa estar entre 18.5 e 24.9.')
    print('seu índice de massa corporal é', imc)

elif 30 <= imc and imc < 34.9:
    print('Olá,', nome, '! você está com obesidade grau 1.')
    print('seu índice de massa corporal é', imc)
    ideal2 = float(input('Digite o peso que dejesa: '))
    idealc2 = ideal2 / altura ** 2
    if idealc2 < 18.5:
        print('Com esse peso, seu imc seria de', idealc2)
        print('Seu imc precisa estar entre 18.5 e 24.9, digite outra meta de peso!')
    elif idealc2 >= 18.5 and idealc2 <= 24.9:
        print('Seu imc com esse peso seria de', idealc2)
        print('Peso legal para sua altura')
    elif 25 < idealc2:
        print('Com esse peso, seu imc seria de', idealc2)
        print('Seu imc precisa estar entre 18.5 e 24.9, coloque outra meta de peso!')


elif 35 <= imc and imc < 39.9:
    print('Olá,', nome, '! você está com obesidade grau 2.')
    print('seu índice de massa corporal é', imc)
    ideal3 = float(input('Digite o peso que dejesa: '))
    idealc3 = ideal3 / altura ** 2
    if idealc3 < 18.5:
        print('Com esse peso, seu imc seria de', idealc3)
        print('Seu imc precisa estar entre 18.5 e 24.9, coloque outra meta de peso!')
    elif idealc3 >= 18.5 and idealc3 <= 24.9:
        print('Seu imc com esse peso seria de', idealc3)
        print('Peso legal para sua altura')
    elif 25 < idealc3:
        print('Com esse peso, seu imc seria de', idealc3)
        print('Seu imc precisa estar entre 18.5 e 24.9, coloque outra meta de peso!')


elif 40 < imc:
    print('Olá,', nome, '! você está com obesidade grau 3.')
    print('seu índice de massa corporal é', imc)
    ideal4 = float(input('Digite o peso que dejesa: '))
    idealc4 = ideal4 / altura ** 2
    if idealc4 < 18.5:
        print('Com esse peso, seu imc seria de', idealc4)
        print('Seu imc precisa estar entre 18.5 e 24.9, coloque outra meta de peso!')
    elif idealc4 >= 18.5 and idealc4 <= 24.9:
        print('Seu imc com esse peso seria de', idealc4)
        print('Peso legal para sua altura')
    elif 25 < idealc4:
        print('Com esse peso, seu imc seria de', idealc4)
        print('Seu imc precisa estar entre 18.5 e 24.9, coloque outra meta de peso!')

