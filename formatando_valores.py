from this import d


class formatando_valores:
    def formatando_os_valroes():
        # :s - Texto (Strings)
        # :d - Intereiros (Int)
        # :f - Números de ponto flutuante (float)
        # . (Número)f - Quantidade de casas decimais (float) :.10f
        # : (caratere)(> ou < ^)(quantidade )(tipo - s,d, ou f)#
        
        
        # > - Esquerda
        # < - Direita   
        # ^ - Centro
        
        num1 = 1
        print (f'{num1:0>10}') 
        num2 = 1150
        print(f'{num2:0<10}')
        num3 = 1150
        print(f'{num3:.2f}')
        nome = "Johao Marcelo"
        print((50 - len (nome))/2)
        print(f'{nome:#^50}')
        