# server.py: Gestión del socket servidor y escucha en puerto TCP
import socket

HOST = '0.0.0.0'  # Escucha en todas las interfaces de red locales
PORT = 65432      # Puerto TCP del juego

def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((HOST, PORT))
    servidor.listen(1)
    print(f"[SERVIDOR] Escuchando conexiones en el puerto {PORT}...")
    
    conexion, addr = servidor.accept()
    print(f"[SERVIDOR] ¡Cliente conectado desde la IP: {addr}!")
    
    # Aquí puedes enviar y recibir datos de la partida multijugador en red
    try:
        while True:
            mensaje = conexion.recv(1024).decode('utf-8')
            if not mensaje:
                break
            print(f"[RED] Mensaje recibido del cliente: {mensaje}")
            # Responder al cliente
            conexion.sendall("Impacto recibido correctamente".encode('utf-8'))
    except ConnectionResetError:
        print("[SERVIDOR] El cliente se ha desconectado.")
    finally:
        conexion.close()
        servidor.close()

if __name__ == "__main__":
    iniciar_servidor()