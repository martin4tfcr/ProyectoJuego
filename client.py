# client.py: Conexión del cliente a la IP del servidor
import socket

HOST = '127.0.0.1'  # Cambiar por la IP del servidor en la red local
PORT = 65432

def iniciar_cliente():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        cliente.connect((HOST, PORT))
        print(f"[CLIENTE] Conectado exitosamente al servidor en {HOST}:{PORT}")
        
        # Ejemplo de envío de datos por red
        mensaje = "Hola servidor, listo para disparar"
        cliente.sendall(mensaje.encode('utf-8'))
        
        respuesta = cliente.recv(1024).decode('utf-8')
        print(f"[CLIENTE] Respuesta del servidor: {respuesta}")
        
    except ConnectionRefusedError:
        print("[CLIENTE] Error: No se pudo conectar con el servidor. Verifique que esté encendido.")
    finally:
        cliente.close()

if __name__ == "__main__":
    iniciar_cliente()