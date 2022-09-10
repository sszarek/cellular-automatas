import string
from shell.configuration import Configuration
from shell.application import Application

CELL_SIZE: int = 5
X_CELLS: int = 120
Y_CELLS: int = 120
WINDOW_CAPTION: string = "Game of Life"
FRAME_RATE: int = 10

frame_rate: int = 10

configuration = Configuration(CELL_SIZE, Y_CELLS, X_CELLS, WINDOW_CAPTION, FRAME_RATE)
app = Application(configuration)

app.run()
