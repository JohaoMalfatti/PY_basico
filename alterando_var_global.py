#variavel = 'valor1'
#    
#def func1(): 
#    print(variavel)
#    
#def func2():
#    global variavel
#    variavel = 'Outro Valor'
#    print(variavel)    
#func1()
#func2()
#print(variavel)              

def func():
    outra_variavel = 'Luiz Otávio'
    return outra_variavel
def func2(arg):
    print(arg)
var = func()
func2(var)
#boas pratias, não uso uma var glogal e sim um em cada funcão e depois migro os valores
#entre as funcoes. 