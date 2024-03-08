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

## :computer: Projeto - Jogo de Damas com Algoritmo Minimax [Breakthru](<https://en.wikipedia.org/wiki/Breakthru_(board_game)>)

Esta é uma implementação em Python de um jogo de damas com o algoritmo Minimax usando Poda Alpha-Beta para tomada de decisões.

### Visão Geral

Nesta implementação, o algoritmo Minimax é utilizado para tomar decisões em um jogo de damas. Esse algoritmo é uma técnica de tomada de decisão comumente usada em jogos adversariais, como damas ou xadrez, para encontrar a jogada ótima. A poda Alpha-Beta é aplicada para otimizar o algoritmo Minimax, reduzindo o espaço de busca ao eliminar ramos que não afetam a decisão final.

### Características

- **Algoritmo Minimax**: Utiliza o algoritmo Minimax para tomar decisões ótimas em um jogo de damas.
- **Poda Alpha-Beta**: Implementa a Poda Alpha-Beta para otimizar o algoritmo Minimax, reduzindo o espaço de busca.
- **Busca Recursiva com Profundidade Limitada**: O algoritmo Minimax é implementado recursivamente com um limite de profundidade para evitar uma busca exaustiva.
- **Heurística de Avaliação**: Avalia o estado atual do tabuleiro usando uma heurística simples para estimar a vantagem de cada jogador.
- **Geração de Movimentos**: Gera todos os movimentos possíveis para uma peça de um jogador específico no tabuleiro.
- **Alternância de Jogadores**: Alterna entre turnos de maximização e minimização dos jogadores durante a busca.
- **Verificação de Condição de Vitória**: Verifica as condições de vitória para determinar o fim do jogo.
- **Interface do Usuário**: Fornece uma interface de usuário simples usando Pygame para visualização.

### Utilização

Para executar o jogo de damas com o algoritmo Minimax, é utilizada a função `main()` no script Python fornecido (breakthru.py). O jogo solicitará ao usuário que escolha o jogador inicial e o jogador da IA antes de começar.

### Discussão dos resultados

A implementação do algoritmo Minimax com Poda Alpha-Beta oferece resultados superiores em comparação com a versão sem poda, fornecendo decisões de alta qualidade em um tempo de execução mais curto. Isso torna o algoritmo mais eficiente e escalável para jogos de damas de tamanho real ou maiores.

- Minimax sem Poda Alpha-Beta:

**Eficiência Computacional:** o algoritmo minimax sem poda alpha-beta exploraria a árvore de busca completamente, o que pode resultar em um tempo de execução muito longo.
**Qualidade das Decisões:** em termos de qualidade das decisões, o minimax sem poda alpha-beta seria capaz de encontrar a jogada ótima, mas a eficiência de tempo poderia se tornar um problema.
**Escalabilidade:** a escalabilidade seria limitada devido à sua natureza exponencial, tornando o algoritmo menos prático para jogos de damas mais complexos (maiores)

- Minimax com Poda Alpha-Beta:

**Eficiência Computacional:** com a poda alpha-beta implementada, o algoritmo minimax consegue cortar os ramos da árvore de busca que não afetam a decisão final, reduzindo de forma significativa o tempo de execução em comparação com a versão sem a poda.
**Qualidade das Decisões:** a qualidade das decisões permanece alta, já que o algoritmo ainda é capaz de encontrar a jogada ótima, mas em menos tempo.
**Escalabilidade:** a escalabilidade é melhorada com a poda alpha-beta, permitindo que o algoritmo lide com jogos de damas maiores com maior eficiência do que a versão sem poda.

**Heurítiscas Uitlizadas:**
Para o jogador S, a heurística leva em consideração se aproximar de X e, caso haja alguma peça de G para capturar no caminho, ele irá capturar. Caso haja X para captura, ele deve dar uma prioriodade maior na caputra de X.
Para o jogador G, a heurística leva em consideração se há peças de S para captura, até eliminar todas. 


#### Créditos

Autoras do trabalho: Joana Mespaque e Gabriela Ribeiro
