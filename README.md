# sitio_inacap

Proyecto Django de la asignatura Programación Back End (TI3041), Evaluación Sumativa 2, INACAP La Serena.

Sitio web sobre la malla curricular de Analista Programador, con dos aplicaciones (`malla` y `egreso`). Los datos, que antes estaban en archivos JSON, ahora se guardan en una base de datos relacional MySQL y se administran desde Django Admin.

## Aplicaciones y modelos

- `malla`: Semestre y Asignatura (Asignatura tiene una llave foránea a Semestre).
- `egreso`: Estudiante, Nota, CampoLaboral y Competencia (Nota se relaciona con Estudiante y Asignatura; CampoLaboral se relaciona con Estudiante).

## Tecnologías

- Python 3.14 y Django 5.2
- MySQL (conector `mysqlclient`)
- Gunicorn y Nginx en una instancia AWS EC2 (Amazon Linux 2023)
- Bootstrap local y variables de entorno con `python-dotenv`

## Instalación

1. Clonar el repositorio:

        git clone https://github.com/renatoelsato-cloud/sitio-inacap-eval2.git

2. Crear y activar el entorno virtual, e instalar las dependencias:

        python3.14 -m venv venv
        source venv/bin/activate
        pip install -r requirements.txt

3. Crear el archivo `.env` a partir de la plantilla `.env.example` y completar los valores: `DB_ENGINE`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT` y `SECRET_KEY`. El archivo `.env` no se sube al repositorio.

4. Aplicar las migraciones, recopilar los archivos estáticos y crear el superusuario:

        python manage.py migrate
        python manage.py collectstatic --noinput
        python manage.py createsuperuser

## Uso

- Sitio: página de inicio y listados de `malla` y `egreso`, leídos desde la base de datos con el ORM de Django.
- Administración: `/admin/`, donde se pueden crear, modificar, eliminar, visualizar y buscar registros de todas las entidades.
