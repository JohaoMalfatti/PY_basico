class valida_tamanho_nome:
    def valida_o_tamanho_do_nome():

        usuario = input('Digite seu usuário:')
        qtd_caracteres = len(usuario)

        if qtd_caracteres <=4:
            print('Seu nome é muito curto')
        elif qtd_caracteres <=6:
            print('Seu nome é normal')
        else:
            print('Seu nome é muito grande')