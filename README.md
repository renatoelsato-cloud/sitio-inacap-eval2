# Sitio INACAP - Analista Programador

Evaluación Sumativa 2 - Programación Back End (TI3041) - INACAP La Serena

## Descripción

Aplicación web hecha con Django que continúa el proyecto de la Evaluación Sumativa 1. La información que antes se leía desde archivos JSON ahora se guarda en una base de datos relacional (MySQL/MariaDB), se administra desde Django Admin y se muestra en páginas con plantillas Django y Bootstrap.

La aplicación se despliega en una instancia Amazon EC2 (Linux) y el código se distribuye mediante GitHub.

## Aplicaciones

- **malla**: malla curricular de la carrera (semestres y asignaturas).
- **egreso**: perfil de egreso (egresados, notas, campo laboral y competencias).

## Modelos y relaciones

| App | Modelo | Descripción | Relaciones |
|---|---|---|---|
| malla | Semestre | Número de semestre y horas totales | Tiene muchas asignaturas |
| malla | Asignatura | Nombre, código y créditos | ForeignKey a Semestre |
| egreso | Estudiante | Nombre, RUT, correo y año de egreso | Tiene muchas notas y campos laborales |
| egreso | Nota | Calificación de un estudiante en una asignatura | ForeignKey a Estudiante y a Asignatura |
| egreso | CampoLaboral | Empresa, cargo y descripción | ForeignKey a Estudiante (opcional) |
| egreso | Competencia | Nombre y descripción | Sin relaciones |

## Tecnologías

Python, Django, MySQL/MariaDB (mysqlclient), python-dotenv, Bootstrap y Bootstrap Icons, Git y GitHub, AWS EC2.

## Variables de entorno

Las credenciales de la base de datos no están escritas en el código. Se guardan en un archivo `.env` (que no se sube al repositorio) y se cargan con python-dotenv. Para usarlo, copiar `.env.example` a `.env` y completar los valores:

- DB_ENGINE
- DB_NAME
- DB_USER
- DB_PASSWORD
- DB_HOST
- DB_PORT

## Instalación

    git clone https://github.com/renatoelsato-cloud/sitio-inacap-eval2.git
    cd sitio-inacap-eval2
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

Crear el archivo `.env` y luego:

    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver 0.0.0.0:8000

Nota: en la instancia EC2 (Python 3.14) se usa Django 5.2, porque Django 4.2 no es compatible con Python 3.14. En el equipo de desarrollo (Python 3.11) se usa Django 4.2.

## Rutas

- `/admin/`: panel de administración de Django.
- `/malla/listado/`: listado de la malla curricular.
- `/egreso/`: egresados y campo laboral.
- `/egreso/competencias/`: competencias del perfil de egreso.
- `/egreso/notas/`: notas de los estudiantes.

## Funcionalidad

- Django Admin permite crear, modificar, eliminar, visualizar y buscar registros de todas las entidades, y navegar entre entidades relacionadas.
- Las vistas obtienen la información con Django ORM y la muestran en tablas Bootstrap.
- Los botones Agregar, Modificar, Eliminar y Buscar de las vistas son solo visuales. Su funcionamiento se implementa en la siguiente evaluación.

## Autor

Renato Cárdenas - INACAP La Serena (Analista Programador)
