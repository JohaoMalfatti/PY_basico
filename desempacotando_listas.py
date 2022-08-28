class desempacotando:
    def desempacotando_lystas_py():
        lista = ['Johao', 'Luiz','William','Maria',1,2,3,4,5,6]
        outra_lista=[]
        
        n1, n2, n3, *outra_lista = lista # o simbolo *vai colocar tudo o que for além dos 3 dados na outra lista (*= sobra)
        print(n2)
        *outra_lista, n1, n2, n3 = lista 
        print(outra_lista) #vai imprimir até o numero 3, 456 só imprime se passar os n1,n2,n3 no prin
        
        