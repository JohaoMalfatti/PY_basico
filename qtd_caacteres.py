usuario = input('Digite seu usuário:')
qtd_caracteres = len(usuario)

if qtd_caracteres <6:
    print('Voce precisa digitar no minimo 6 caracteres.')
else:
    print('Voce foi cadastrado no sistema.')