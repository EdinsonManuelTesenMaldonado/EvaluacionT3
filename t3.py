ENERGIA_MAXIMA = 18

mapa = [
    [1, 1, 1, 1, 99, 1, 1, 1, "A"],
    [1, 99, 99, 1, 99, 1, 99, 1, 99],
    [1, 1, 99, 1, 1, 1, 99, 1, 99],
    [99, 1, 99, 1, 99, 99, 99, 1, 99],
    [1, 1, 99, -1, 1, 1, 1, 3, 99],
    [-2, 99, 99, 1, 99, 99, 99, 1, 1],
    [1, 99, 1, -1, 1, 1, 1, 1, 99],
    [1, 99, 99, 99, 99, 2, 99, 1, 99],
    ["B", 1, 3, 1, 1, 1, 99, 1, 1]
]

for fila in range(9):
    for col in range(9):
        if mapa[fila][col] == "A":
            punto_inicio = (fila, col)
            mapa[fila][col] = 0
        if mapa[fila][col] == "B":
            punto_final = (fila, col)
            mapa[fila][col] = 0

trayecto = [[0 for _ in range(9)] for _ in range(9)]

direcciones = [(0, -1), (1, 0), (-1, 0), (0, 1)]

def buscar_camino(f, c, energia_actual):
    if (f, c) == punto_final:
        trayecto[f][c] = 1
        return True

    trayecto[f][c] = 1

    for df, dc in direcciones:
        nf, nc = f + df, c + dc

        if 0 <= nf < 9 and 0 <= nc < 9:
            if mapa[nf][nc] == 99 or trayecto[nf][nc] == 1:
                continue

            celda = mapa[nf][nc]
            energia_restante = energia_actual - celda

            if celda == 0:
                energia_restante = energia_actual

            if energia_restante < 0:
                continue

            if buscar_camino(nf, nc, energia_restante):
                return True

    trayecto[f][c] = 0
    return False

print("MAPA ORIGINAL:\n")
for fila in mapa:
    print(fila)

print("\nIniciando búsqueda...\n")

if buscar_camino(punto_inicio[0], punto_inicio[1], ENERGIA_MAXIMA):
    print("¡Ruta encontrada! El personaje puede salir.\n")
else:
    print("No hay salida posible con la energía disponible.\n")

print("TRAYECTO RECORRIDO (1 = camino):\n")
for fila in trayecto:
    print(fila)