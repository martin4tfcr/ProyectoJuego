# juego.py: Punto de entrada y selección de modo (Interfaz Tkinter)
import tkinter as tk
from tkinter import messagebox
from game_logic import N, LARGOS, C_VACIO, C_BARCO, C_TOCADO, C_AGUA, C_OCULTO, barcos_restantes

class BatallaNavalApp:
    def __init__(self, root):
        self.root = root
        root.title("Batalla Naval 5x5 - Modo Local")
        root.resizable(False, False)
        
        self.titulo = tk.Label(root, text="BATALLA NAVAL", font=("Arial", 18, "bold"))
        self.titulo.pack(pady=(10, 0))
        
        self.info = tk.Label(root, text="", font=("Arial", 12), wraplength=350, height=3)
        self.info.pack(pady=5)

        self.grid_frame = tk.Frame(root)
        self.grid_frame.pack(padx=15)
        
        for c in range(N):
            tk.Label(self.grid_frame, text=str(c + 1), font=("Arial", 10, "bold")).grid(row=0, column=c + 1)
            
        self.botones = []
        for f in range(N):
            tk.Label(self.grid_frame, text=str(f + 1), font=("Arial", 10, "bold")).grid(row=f + 1, column=0, padx=4)
            fila = []
            for c in range(N):
                b = tk.Button(self.grid_frame, width=5, height=2, bg=C_OCULTO,
                              font=("Arial", 12, "bold"),
                              command=lambda f=f, c=c: self.clic(f, c))
                b.grid(row=f + 1, column=c + 1, padx=1, pady=1)
                fila.append(b)
            self.botones.append(fila)
            
        controles = tk.Frame(root)
        controles.pack(pady=10)
        self.btn_orient = tk.Button(controles, text="Orientación: Horizontal", command=self.cambiar_orient)
        self.btn_orient.grid(row=0, column=0, padx=5)
        
        self.btn_listo = tk.Button(controles, text="Listo", width=14)
        self.btn_listo.grid(row=0, column=1, padx=5)
        
        tk.Button(controles, text="Reiniciar", command=self.iniciar).grid(row=0, column=2, padx=5)
        self.iniciar()

    def iniciar(self):
        self.barcos = {1: [], 2: []}  
        self.disparos = {1: set(), 2: set()} 
        self.orient = "H"
        self.btn_orient.config(text="Orientación: Horizontal")
        self.activo = False
        self.pasar("Jugador 1: coloca tus barcos.\n(El jugador 2 no debe mirar)",
                   lambda: self.empezar_colocacion(1))

    def pasar(self, mensaje, siguiente):
        self.activo = False
        for f in range(N):
            for c in range(N):
                self.botones[f][c].config(bg=C_OCULTO, text="")
        self.info.config(text=mensaje)
        self.btn_orient.config(state="disabled")
        self.btn_listo.config(text="Listo", state="normal", command=siguiente)

    def cambiar_orient(self):
        if self.orient == "H":
            self.orient = "V"
            self.btn_orient.config(text="Orientación: Vertical")
        else:
            self.orient = "H"
            self.btn_orient.config(text="Orientación: Horizontal")

    def empezar_colocacion(self, p):
        self.jug = p
        self.indice = 0
        self.activo = True
        self.btn_orient.config(state="normal")
        self.btn_listo.config(state="disabled")
        self.dibujar_propio()
        self.info.config(text=f"Jugador {p}: coloca el barco de {LARGOS[0]} casillas.\nHaz clic en la casilla inicial.")

    def celdas_ocupadas(self, p):
        todas = set()
        for barco in self.barcos[p]:
            for celda in barco:
                todas.add(celda)
        return todas

    def dibujar_propio(self):
        ocupadas = self.celdas_ocupadas(self.jug)
        for f in range(N):
            for c in range(N):
                color = C_BARCO if (f, c) in ocupadas else C_VACIO
                self.botones[f][c].config(bg=color, text="")

    def colocar(self, f, c):
        largo = LARGOS[self.indice]
        celdas = []
        for k in range(largo):
            if self.orient == "H":
                celdas.append((f, c + k))
            else:
                celdas.append((f + k, c))
        for (ff, cc) in celdas:
            if ff >= N or cc >= N:
                self.info.config(text="El barco se sale del tablero. Prueba otra casilla.")
                return
        ocupadas = self.celdas_ocupadas(self.jug)
        for celda in celdas:
            if celda in ocupadas:
                self.info.config(text="Se cruza con tu otro barco. Prueba otra posición.")
                return
        self.barcos[self.jug].append(celdas)
        self.indice += 1
        self.dibujar_propio()
        if self.indice < len(LARGOS):
            self.info.config(text=f"Jugador {self.jug}: ahora el barco de {LARGOS[self.indice]} casillas.")
        else:
            self.activo = False
            self.btn_orient.config(state="disabled")
            if self.jug == 1:
                self.btn_listo.config(text="Ocultar y pasar", state="normal",
                                      command=lambda: self.pasar(
                                          "Jugador 2: coloca tus barcos.\n(El jugador 1 no debe mirar)",
                                          lambda: self.empezar_colocacion(2)))
                self.info.config(text="¡Barcos listos! Pulsa 'Ocultar y pasar'.")
            else:
                self.btn_listo.config(text="Ocultar y pasar", state="normal",
                                      command=lambda: self.pasar(
                                          "¡Empieza la batalla!\nTurno del jugador 1.",
                                          lambda: self.empezar_turno(1)))
                self.info.config(text="¡Barcos listos! Pulsa 'Ocultar y pasar'.")

    def empezar_turno(self, p):
        self.jug = p
        self.enemigo = 3 - p
        self.activo = True
        self.btn_listo.config(state="disabled")
        self.dibujar_enemigo()
        restantes = barcos_restantes(self.barcos[self.enemigo], self.disparos[self.enemigo])
        self.info.config(text=f"Turno del jugador {p}: haz clic para disparar.\nBarcos enemigos restantes: {restantes}")

    def dibujar_enemigo(self):
        ocupadas = self.celdas_ocupadas(self.enemigo)
        for f in range(N):
            for c in range(N):
                if (f, c) in self.disparos[self.enemigo]:
                    if (f, c) in ocupadas:
                        self.botones[f][c].config(bg=C_TOCADO, text="X", fg="white")
                    else:
                        self.botones[f][c].config(bg=C_AGUA, text="•", fg="white")
                else:
                    self.botones[f][c].config(bg=C_VACIO, text="", fg="black")

    def disparar(self, f, c):
        if (f, c) in self.disparos[self.enemigo]:
            self.info.config(text="Ya disparaste ahí. Elige otra casilla.")
            return
        self.disparos[self.enemigo].add((f, c))
        self.dibujar_enemigo()
        self.activo = False
        
        resultado = "¡Agua!"
        for barco in self.barcos[self.enemigo]:
            if (f, c) in barco:
                resultado = "¡TOCADO!"
                hundido = True
                for celda in barco:
                    if celda not in self.disparos[self.enemigo]:
                        hundido = False
                if hundido:
                    resultado = f"¡TOCADO Y HUNDIDO! (barco de {len(barco)} casillas)"
                    
        restantes = barcos_restantes(self.barcos[self.enemigo], self.disparos[self.enemigo])
        if restantes == 0:
            self.info.config(text=f"¡EL JUGADOR {self.jug} GANA LA PARTIDA!")
            self.btn_listo.config(text="Jugar de nuevo", state="normal", command=self.iniciar)
            messagebox.showinfo("Fin del juego", f"¡El jugador {self.jug} derribó todos los barcos y gana!")
            return
            
        self.info.config(text=resultado)
        siguiente = self.enemigo
        self.btn_listo.config(text="Pasar turno", state="normal",
                              command=lambda: self.pasar(f"Turno del jugador {siguiente}.",
                                                         lambda: self.empezar_turno(siguiente)))

    def clic(self, f, c):
        if not self.activo:
            return
        if self.btn_listo["text"] == "Listo" and self.btn_listo["state"] == "normal":
            return
        if self.btn_orient["state"] == "normal":
            self.colocar(f, c)
        else:
            self.disparar(f, c)

if __name__ == "__main__":
    root = tk.Tk()
    BatallaNavalApp(root)
    root.mainloop()