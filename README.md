📖 Telegram Bible Verse Bot

Un bot de Telegram que permite obtener versículos bíblicos, capítulos completos, realizar búsquedas rápidas y recibir un versículo diario.
Utiliza la Bible API y está desarrollado con Python y python-telegram-bot (v20+).

✨ Funciones disponibles
/verse [libro capítulo:versículo]

Devuelve un versículo específico.
Ejemplo:

/verse Juan 3:16

/chapter [libro capítulo]

Devuelve un capítulo completo.

/search [texto]

Busca versículos que coincidan con un texto.
Ejemplo:

/search amor

/random

Devuelve un versículo aleatorio.

/daily

Activa un envío diario automático de un versículo.

📦 Estructura del proyecto
bot/
│   main.py
│   config.py
│   __init__.py
│
├───handlers/
│       verse.py
│       chapter.py
│       search.py
│       random_verse.py
│       daily.py
│       __init__.py
│
├───services/
│       bible_service.py
│       __init__.py
│
├───client/
│       http.py
│       __init__.py
│
└───utils/
        cache.py
        __init__.py

⚙️ Instalación
1. Clonar el repositorio
git clone https://github.com/tuusuario/telegram-bible-verse-bot.git
cd telegram-bible-verse-bot

2. Crear entorno virtual (opcional)
python -m venv venv
venv\Scripts\activate   # Windows

3. Instalar dependencias
pip install -r requirements.txt

🔑 Configuración

En bot/config.py, definí tu token del bot:

TOKEN = "TU_TOKEN_AQUI"
API_URL = "https://bible-api.com/"


⚠️ Importante: Nunca publiques el token del bot en GitHub.
Usá variables de entorno si querés mayor seguridad.

▶️ Ejecutar el bot

Desde la raíz del proyecto:

py -m bot.main


El bot iniciará modo polling de forma asíncrona.

🧩 Dependencias principales

python-telegram-bot ≥ 20

aiohttp

pytz

APScheduler

Todas están listadas en requirements.txt.

🤝 Contribuciones

Pull requests, mejoras y correcciones son bienvenidas.

📄 Licencia

MIT License.