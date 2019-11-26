# Meu Carona

Sistema desenvolvido para a disciplina Projeto e Desenvolvimento de Software do DCA na UFRN.

## Instalação

### Adicionando bibliotecas necessárias do Python

O pip é um instalador de bibliotecas Python, é muito útil para instalar as dependências do seu projeto, instale executando o comando abaixo.

```sh
sudo apt install python-pip
```

Outra ferramenta muito útil é o virtualenvwrapper, usado para criar ambientes que vão lhe ajudar quando estiver trabalhando com projetos que utilizam diferentes versões da mesma biblioteca.

```sh
sudo pip install virtualenvwrapper
```

Agora é necessário realizar algumas configurações para que o virtualenvwrapper funcione corretamente, crie um novo diretório em sua home. Ele será usado para guardar os ambientes criados.

```sh
mkdir ~/.virtualenvs
```

Abra seu arquivo ~/.bashrc.

```sh
gedit ~/.bashrc
```

Adicione as linhas abaixo no final do arquivo que foi aberto com o comando anterior.

```sh
export WORKON_HOME=~/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
```

Por último atualize o terminal.

```sh
exec bash
```

### Utilização da virtualenv

Para criar uma nova virtualenv, execute o comando abaixo.

```sh
mkvirtualenv <nome da virtualenv>
```

### Instalando os requirements

Após instalar o pip e deixar sua virtualenv ativa, precisamos instalar os requirements. 

```sh
cd caronas
```

```sh
pip install -r requirements.txt
```

### Colocando para Rodar

Agora para iniciarmos a aplicação, voltamos para a pasta principal do projeto, precisamos dar um run nas nossas migrações e rodar o servidor.

```sh
cd ..
python manage.py migrate
python manage.py runserver
```

## O Sistema

O Sistema serve para cadastrar e procurar caronas ao longo de uma rota ou de pontos numa determinada região.
O usuário pode realizar cadastro tanto como passageiro (desejando solicitar carona) quanto motorista (desejando oferecer carona).

## Implementação e Ferramenta

O Sistema foi desenvolvido utilizando o framework Django feito em Python, voltado para aplicaçoes Web. 
Utiliza como SGBD o SQLite3 e o Mapeamento Objeto-Relacional (ORM) do Django. Além de utilizar sessões, forms e outros utilitários do framework.

## Funcionamento e Fluxo

Inicialmente o usuário irá fazer um cadastro no sistema, podendo optar por ser Motorista, Passageiro ou ambos. Apos preencher o
formulario ja possui sua conta para fazer login no sistema.

Ao realizar login no sistema, caso o usuário tenha optado por ter ambos os perfis, tanto de motorista quanto de passageiro, terá qe optar
por qual deseja prosseguir na sessão. Caso seja motorista, poderá ofertar uma carona indicando os pontos e a sua rota ao longo do trajeto.
Caso seja passageiro, pode solicitar uma carona também ao longo do trajeto ou da rota.
