# game_logic.py: Lógica central para la matriz 5x5 y validaciones

N = 5
LARGOS = [2, 4]

# Colores de la interfaz
C_VACIO = "#d6eaf8"
C_BARCO = "#34495e"
C_TOCADO = "#e74c3c"
C_AGUA = "#5dade2"
C_OCULTO = "#bdc3c7"

def crear_tablero():
    """Crea una matriz de 5x5 inicializada en celdas vacías"""
    return [["~" for _ in range(N)] for _ in range(N)]

def validar_coordenada(f, c):
    """Valida que la coordenada esté dentro del rango 0 a N-1"""
    return 0 <= f < N and 0 <= c < N

def verificar_hundido(barco, disparos):
    """Verifica si un barco específico ha sido completamente hundido"""
    for celda in barco:
        if celda not in disparos:
            return False
    return True

def barcos_restantes(barcos_jugador, disparos_enemigos):
    """Cuenta cuántos barcos siguen con vida"""
    total = 0
    for barco in barcos_jugador:
        if not verificar_hundido(barco, disparos_enemigos):
            total += 1
    return total