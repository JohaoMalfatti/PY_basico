#Operadores Lógicos 
#and, or , no , in e not in

a= 2
b=3

if not b > a :
    print ('B é mario que A.')
else:
    print ('A é maior que B.')
    
    #################################
    
    nome = 'Johao Marcelo'
    if'a' in nome: #valida se existe no texto 
        print("Existe a letra A em seu nome.")
    else:
        print("Não existe.")
        
    if'aasdas' not in nome: #valida se não existe no texto 
        print("Não Existe nome.")
    else:
        print("Existe.")