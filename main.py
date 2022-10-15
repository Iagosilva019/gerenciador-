#Toolname   : Gerenciador
#Author     : Iago-Linux
#Version    : 1.0
#License    : ....
#Copyright  : ....
#Github     : https://github.com/Iagosilva019
#Contact    : iagosilvasantana21@gmail.com
#Descriptin : Gerenciador de sites/senhas em python
#Tags       : Incluir, Buscar , Remover , Listar, Gdrive, etc ...
#1st Commit : 15/10/2022
#Language   : Python
#Portable   : file/script





import abc
import os
import sys


 #--------------------------------------------------------------
def sprint(n):
      for word in n + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        sleep(0.01)

def clear():
      if os == 'nt':
        os.system('cls')
      else:
        os.system('clear')
 #--------------------------------------------------------------



class Gerenciador(abc.ABC):
    
    __slots__ = ['_site','_email','_senha','_url','_gerenciador', '_sites']

    def __init__(self,site,email,senha, url):
        self._site = site
        self._email = email
        self._senha = senha
        self._url = url
        self._gerenciador = []
        self._sites = []
    
    @property
    def GET_site(self):
      return self._site
    @GET_site.setter
    def SET_site(self, site):
        self._site = site
        
    @property
    def GET_email(self):
      return self._email
    @GET_email.setter
    def SET_email(self, email):
        self._email = email
    
    @property
    def GET_senha(self):
      return self._senha
    @GET_senha.setter
    def SET_senha(self, senha):
        self._senha = senha
        
    @property
    def GET_url(self):
      return self._url
    @GET_url.setter
    def SET_url(self, url):
        self._url = url
        
  
    #--------------------------------------------------------------
    def Incluir(self):
        with open("docs/TXT/dados.txt", "a") as arquivo: #abertura o arquivo
         self._gerenciador = [f'Site:{self._site} | Email:{self._email} | Senha:{self._senha} | Url:{self._url}\n']
         arquivo.writelines(self._gerenciador)
         print('\nInformações foram salvas com sucesso!')
        arquivo.close() #fechamento de um arquivo
    
         #Sites
        with open("docs/TXT/sites.txt", "a") as sites: #abertura o arquivo
          self._sites = [f'{self._site}\n']
          sites.writelines(self._sites)
        sites.close() #fechamento de um arquivo
        
        
    #-------------------------------------------------------------
    def buscar(self, site):
        with open("docs/TXT/dados.txt", "r") as arquivo: #abertura o arquivo
          dados = arquivo.readlines()
          for linha in dados:
            if site in linha:
                print('\n',linha, '\n')
        arquivo.close() #fechamento de um arquivo


    #-------------------------------------------------------------
    def Remover(self, remov):
        try:
           os.system(f'cat docs/TXT/dados.txt | grep -v {remov} > excluido && mv excluido  docs/TXT/dados.txt')
           os.system(f'cat docs/TXT/sites.txt | grep -v {remov} > excluido2 && mv excluido2  docs/TXT/sites.txt')
           print(f'{remov} removido')
        except:
           print("Oops! error")


    #-------------------------------------------------------------
    def listar(self):
        with open("docs/TXT/dados.txt", "r") as arquivo: #abertura o arquivo
            lista = arquivo.read()
            print('\n',lista)
        arquivo.close() #fechamento de um arquivo

     #-------------------------------------------------------------
     
    def gdrive(self , OP):
          if OP == '1':
            os.system('cat docs/TXT/dados.txt > docs/TXT/gdrive/dados.txt')
            print('Backup salvo no google drive')
          elif OP == '2':
            sprint('---------------------Instale as dependencias-------------------')
            print('[+] O repositorio do gdrive e a montagem')
            print('[+] primeiro adicione o repositorio e depois o faça a montagem')
            os.system("bash drive.sh")
            sleep(2.0)
            exit()
            
    #-------------------------------------------------------------
    @abc.abstractmethod
    def abrir_local(self):
      pass
    
    @abc.abstractmethod
    def permissao(self, tipo):
      pass
         
    @abc.abstractmethod
    def backuplocal(self):
        pass
         
         
