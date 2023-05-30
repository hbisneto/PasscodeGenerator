## WindowsApp File
## This file is used to implement code used to run scripts for Windows

from exception import Exceptions
from windows import FileSystem
from random import sample
from pyperclip import copy

def gerar_senha(quant_caracteres):
   alfa_minusculo = 'abcdefghijklmnopqrstuvwxyz'
   alfa_maiusculo = alfa_minusculo.upper()
   numeros = '0123456789'
   simbolos = '!@#$%&'
   caracteres_senha = alfa_minusculo + alfa_maiusculo + numeros + simbolos
   senha = ''.join(sample(caracteres_senha, quant_caracteres))
   return senha

def main():
   email = input('Informe o email que vai usar com a senha: ')
   site = input('Informe o site que vai usar a senha: ')
   quant = int(input('Informe a quantidade de caracteres que deseja: '))
   nova_senha = gerar_senha(quant)
   copy(nova_senha)

   with open(FileSystem.PASSCODE_FILE, 'a') as arquivo:
      dados = f'Email: {email} \nSite: {site} \nSenha: {nova_senha}\n\n'
      arquivo.write(dados)
      arquivo.close()
   print(f'A senha gerada foi {nova_senha}: {len(nova_senha)}')
   print('Ela foi copiada para a sua área de transferência e adicionada ao arquivo de senhas')

main()