from this import d


class exemplos_listas:
    
    def exemplos_de_listas():
        lista = [
            # 0        1         2
            ['Edu',  'Johao', 'Luiz'], #0
            ['Maria', 'Alie',  'Joana'],#1
            ['Helena', 'ED',    'LU'],#2
        ]
        print(lista[1][2]) #vai imprimir joana
        enumerada = enumerate(lista)
        print(enumerada)