class Metodos_Abstratos(Gerenciador):
      def backuplocal(self):
        os.system('cat docs/TXT/dados.txt > docs/TXT/backup.txt') 
  
      def abrir_local(self):
        os.system('open docs/TXT/')

      def permissao(self, tipo):
        if tipo == '1':
          os.system('chmod 700 docs/TXT')
          print('permitido')
        elif tipo == '2':
          os.system('chmod 300 docs/TXT')
          print('não permitido')



#main-------------------------------------------------------------------------------



if __name__ == "__main__":
    from random import choice
    from time import sleep

    from docs.CLASSES.colors import Cores
    from docs.CLASSES.Login import Login
    GE =  Metodos_Abstratos('','','','')
    L  = Login('')
    C  = Cores()
    
#-------------------------------------------------------------

    logo = f'''{choice(C.listColor)}╭━━━╮╭━━━╮╭━━━╮╭━━━╮╭━╮╱╭╮╭━━━╮╭━━╮╭━━━╮╭━━━╮╭━━━╮╭━━━╮
{choice(C.listColor)}┃╭━╮┃┃╭━━╯┃╭━╮┃┃╭━━╯┃┃╰╮┃┃┃╭━╮┃╰┫┣╯┃╭━╮┃╰╮╭╮┃┃╭━╮┃┃╭━╮┃
{choice(C.listColor)}┃┃╱╰╯┃╰━━╮┃╰━╯┃┃╰━━╮┃╭╮╰╯┃┃┃╱╰╯╱┃┃╱┃┃╱┃┃╱┃┃┃┃┃┃╱┃┃┃╰━╯┃
{choice(C.listColor)}┃┃╭━╮┃╭━━╯┃╭╮╭╯┃╭━━╯┃┃╰╮┃┃┃┃╱╭╮╱┃┃╱┃╰━╯┃╱┃┃┃┃┃┃╱┃┃┃╭╮╭╯
{choice(C.listColor)}┃╰┻━┃┃╰━━╮┃┃┃╰╮┃╰━━╮┃┃╱┃┃┃┃╰━╯┃╭┫┣╮┃╭━╮┃╭╯╰╯┃┃╰━╯┃┃┃┃╰╮
{choice(C.listColor)}╰━━━╯╰━━━╯╰╯╰━╯╰━━━╯╰╯╱╰━╯╰━━━╯╰━━╯╰╯╱╰╯╰━━━╯╰━━━╯╰╯╰━╯
{choice(C.listColor)}╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱
{choice(C.listColor)}╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱
           {choice(C.listColor)}V1.0                           Iago-Linux'''

#-------------------------------------------------------------
    print('\nSenha: 0000')
    print( choice(C.listColor))
    sprint('|================================================|')
    sprint('|                  GERENCIADOR 1.0               |')
    sprint('|================================================|')
    sprint('|[1] - Alterar senha:                            |')
    sprint('|[2] - Entrar no gerenciador                     |')
    sprint(' ================================================')
#-------------------------------------------------------------

    try:    #tratamento de erros
     ss  = input(f'{C.code_result}{choice(C.listColor)}Deseja entrar ou alterar senha:{C.C} ')  
     if ss == '1':   #Alterar senha ou entrar

        with open('docs/TXT/senha.txt','r+') as senha:  #abertura o arquivo

          passs = senha.read()
          Pass1 = input(f'{C.code_result}{choice(C.listColor)}Digite sua senha antiga:{C.C} ')
          if Pass1 in passs:
            novasenha = input(f'{C.code_result}{choice(C.listColor)}Digite sua nova senha:{C.C} ')
            print(f'{C.code_info}{choice(C.listColor)}Senha alterada com sucesso')
            sleep(2.0)
            clear()
            L  = Login(novasenha)
            L.alterar()
          else:
              sprint(f'\n{C.code_error}Senha não confere')
              sleep(2.0)
              exit()
        senha.close()     #fechamento de um arquivo


     elif ss == '2':   #Entrar no Gerenciador
       senha = input(f'{C.code_result}{choice(C.listColor)}Digite sua senha:')
       L.entrar(senha)
       sleep(2.0)
       clear()
     else:
        sprint('Escolha uma opcao')
        exit()
    except:   #tratamento de erros
        print('key-force-exit or error')
        exit()
