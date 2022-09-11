
def mestre(funcao, *args, **kwargs): #funcao mestre que recebe a func1 e func2
    return funcao(*args, **kwargs)
#precisa ser usado o args e kwargs para pasar poder torar os valores
def func1_olá(nome):
    return f'Olá {nome}'
    
def func2_saudacao(nome,saudacao):
    return f'{saudacao} {nome}'

executando = mestre(func1_olá,'Johao') #passa par a func mestre a func1 
executando2 = mestre(func2_saudacao, 'Johao', saudacao= 'Bom dia') #passa par a func mestre afunc2
print(executando)
print(executando2)