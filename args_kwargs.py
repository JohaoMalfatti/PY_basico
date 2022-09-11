class argumentos_chave_argumentos:
    def func(*args, **kwargs):
        print(args)
        print(kwargs)
        
        idade = kwargs.get('idade')
        
        if idade is not None:
            print (idade)
        else:
            print('Idade não existe')    
        
    lista = [1,2,3,4,5] #desepacotando lista1 da tupla
    lista2 = [10,20,30,40,50]#desempacotando lista2 da tupla
    func(*lista, *lista2, nome = 'Johao', sobrenome= 'Malfatti', idade= 30)