nome = input('Qual o seu nome?')
idade = input('Qual a sua idade?')

idade = int(idade) #cascatate - convertendo idade stf para int

idade_menor = 18
idade_maior = 50

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} Pode pegar o empréstimo.')
else:
    print(f'{nome}Não pode pegar o empréstimo.')