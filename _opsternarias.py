class operadores_ternarios:
    def ternarios_operadores():
        idade = input('Digite sua idade')
        if not idade.isnumeric(): #validando se digitou somente números inteiros
            print('Digite apenas números inteiros')    
        else:
            idade = int (idade) #convertando str em inteiro 
            de_maior =(idade>=18)
            msg = 'Pode Acessar' if de_maior else 'Não pode Acessar'
            print(msg)