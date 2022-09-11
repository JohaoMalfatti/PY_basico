class exec_contadores:
    def exercicios_de_contadores():          
########################################################
#        x = 0 #coluna
#        while x < 8:
#            y = 10 #linha
#            while y >1:
#               print(f' X vale {x} e Y vale {y}')
#                y -= 1
#                x+=1
#        print('Acabou!')
#minha logica comentada 

#logica do professor
        for c, r in enumerate(range(10,1,-1)):
            print(c,r)