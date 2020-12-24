from pyswip.prolog import Prolog

# Crea el Objeto Prolog
prolog = Prolog()

# Carga el PL
prolog.consult('tictactoegame.pl')


def moveHuman(player, state, board, pos):
    for move in prolog.query(f'humanMove([{player},{state},{board}],NewB,{pos})'):
        newPlayer = move['NewB'][0]
        newState = str(move['NewB'][1])
        newBoard = move['NewB'][2]

    return newPlayer, newState, newBoard


def moveMachine(player, state, board):
    for move in prolog.query(f'bestMove([{player}, {state}, {board}],NewB)'):
        newPlayer = move['NewB'][0]
        newState = str(move['NewB'][1])
        newBoard = move['NewB'][2]

    return newPlayer, newState, newBoard
