# MiPrimeraPagina+Arenas
Proyecto para el curso de coderhouse Python Flex

1) Requisitos: tener instalado Python 3.11 o superior y Git
2) Clonar el repositorio: abrir una terminal y clonar el link del repositorio:
git clone "link del repositorio"
2) Crear un entorno virtual: 
py -m venv .venv
.venv\Scripts\activate
3) Entrar al entorno virtual e instalar el archivo requirements.txt:
pip freeze > requirements.txt
4) Iniciar django, y preparar la base de datos:
python manage.py migrate
python manage.py runserver
5) Abrir en el navegador:
http://127.0.0.1:8000/
