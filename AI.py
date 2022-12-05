# This is the AI opponent againt a player in connect 4

import random
import GameEngine

def random_move(possible_moves):
    return possible_moves[random.randint(0, len(possible_moves) - 1)]

def depth_3(board, possible_moves, turn):
    best_move = None
    print(possible_moves)
    for move in possible_moves:    
        game = GameEngine.Board(no_render=True, board=board)
        game.make_move(move)
        board2 = game.board
        winner = game.check_for_winner(move)
        if winner == turn:
            best_move = move
            break
        possible_moves2 = game.get_possible_columns()
        for move2 in possible_moves2:
            game = GameEngine.Board(no_render=True, board=board2)
            game.make_move(move2)
            board3 = game.board
            winner = game.check_for_winner(move2)
            if winner == turn:
                best_move = move
                break
            possible_moves3 = game.get_possible_columns()
            for move3 in possible_moves3:
                game = GameEngine.Board(no_render=True, board=board3)
                game.make_move(move3)
                winner = game.check_for_winner(move3)
                if winner == turn:
                    best_move = move
                    break
    if best_move is None:
        return possible_moves[possible_moves.sample()]

def depth_5(board, possible_moves, turn):
    game = GameEngine.Board(no_render=True)
    best_move = None
    for move in possible_moves:
        game.make_move(move)
        winner = game.check_for_winner(move)
        if winner == turn:
            best_move = move
            break
        possible_moves2 = game.get_possible_columns()
        for move2 in possible_moves2:
            game.make_move(move2)
            winner = game.check_for_winner(move2)
            if winner == turn:
                best_move = move
                break
            possible_moves3 = game.get_possible_columns()
            for move3 in possible_moves3:
                game.make_move(move3)
                winner = game.check_for_winner(move3)
                if winner == turn:
                    best_move = move
                    break
                possible_moves4 = game.get_possible_columns()
                for move4 in possible_moves4:
                    game.make_move(move4)
                    winner = game.check_for_winner(move4)
                    if winner == turn:
                        best_move = move
                        break
                    possible_moves5 = game.get_possible_columns()
                    for move5 in possible_moves5:
                        game.make_move(move5)
                        winner = game.check_for_winner(move5)
                        if winner == turn:
                            best_move = move
                            break
    if best_move is None:
        return possible_moves[possible_moves.sample()]