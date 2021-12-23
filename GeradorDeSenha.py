import pyperclip as clip
from random import randint as rand

def verificar_primo(numero):
    contador = 0
    for x in range(1, numero + 1):
        if numero % x == 0:
            contador += 1
    if contador == 2:
        return True
    else:
        return False

def gerar_senha(quantidade_caracteres):
    senha = []
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for x in range(0, quantidade_caracteres):
        cont = 0
        if '.' not in senha:
            if verificar_primo(rand(0, 100)):
                senha.append('.')
                cont += 1

        if cont == 0:
            if rand(0, 1) == 0:
                if rand(0, 1) == 0:
                    senha.append(alfabeto[rand(0, 25)])
                else:
                    senha.append(alfabeto[rand(0, 25)].upper())
            else:
                senha.append(str(rand(0, 9)))

    senha = ''.join(senha)
    return senha

email = input('Informe o email que vai usar com a senha: ')
site = input('Informe o site que vai usar a senha: ')
quant = int(input('Informe a quantidade de caracteres que deseja que a senha tenha: '))
nova_senha = gerar_senha(quant)
clip.copy(nova_senha)
arquivo = open('Senhas.txt', 'a')
arquivo.write(f'Email: {email} \n')
arquivo.write(f'Site:  {site}\n')
arquivo.write(f'Senha: {nova_senha}\n\n')
arquivo.close()
print(f'A senha gerada foi {nova_senha}: {len(nova_senha)}')
print('Ela foi copiada para a sua área de transferência e adicionada ao '\
    'arquivo de senhas')