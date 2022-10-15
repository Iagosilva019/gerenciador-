
from docs.CLASSES.colors import Cores
from random import choice
from time import sleep
import os
import abc

C = Cores()


def clear():
      if os == 'nt':
        os.system('cls')
      else:
        os.system('clear')

class Login():
    
    def __init__(self,senha):
        self._senha = senha
    
    
    def alterar(self, senha):
        with open('docs/TXT/senha.txt','w') as senha:
          senha.write(self._senha)
          
        senha.close()
  
    def entrar(self, password):
        with open('docs/TXT/senha.txt','r') as senha:
           if password not in senha:
               print('senha incorreta')
               sleep(2.0)
               clear()
               exit()
           else:
              print(f'{C.code_info}{choice(C.listColor)}Entrando no gerenciador...')
        senha.close() 
        
        

