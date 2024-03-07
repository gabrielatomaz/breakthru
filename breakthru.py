import pygame
import pygame_gui
import sys
from pygame.locals import *
import copy

def main():
    # Inicialização do Pygame
    pygame.init()
    screen = pygame.display.set_mode((560, 700))  # Ajustando a altura da tela para acomodar a nova pergunta
    pygame.display.set_caption("Checkers Game")
    manager = pygame_gui.UIManager((560, 700))  # Ajustando a altura do manager também
    clock = pygame.time.Clock()
    is_running = True

    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((200, 180), (150, 100)),
                                            text='Quem irá iniciar?', manager=manager)
    # Adicionando botões para escolha do jogador humano
    silver_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((80, 250), (150, 50)),
                                                  text='Cinza', manager=manager)
    gold_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((330, 250), (150, 50)),
                                                text='Dourado', manager=manager)

    # Adicionando pergunta para escolha do jogador da IA
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((200, 300), (150, 50)),
                                            text='Quem será a IA?', manager=manager)
    ai_silver_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((80, 340), (150, 50)),
                                                     text='Cinza', manager=manager)
    ai_gold_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((330, 340), (150, 50)),
                                                   text='Dourado', manager=manager)

    player = None
    ai_player = None

    while is_running:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == QUIT:
                is_running = False
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == silver_button:
                        player = 'S'
                    elif event.ui_element == gold_button:
                        player = 'G'
                    elif event.ui_element == ai_silver_button:
                        ai_player = 'S'
                    elif event.ui_element == ai_gold_button:
                        ai_player = 'G'
                    if player is not None and ai_player is not None:
                        is_running = False
            manager.process_events(event)

        manager.update(time_delta)

        screen.fill((255, 255, 255))
        manager.draw_ui(screen)
        pygame.display.flip()

    if player is not None and ai_player is not None:
        start_game(player, ai_player)
    pygame.quit()
    sys.exit()


