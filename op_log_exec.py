usuario = input ('Nome do Usúario:')
senha = input ('Senha do Usúario:')

usuario_bd = 'Johao'
senha_bd = '123'

if usuario_bd ==usuario  and senha_bd == senha:
    print('Voce está logado no sistema!')
else:
    print('Login Inválido')