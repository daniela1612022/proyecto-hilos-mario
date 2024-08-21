🎮 Proyecto Hilos Mario
📝 Descripción
Este proyecto es una implementación del primer nivel del clásico juego de Mario Bros, desarrollado en Python utilizando hilos (threads). La simulación muestra a Mario y otros elementos del juego, como enemigos y obstáculos, todos ejecutándose de manera concurrente para lograr una visualización dinámica en la consola. 🎉

🚀 Características
👾 Movimiento de Mario: Simula el movimiento de Mario a lo largo del nivel, incluyendo correr y saltar.
🐢 Enemigos: Se incluyen enemigos como Goombas y Koopas que se mueven de manera independiente en la pantalla.
🧱 Obstáculos: Implementa bloques y tuberías con los que Mario puede interactuar.
🔄 Hilos: Cada elemento del juego se maneja en un hilo separado, permitiendo acciones concurrentes y una simulación más realista.
📁 Estructura del Proyecto
    proyecto-hilos-mario/
    │
    ├── data/
    │   └── [Archivos relacionados con los datos del juego]
    │
    ├── resources/
    │   └── [Recursos adicionales como imágenes o configuraciones]
    │
    ├── mario_level_1.py    # Código principal para la simulación del primer nivel de Mario
    ├── README.md           # Documentación del proyecto
    └── [Otros archivos relacionados]

⚙️ Instalación
Clona el repositorio a tu máquina local:

  git clone https://github.com/daniela1612022/proyecto-hilos-mario.git
  cd proyecto-hilos-mario
  
Crea un entorno virtual y actívalo:

  python3 -m venv venv
  source venv/bin/activate

Instala las dependencias requeridas :

  pip install -r requirements.txt

🎮 Uso
Para iniciar la simulación, simplemente ejecuta el script principal:

  python mario_level_1.py
  
Mario comenzará a moverse por el nivel, enfrentándose a varios enemigos y obstáculos. Cada elemento del juego se ejecuta en su propio hilo, proporcionando una simulación fluida y dinámica en la consola.

🌟 Contenido de Otros Repositorios
Este proyecto incluye contenido de otros repositorios de código abierto que han sido adaptados y utilizados para mejorar la funcionalidad y visualización del juego.

🤝 Contribuir
¡Las contribuciones son bienvenidas! Si deseas mejorar la simulación o agregar nuevas características, por favor, realiza un fork del repositorio y envía un pull request. 🚀

📄 Licencia
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

📧 Contacto
Si tienes preguntas o sugerencias, no dudes en contactarme a través de danispc389@gmail.com.