def start_game(player, ai_player):
    pygame.init()
    screen = pygame.display.set_mode((560, 650))
    pygame.display.set_caption("Checkers Game")
    clock = pygame.time.Clock()

    # Definindo cores
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    SILVER = (192, 192, 192)
    DARK_GRAY = (100, 100, 100)
    GOLD = (255, 215, 0)
    DARK_GOLD = (184, 134, 11)

    # Definindo tamanho da tela e do quadrado do tabuleiro
    SCREEN_WIDTH = 560
    SCREEN_HEIGHT = 650
    SQUARE_SIZE = SCREEN_WIDTH // 7

    # Definindo a fonte para o texto
    font = pygame.font.Font(None, 36)

    # Função para desenhar o tabuleiro
    def draw_board(screen, board):
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), 5)
        for row in range(7):
            for col in range(7):
                if (row + col) % 2 == 0:
                    pygame.draw.rect(screen, DARK_GRAY,
                                     (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                else:
                    pygame.draw.rect(screen, WHITE,
                                     (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                pygame.draw.rect(screen, BLACK, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
                                 1)
                if board[row][col] == "S":
                    pygame.draw.circle(screen, SILVER,
                                       (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2),
                                       SQUARE_SIZE // 3)
                elif board[row][col] == "G":
                    pygame.draw.circle(screen, GOLD,
                                       (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2),
                                       SQUARE_SIZE // 3)
                elif board[row][col] == "X":
                    pygame.draw.circle(screen, DARK_GOLD,
                                       (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2),
                                       SQUARE_SIZE // 3)
                    pygame.draw.rect(screen, GOLD, (
                        col * SQUARE_SIZE + SQUARE_SIZE // 3, row * SQUARE_SIZE + SQUARE_SIZE // 3,
                        SQUARE_SIZE // 3, SQUARE_SIZE // 3))
                    pygame.draw.rect(screen, BLACK, (
                        col * SQUARE_SIZE + SQUARE_SIZE // 3, row * SQUARE_SIZE + SQUARE_SIZE // 3,
                        SQUARE_SIZE // 3, SQUARE_SIZE // 6), 1)
                    pygame.draw.polygon(screen, BLACK,
                                        [(col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 3),
                                         (col * SQUARE_SIZE + SQUARE_SIZE // 3, row * SQUARE_SIZE + SQUARE_SIZE // 2),
                                         (col * SQUARE_SIZE + 2 * SQUARE_SIZE // 3, row * SQUARE_SIZE + SQUARE_SIZE // 2)])

    def move_piece(board, piece, from_row, from_col, to_row, to_col):
        if board[from_row][from_col] != piece:
            #print("Movimento inválido: Não há nenhuma peça para mover na posição especificada.")
            return board, False

        possible_moves = get_moves(board, from_row, from_col, piece)
        #print(f"Peça {piece} ({from_row + 1}, {from_col + 1}) movimentos ({possible_moves})")

        if (to_row, to_col) not in possible_moves:
            #print("Movimento inválido: O movimento especificado não é permitido para a peça selecionada.")
            return board, False

        if abs(to_row - from_row) > 1 or abs(to_col - from_col) > 1:
            #print("Movimento inválido: a peça só pode mover uma casa de cada vez.")
            return board, False

        board[to_row][to_col] = piece
        board[from_row][from_col] = '-'
        #print(f"Peça {piece} movida da posição ({from_row + 1}, {from_col + 1}) para ({to_row + 1}, {to_col + 1})")
        return board, True

    # Função para obter os movimentos possíveis para uma peça
    def get_moves(board, row, col, piece):
        moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        diagonal_directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

        if piece == "X":
            # Movimentos para frente, trás e para os lados (apenas uma casa)
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == "-":
                    moves.append((r, c))
            # Movimentos de "roubo" de posição nas diagonais
            for dr, dc in diagonal_directions:
                r, c = row + dr, col + dc
                if 0 <= r < len(board) and 0 <= c < len(board[0]):
                    if (board[r][c] == 'S'):
                        moves.append((r, c))
        else:
            # Movimentos para frente, trás e para os lados
            for dr, dc in directions:
                r, c = row + dr, col + dc
                while 0 <= r < len(board) and 0 <= c < len(board[0]):
                    if board[r][c] == "-":
                        moves.append((r, c))
                    else:
                        break
                    r += dr
                    c += dc

            # Movimentos de "roubo" de posição nas diagonais
            for dr, dc in diagonal_directions:
                r, c = row + dr, col + dc
                if 0 <= r < len(board) and 0 <= c < len(board[0]):
                    if (piece == "S" and board[r][c] == "G") or (piece == 'G' and board[r][c] == 'S'):
                        moves.append((r, c))

        return moves

    def check_victory(board, piece):
        if piece == 'S':
            for row in board:
                if "X" in row:
                    return False
            return True
        elif piece == 'X':
            perimeter_coordinates = [(1, col) for col in range(1, 8)] + \
                                    [(7, col) for col in range(1, 8)] + \
                                    [(row, 1) for row in range(2, 7)] + \
                                    [(row, 7) for row in range(2, 7)]
            x_row, x_col = None, None
            for row_idx, row in enumerate(board):
                if 'X' in row:
                    x_row, x_col = row_idx + 1, row.index('X') + 1
                    break
            if (x_row, x_col) in perimeter_coordinates:
                return True
            else:
                return False
        for row in board:
            if "S" in row:
                return False
        return True


    def evaluate(board, player):
        silver_count = sum(row.count('S') for row in board)
        gold_count = sum(row.count('G') for row in board)

        if player == 'S':
            return silver_count - gold_count
        else:
            return gold_count - silver_count

    def minimax(board, depth, player):
        if depth == 0 or check_victory(board, 'S') or check_victory(board, 'G'):
            evaluation = evaluate(board, player)
            return evaluation, None

        if player == 'S':
            max_eval = float('-inf')
            best_move = None
            for row in range(7):
                for col in range(7):
                    if board[row][col] == 'S':
                        piece_moves = get_moves(board, row, col, 'S')
                        for move in piece_moves:
                            new_board = copy.deepcopy(board)
                            new_board, was_moved = move_piece(new_board, 'S', row, col, move[0], move[1])
                            eval, _ = minimax(new_board, depth - 1, 'G')
                            if eval > max_eval:
                                max_eval = eval
                                best_move = (row, col, move[0], move[1])
            return max_eval, best_move
        else:
            min_eval = float('inf')
            best_move = None
            for row in range(7):
                for col in range(7):
                    if board[row][col] == 'G':
                        piece_moves = get_moves(board, row, col, 'G')
                        for move in piece_moves:
                            new_board = copy.deepcopy(board)
                            new_board, was_moved = move_piece(new_board, 'G', row, col, move[0], move[1])
                            eval, _ = minimax(new_board, depth - 1, 'S')
                            if eval < min_eval:
                                min_eval = eval
                                best_move = (row, col, move[0], move[1])
            return min_eval, best_move


    def move_ai(board, ai_player):
        new_board = copy.deepcopy(board)
        _, best_move = minimax(new_board, 3, ai_player)  # Aumentar o horizonte de busca
        if best_move:
            from_row, from_col, to_row, to_col = best_move
            piece = new_board[from_row][from_col]
            # Verifica se a peça é do jogador 'G' ou 'X' antes de fazer o movimento
            move_piece(new_board, piece, from_row, from_col, to_row, to_col)
        return new_board



    # Função principal do jogo
    rows = 7
    cols = 7
    board = [["-" for _ in range(cols)] for _ in range(rows)]
    board[0][2:5] = ["S"] * 3
    board[2][0] = "S"
    board[2][6] = "S"
    board[2][2:5] = ["G"] * 3
    board[3][0] = "S"
    board[3][6] = "S"
    board[3][2] = "G"
    board[3][4] = "G"
    board[3][3] = "X"
    board[4][0] = "S"
    board[4][6] = "S"
    board[4][2:5] = ["G"] * 3
    board[6][2:5] = ["S"] * 3

    from_row, from_col = None, None
    current_player = player  # Define o jogador atual como o jogador escolhido pelo usuário
    while True:
        draw_board(screen, board)
        if check_victory(board, "G"):
            font = pygame.font.Font(None, 36)
            text = font.render('Jogador G ganhou!', True, BLACK)
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 600))
            screen.blit(text, text_rect)
            pygame.display.flip()
            pygame.time.delay(3000)
            pygame.quit()
            sys.exit()

        # Verificar se é a vez do jogador humano ou da IA e atualizar o texto
        if current_player != 'X' and current_player != 'G':
            turn_text = font.render("Vez do jogador: " + current_player, True, BLACK)
            turn_text_rect = turn_text.get_rect(center=(SCREEN_WIDTH // 2, 600))
            screen.blit(turn_text, turn_text_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                clicked_row = mouse_y // SQUARE_SIZE
                clicked_col = mouse_x // SQUARE_SIZE
                if from_row is None and from_col is None:
                    if (current_player == "S" and board[clicked_row][clicked_col] == "S") or (
                            current_player == "G" and board[clicked_row][clicked_col] == "G"):
                        from_row, from_col = clicked_row, clicked_col
                    elif current_player == "G" and board[clicked_row][clicked_col] == "X":
                        from_row, from_col = clicked_row, clicked_col
                        current_player = "X"
                else:
                    to_row, to_col = clicked_row, clicked_col
                    new_board, was_moved = move_piece(board, current_player, from_row, from_col, to_row, to_col)
                    if was_moved:
                        #print(f"Peça {current_player} movida da posição ({from_row + 1}, {from_col + 1}) para ({to_row + 1}, {to_col + 1})")
                        draw_board(screen, board)
                        pygame.display.flip()
                        if check_victory(board, current_player):
                            if current_player == 'X':
                                message = 'Jogador G ganhou!'
                            else:
                                message = f'Jogador {current_player} ganhou!'
                            font = pygame.font.Font(None, 36)
                            text = font.render(message, True, BLACK)
                            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 600))
                            screen.blit(text, text_rect)
                            pygame.display.flip()
                            pygame.time.delay(3000)
                            pygame.quit()
                            sys.exit()

                        if current_player == "S":
                            current_player = "G"
                        elif current_player == "G":
                            current_player = "S"
                        else:
                            current_player = "S"
                    else:
                        if current_player == "X":
                            current_player = "G"

                    from_row, from_col = None, None


        if current_player == 'X' or current_player == ai_player:
            print(ai_player)
            turn_text = font.render("Vez do jogador: " + ai_player, True, BLACK)
            turn_text_rect = turn_text.get_rect(center=(SCREEN_WIDTH // 2, 600))
            screen.blit(turn_text, turn_text_rect)
            pygame.display.flip()

            board = move_ai(board, ai_player)
            if (current_player == 'S'):
                current_player = 'G'
            else:
                current_player = 'S'
            print(current_player)



        clock.tick(60)

main()