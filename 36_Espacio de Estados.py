class PuzzleState:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def __eq__(self, other):
        return self.puzzle == other.puzzle

    def __hash__(self):
        return hash(tuple(self.puzzle))

    def generar_acciones(self):
        acciones = []
        empty_row, empty_col = self.find_empty()
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Movimientos arriba, abajo, izquierda, derecha
        for dr, dc in moves:
            new_row, new_col = empty_row + dr, empty_col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_puzzle = [list(row) for row in self.puzzle]
                new_puzzle[empty_row][empty_col], new_puzzle[new_row][new_col] = new_puzzle[new_row][new_col], new_puzzle[empty_row][empty_col]
                acciones.append(PuzzleState(tuple(map(tuple, new_puzzle))))
        return acciones

    def find_empty(self):
        for i, row in enumerate(self.puzzle):
            for j, val in enumerate(row):
                if val == 0:
                    return i, j

# Ejemplo de uso
estado_inicial = PuzzleState(((1, 2, 3), (4, 0, 5), (6, 7, 8)))
acciones_posibles = estado_inicial.generar_acciones()

print("Acciones posibles desde el estado inicial:")
for accion in acciones_posibles:
    print(accion.puzzle)
