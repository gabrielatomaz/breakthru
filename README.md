## Breakthru - Fundamentos de Inteligência Artificial

### :rocket: Guia de execução

Para executar esse projeto, é necessário que você tenha o python3 instalado na sua máquina.

Primeiro verifique se o python já está instalado. Os sistemas GNU/Linux mais recentes ja possuem uma versão do Python instalada junto com o sistema operacional.

```
$ which python3
```

Se não estiver instalado, instale usando o gerenciador de pacote de distribuição

Antes de tudo, atualize o seu índice de pacotes locais

```
$ sudo apt update
```

Depois instale o Python3 na versão de sua preferência

```
$ sudo apt-get install python<3.x>
```

Para verificar se a instalação foi realizada corretamente, execute novamente

```
$ python3 --version
```

Agora precisamos instalar as dependências do projeto, você precisa ter o gerenciador de pacotes pip instalado. Caso não tenha, instale utilizando o seguinte comando

```
$ sudo apt-get install python-pip
```

Para verificar a instalação corretamente

```
$ pip --version
```

Para instalar as dependência do projeto, utilize

```
$ pip install -r requirements.txt
```

### :computer: Projeto - Jogo de Damas
