# App-DogWalker

Video da aplicação no youtube: https://youtu.be/6M3FCOp3Ihs

Preparando a máquina para rodar a aplicação:

1°) Realizar o download do WampServer: https://www.wampserver.com/en/download-wampserver-64bits/  

2°) Ao clonar o repositório entre na pasta venv e verifique se o arquivo pyvenv.cfg está com os dados do python referentes a sua máquina. Caso não esteja, é essencial que você altere para conseguir rodar os comandos a seguir.  

3°) Entre na pasta App-DogWalker/venv/Scripts e digite "activate". Após isso volte para a raiz do projeto.  

4°) Com o WampServer ligado, acesse o banco http://localhost/phpmyadmin 

Para entrar no banco use: 

  Utilizador: root 
  
  Escolha de servidor: MySQL

Crie um banco de dados com os seguintes dados:

  Nome: dogwalker  
  Tipo: utf8_general_ci
  
Após esse processo, temos que instalar o mysql no projeto. Deixamos na raiz o arquivo mysqlclient-2.1.1-cp311-cp311-win_amd64.whl, ele é referente a versão 3.11 do python e versão operacional x64. Caso esse não seja seu caso segue o link para todas as versões disponiveis: https://archive.linux.duke.edu/pypi/simple/mysqlclient/

Você deve baixar o app na raiz do projeto e rodar o seguinte comando:   

- pip install mysqlclient-2.1.1-cp311-cp311-win_amd64.whl 

Lembrando que caso você tenha baixado outra versão você deve deixar apenas a que vai utilizar na raiz do projeto e copiar o nome dela para rodar no comando pip install.

Execute o comando python manage.py migrate para levar as tabelas para o banco de dados. 

Após a migração das tabelas você conseguirá entrar no servidor com o comando: python manage.py runserver.




