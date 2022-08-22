class calculadora_basica_while:
    def calc_basic_while1():
        while True: 
            print()
            sair = input ('Deseja Continuar (S) Sim (N) Não')
            if sair == 'n':
                break     
            num_1 = input('Digite um número')
            num_2 = input ('Digite outro número')
            operador = input ('Digite a operação')
        
            if not num_1.isnumeric() or not num_2.isnumeric():
                print('Voce precisa digitar um número')
                continue
        
            num_1= float(num_1)
            num_2 = float(num_2)
        
        
        
            if operador == '+':
                print (num_1 + num_2)
            elif operador == '-':
                print (num_1 - num_2)
            elif operador == '*':
                print (num_1 * num_2)
            elif operador == '/':
                print (num_1 / num_2)
            else:
                print('Operador Invalido')
                
        