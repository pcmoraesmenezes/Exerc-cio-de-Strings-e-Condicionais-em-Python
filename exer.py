"""
Pedir ao usuario um nome de entrada
Pedir ao usuario uma idade
Se nome e idade forem digitados faça:
    Seu nome é: (nome)
    Seu nome invertido é(nome invertido)
    Se nome contem ou não espaço
    Seu nome tem n letras
    A primeira letra do seu nome é()
    A ultima letra do seu nome é ()
Senão digite "Desculpa você não informou os campos
"""
nome = input("Digite o seu nome para iniciarmos ")
idade = int(input("Digite a sua idade agora "))
invert = len(nome)
if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if '' in nome:
        print("Seu nome contém espaços")
    else:
        print("Seu nome não contém espaços")
    print(f'Seu nome tem',len(nome),'letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
else:
    print("Você não informou os campos necessarios!")
    