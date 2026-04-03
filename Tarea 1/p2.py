import sys
from collections import defaultdict

def main():
    # Usamos readline para entrada rápida (importante si S es grande)
    input = sys.stdin.readline

    # N: numero de socios
    # M: numero de terminales
    # S: numero de transacciones
    N, M, S = map(int, input().split())

    # Diccionario que mapea:
    # terminal -> socio
    terminal_to_socio = {}

    # Leemos los M pares (p, t)
    # donde p = socio, t = terminal
    for _ in range(M):
        p, t = map(int, input().split())
        terminal_to_socio[t] = p
        # Esto permite luego identificar rápidamente
        # a qué socio pertenece cada terminal

    # Estructura principal de conteo:
    # socio -> {cliente -> número de compras}
    conteo = {i: defaultdict(int) for i in range(1, N + 1)}

    # Procesamos las S transacciones
    for _ in range(S):
        c, t = map(int, input().split())
        # c: cliente
        # t: terminal usado

        # Verificamos que el terminal exista
        if t not in terminal_to_socio:
            continue  # ignorar si no pertenece a ningún socio

        # Obtenemos el socio asociado al terminal
        socio = terminal_to_socio[t]

        # Incrementamos el número de compras del cliente c
        # para ese socio
        conteo[socio][c] += 1

    # Para cada socio, determinamos su cliente más fiel
    for socio in range(1, N + 1):
        clientes = conteo[socio]

        # Si no tiene transacciones
        if not clientes:
            print(socio, -1)
            continue

        # Variables para encontrar el óptimo
        mejor_cliente = -1
        max_compras = -1

        # Recorremos todos los clientes de ese socio
        for c, compras in clientes.items():

            # Condición de actualización:
            # 1. Mayor número de compras
            # 2. Empate → menor ID de cliente
            if (compras > max_compras or
               (compras == max_compras and c < mejor_cliente)):

                max_compras = compras
                mejor_cliente = c

        # Imprimimos el resultado para el socio
        print(socio, mejor_cliente)


# Punto de entrada del programa
if __name__ == "__main__":
    main()