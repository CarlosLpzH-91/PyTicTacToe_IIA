import tkinter as tk
import tkinter.messagebox as mssg
import conexionProlog as pl

LARGE_FONT = ('Arial', 16)
MEDIUM_FONT = ('Arial', 15)
SMALL_FONT = ('Arial', 12)


class TicTacToe(tk.Tk):

    # Constructor
    def __init__(self, *args, **kwargs):
        # Inicialida lo que venga en args y kwars
        tk.Tk.__init__(self, *args, **kwargs)

        # Crea el frame
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Establece el orden en que se jugara. Primero jugan X
        self.order = None

        # Dict de los frames a usar
        self.frames = {}
        for F in (StartPage, BoardPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        # Inicia con StartPage
        self.show_frame(StartPage)

    # Obtener métodos de los frames
    def get_page(self, page_class):
        return self.frames[page_class]

    # Muestra el Frame
    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()

    # Inicia el el juego
    def startGame(self, desicion):
        # Crea el orden de jugadores apartir de la decisión
        # del jugador en el Frame "StartPage"
        self.order = ['human', 'machine'] if desicion == 1 else ['machine', 'human']

        # Si primero juga la máquina, ejecuta el método machineTurn
        if self.order[0] == 'machine':
            page = self.get_page(BoardPage)
            page.machineTurn()

        # Muestra el Tablero
        self.show_frame(BoardPage)


# Frame que usuario selecciona con que jugar
class StartPage(tk.Frame):
    """El jugador hace su elección"""

    # Constructor
    def __init__(self, parent, controller):
        # Inicializa la ventana
        tk.Frame.__init__(self, parent, bg='black')

        # Referenciar al controlador principal
        self.controller = controller

        # Texto descriptivo
        label = tk.Label(self, text='¿Con que quieres Jugar?', font=LARGE_FONT,
                         bg='black', fg='white')
        label.pack(pady=10, padx=10)

        # Crea los botones para seleccionar.
        # Cada uno ejecuta StartGame, con la opción, del master
        # para arrancar el juego
        option1 = tk.Button(self, text="X", font=MEDIUM_FONT, width=15,
                            command=lambda: self.controller.startGame(1))
        option2 = tk.Button(self, text="O", font=MEDIUM_FONT, width=15,
                            command=lambda: self.controller.startGame(2))

        # Muestra y posiciona los botones
        option1.pack(pady=15, padx=10)
        option2.pack(pady=18, padx=10)


class BoardPage(tk.Frame):
    """Ventana del tablero"""

    # Constructor
    def __init__(self, parent, controller):
        # inicializa la ventana
        tk.Frame.__init__(self, parent, bg='black')

        # Referenciar al controlador principal
        self.controller = controller

        # Constantes para la dimensionalidad de los botones.
        # Ancho
        bw = 3
        # Alto
        bh = 7

        # Variables a utilizar
        # Guarda los objetos de los botones
        self.boardObjects = []
        # Valores numericos del tablero. Se inicializa en
        # tablero vacio
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        # turno de player. Se inicializa con 1 (X)
        self.player = 1
        # Estado del juego. Se inicializa en play
        self.state = 'play'

        # Construye los objetos de los botones que formaran
        # la cuadricula del tablero. Cada objeto accionará
        # la función humanTurn con su respectiva posición.
        pos1 = tk.Button(self, text=' ', height=bw, width=bh,
                         font=MEDIUM_FONT, borderwidth=1,
                         command=lambda: self.humanTurn(1))
        pos1.grid(row=2, column=1)
        self.boardObjects.append(pos1)

        pos2 = tk.Button(self, text=' ', height=bw, width=bh,
                         font=MEDIUM_FONT, borderwidth=1,
                         command=lambda: self.humanTurn(2))
        pos2.grid(row=2, column=2)
        self.boardObjects.append(pos2)

        pos3 = tk.Button(self, text=' ', height=bw, width=bh,
                         font=MEDIUM_FONT, borderwidth=1,
                         command=lambda: self.humanTurn(3))
        pos3.grid(row=2, column=3)
        self.boardObjects.append(pos3)

        pos4 = tk.Button(self, text=' ', height=bw, width=bh,
                         font=MEDIUM_FONT, borderwidth=1,
                         command=lambda: self.humanTurn(4))
        pos4.grid(row=3, column=1)
        self.boardObjects.append(pos4)

        pos5 = tk.Button(self, text=' ', height=bw, width=bh,
                         font=MEDIUM_FONT, borderwidth=1,
                         command=lambda: self.humanTurn(5))
        pos5.grid(row=3, column=2)
        self.boardObjects.append(pos5)

        pos6 = tk.Button(self, text=' ', height=bw, width=bh,
                         font=MEDIUM_FONT, borderwidth=1,
                         command=lambda: self.humanTurn(6))
        pos6.grid(row=3, column=3)
        self.boardObjects.append(pos6)

        pos7 = tk.Button(self, text=' ', height=bw, width=bh,
                         font=MEDIUM_FONT, borderwidth=1,
                         command=lambda: self.humanTurn(7))
        pos7.grid(row=4, column=1)
        self.boardObjects.append(pos7)

        pos8 = tk.Button(self, text=' ', height=bw, width=bh,
                         font=MEDIUM_FONT, borderwidth=1,
                         command=lambda: self.humanTurn(8))
        pos8.grid(row=4, column=2)
        self.boardObjects.append(pos8)

        pos9 = tk.Button(self, text=' ', height=bw, width=bh,
                         font=MEDIUM_FONT, borderwidth=1,
                         command=lambda: self.humanTurn(9))
        pos9.grid(row=4, column=3)
        self.boardObjects.append(pos9)

        # Crea el boton para reiniciar la partida. Esto
        # permitirá cambiar de jugador.
        rs = tk.Button(self, text='Reiniciar', bg='grey',
                       font=MEDIUM_FONT, borderwidth=2,
                       command=lambda: self.restart())
        rs.grid(row=2, column=5)

    # Deshabilita todos los botones
    def disAll(self):
        for obj in self.boardObjects:
            obj.config(state=tk.DISABLED)

    # Escribe los valores en los botones
    def setBoard(self):
        for value, obj in zip(self.board, self.boardObjects):
            # Si no es cero, entonces algun jugador le seleccionó.
            # en otro caso, se desea limpiar el tablero
            if value != 0:
                # Actualiza el texto
                obj['text'] = 'X' if value == 1 else 'O'
                # Deshabilita el boton.
                obj.config(state=tk.DISABLED)
            else:
                obj['text'] = ' '
                obj.config(state=tk.ACTIVE)

    # Reinicia el juego
    def restart(self):
        # Reinicia el tablero
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        # Reinicia el estado
        self.state = 'play'
        # Reinicia el jugador
        self.player = 1

        self.setBoard()
        # Llama a StartPage
        self.controller.show_frame(StartPage)

    # Turno del Humano
    def humanTurn(self, position):
        # Si el estado es 'play', entonces aun se puede jugar.
        # en otro caso, la máquina ganó o hubo empate
        if self.state == 'play':
            self.player, self.state, self.board = pl.moveHuman(self.player, self.state, self.board, position)
            self.setBoard()
            self.checkWinner()
            self.machineTurn()
        # elif self.state == 'win':
        #     mssg.showinfo('Fin', 'La máquina ganó')
        #     self.disAll()
        # else:
        #     mssg.showinfo('Fin', 'Empate!')

    # Turno de la máquina
    def machineTurn(self):
        # Si el estado es 'play', entonces aun se puede jugar.
        # en otro caso, el humano ganó o hubo empate
        if self.state == 'play':
            self.player, self.state, self.board = pl.moveMachine(self.player, self.state, self.board)
            self.setBoard()
            self.checkWinner()
        # elif self.state == 'win':

            # mssg.showinfo('Fin', 'Ganaste!')
            # self.disAll()
        # else:
        #     mssg.showinfo('Fin', 'Empate!')

    # verifica si hay resultado
    def checkWinner(self):
        # Si el estado es 'win' entonces hay ganador.
        # En otro caso, es empate.
        if self.state == 'win':
            # El ganador será el jugador contraio al 'player' actual.
            # Podemos saber quien por el arreglo 'order'.
            winner = self.controller.order[0] if self.player == 2 \
                else self.controller.order[1]

            # Imprime el mensaje
            message = f'Victoria de {winner}'
            mssg.showinfo('Fin', message)

            # Deshabilita todos los botones.
            self.disAll()

        elif self.state == 'draw':
            # Imprime el mesaje.
            mssg.showinfo('Fin', 'Empate')
            # Deshabilita todos los botones.
            self.disAll()