#-------------------------------------------------------------
    #menu e logo

    sprint(logo)
    print('\n[1] - Incluir no Gerenciador')
    print('[2] - Mostrar Dados no Gerenciador')
    print('[3] - Buscar no Gerenciador')
    print('[4] - Remover do Gerenciador')
    print('[5] - Salvar um backup local')
    print('[6] - Backup no google drive/Instalar depedencias')
    print('[7] - Abrir pasta dos arquivos local')
    print('[8] - Alterar permissão de acesso a pasta')
    print('[9] - sair')
    
#-------------------------------------------------------------
    #Incluir no Gerenciador

    try:  #tratamento de erros
      while True:
        op = input(f'{C.code_result}{choice(C.listColor)}O que deseja fazer:{C.C}')
        if op == '1':
          site   = input(f'\n{C.code_result}Digite o site:')
          emaill = input(f'{C.code_result}Digite o email:')
          senha  = input(f'{C.code_result}Digite a senha:')
          url    = input(f'{C.code_result}Digite a url:')
          GE     = Metodos_Abstratos(site,emaill,senha,url)
          GE.Incluir()
          
#-------------------------------------------------------------
    #Mostrar Dados no Gerenciador
        elif op == '2':
            print(choice(C.listColor))
            sprint(f'---------------------------------------------------------------------------{C.C}')
            print(choice(C.listColor))
            GE.listar()
            print(choice(C.listColor))
            sprint(f'---------------------------------------------------------------------------{C.C}')
            
#-------------------------------------------------------------
   #Buscar no Gerenciador
        elif op == '3':
            with open("docs/TXT/sites.txt", "r") as sites: #abertura o arquivo
              site = sites.read()
              print('\nSites salvos no gerenciador:')
              print('--------------------')
              print('\n',site)
              print('--------------------')
            sites.close() #fechamento de um arquivo
            siteB = input(f'{C.code_result}{choice(C.listColor)}qual site deseja ver as informações:{C.C}')
            GE.buscar(siteB)
            
#-------------------------------------------------------------
    #Remover do Gerenciador
        elif op == '4':
            with open("docs/TXT/sites.txt", "r") as sites: #abertura o arquivo
              site = sites.read()
              print('\nSites salvos no gerenciador:')
              print('--------------------')
              print('\n',site)
              print('--------------------')
            sites.close() #fechamento de um arquivo
            R = input(f'{C.code_result}{choice(C.listColor)}qual site deseja remover:{C.C}')
            GE.Remover(R)
            
#-------------------------------------------------------------
    #Fazer Backup
        elif op == '5':
            GE.backuplocal()
            print('\nBackup criado com sucesso!')
            
#-------------------------------------------------------------
        elif op == '6':
            print('1 - Fazer backup\n2 - Instalar as depedencias')
            OP = input('Escolha uma opção:')
            GE.gdrive(OP)
          
#-------------------------------------------------------------
        elif op == '7':
          GE.abrir_local()
          print('Pasta aberta')
          
#-------------------------------------------------------------
        elif op == '8':
          print('1 - Permitir acesso a pasta\n2 - não permitir acesso a pasta')
          T = input('escolha uma opção:')
          GE.permissao(T)
          
#-------------------------------------------------------------
        elif op == '9':
            print('\nSaindo...')
            sleep(2.0)
            clear()
            exit()
    except:    #tratamento de erros
        print('key-force-exit or error')
        exit()
      