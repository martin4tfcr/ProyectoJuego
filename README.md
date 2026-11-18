# ProyectoJuego: Batalla Naval 5x5

## Integrantes del Equipo
* Matías Zúñiga[cite: 5]
* Mateo Coronado[cite: 5]
* Martín Torres[cite: 5]

---

## Descripción del Proyecto
Juego interactivo de **Batalla Naval** desarrollado en Python utilizando la librería gráfica `Tkinter` para el tablero de $5\times5$ celdas[cite: 5]. El proyecto cuenta con arquitectura modular y soporte para modalidades de juego local y comunicaciones en red mediante sockets TCP[cite: 5, 7].

---

## Estructura del Repositorio
* `juego.py`: Punto de entrada principal y gestión de la interfaz gráfica local[cite: 1, 6].
* `game_logic.py`: Lógica central del juego, tableros, validaciones y reglas de impacto[cite: 1, 6].
* `server.py`: Gestión del socket servidor y escucha en puerto TCP[cite: 1, 6].
* `client.py`: Conexión del cliente hacia la IP del servidor[cite: 1, 6].
* `LICENSE`: Archivo de licenciamiento Open Source (MIT)[cite: 1, 7].
* `README.md`: Documentación oficial, bitácora y créditos del proyecto[cite: 1].

---

## Declaración de Autoría y Licenciamiento
Este proyecto se distribuye bajo los términos de la **Licencia MIT** (consulte el archivo `LICENSE` para más detalles)[cite: 1, 7].

* **Créditos y Recursos de Terceros:** 
  * Se utilizaron conceptos de programación en red basados en la librería estándar de sockets de Python (`socket`).
  * Se consultó la documentación oficial de Python para la estructuración modular y el uso de interfaces gráficas con `Tkinter`.
  * Se contó con herramientas de asistencia de IA para la organización lógica del código inicial modular.

---

## Bitácora de Gestión de Conflictos

* **Hechos:** Durante la integración de la estructura modular con el archivo `game_logic.py`, se presentaron discrepancias en las rutas de importación de variables y nombres de funciones entre los equipos, lo que provocaba errores de ejecución al iniciar el programa.
* **Sentimientos:** Generó cierta frustración temporal y desacuerdos sobre cómo estructurar las dependencias sin romper el código beta que ya tenían avanzado.
* **Necesidades:** Requerimos mantener una estricta sincronización en los nombres de las variables globales y asegurar que todos los archivos dependientes se encuentren guardados en el mismo directorio de trabajo antes de ejecutar pruebas.
* **Petición:** Propongo realizar una validación cruzada de las importaciones en equipo y estandarizar un bloque base de constantes para evitar conflictos de nombres en las siguientes fases.
