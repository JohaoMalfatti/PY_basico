class string_while_iterando:
    def while_srting_iterando():
        frase = 'O Rato roeu a roupa do rei de roma'
        tamanho_frase = len(frase)
        contador = 0
        nova_string = ''
        
        letra_maiuscula = input('Qual letra deseja deixar maiuscula?')
        
        while contador < tamanho_frase:
            letra = frase[contador] #faz o check de letra na frase
            if letra == letra_maiuscula: #vai validar a letra que o user digitou
                nova_string += letra_maiuscula.upper() #deixa letra que o user digitou maiuscula
            else:
                    nova_string += letra
            contador +=1
        print(nova_string)
        