# Sitio INACAP - Evaluación Sumativa #3 (Programación Back End, TI3041)

Aplicación web en Django con autenticación, perfiles con permisos diferenciados, mantenedores CRUD, una transacción operacional y recuperación de contraseña por correo. Evoluciona el proyecto de la Evaluación Sumativa N°2 y **no usa Django Admin** para operar el sistema.

## Objetivo y problemática

Gestionar el perfil de egreso de la carrera Analista Programador: estudiantes egresados, asignaturas de la malla y notas, con acceso restringido según el perfil de cada usuario.

## Tecnologías

- Python 3.11, Django, Django ORM y migraciones
- MySQL/MariaDB (variables de entorno con python-dotenv)
- Bootstrap (local) y Django Templates
- Gunicorn + NGINX en AWS EC2 (Amazon Linux 2023)
- GitHub para control de versiones
- Herramientas de IA como apoyo al desarrollo

## Apps del proyecto

| App | Contenido |
|---|---|
| `malla` | Semestres y asignaturas (mantenedor de Asignatura) |
| `egreso` | Estudiantes, notas, campos laborales y competencias (mantenedor de Estudiante y transacción de Nota) |
| `cuentas` | Login, logout, dashboards por perfil, mantenedor de usuarios y recuperación de contraseña |

## Perfiles y permisos

Se crean con `python manage.py crear_grupos`.

| Perfil | Permisos |
|---|---|
| Administrador | Todo sobre Estudiante, Asignatura y Nota, más gestión de usuarios |
| Supervisor | Ver, agregar y modificar. No elimina ni gestiona usuarios |
| Administrativo | Solo ver Estudiante y Asignatura; registrar y ver Notas |

Las vistas están protegidas con `login_required` y `permission_required`. Sin permiso se responde 403, y los botones solo se muestran si el perfil tiene el permiso.

## Funcionalidades

- **Autenticación:** inicio de sesión, cierre de sesión y vistas protegidas.
- **Dashboards:** uno por perfil (Administrador, Supervisor, Administrativo).
- **Mantenedores CRUD completos con búsqueda y validaciones:** Estudiante, Asignatura y Usuarios (con asignación de perfil).
- **Transacción:** registro de Notas, que relaciona Estudiante y Asignatura. Valida calificación entre 1.0 y 7.0 y evita duplicados.
- **Recuperación de contraseña por correo:** solicitud, token seguro (vence en 1 hora), enlace por correo, validación del token, nueva contraseña y confirmación.

## Rutas principales

| Ruta | Descripción |
|---|---|
| `/cuentas/login/` | Inicio de sesión |
| `/cuentas/dashboard/` | Dashboard según perfil |
| `/cuentas/usuarios/` | Mantenedor de usuarios |
| `/cuentas/recuperar/` | Solicitud de recuperación de contraseña |
| `/egreso/estudiantes/` | Mantenedor de Estudiante |
| `/egreso/registro-notas/` | Transacción de Notas |
| `/malla/asignaturas/` | Mantenedor de Asignatura |
| `/malla/listado/` | Malla curricular |

## Modelo de datos

- `Semestre` 1 -> N `Asignatura`
- `Estudiante` 1 -> N `Nota` y `Asignatura` 1 -> N `Nota`
- `Estudiante` 1 -> N `CampoLaboral`
- `Competencia`

## Instalación local

```
git clone https://github.com/renatoelsato-cloud/sitio-inacap-eval2.git
cd sitio-inacap-eval2
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Copiar `.env.example` a `.env` y completar los valores:

```
SECRET_KEY=
DB_ENGINE=
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
```

Si no se definen las variables de correo, los mensajes se imprimen en la consola.

```
python manage.py migrate
python manage.py crear_grupos
python manage.py crear_usuarios
python manage.py runserver
```

## Despliegue en AWS EC2

```
cd /var/www/sitio_inacap
source venv/bin/activate
git pull origin main
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
sudo systemctl restart gunicorn
```

## Seguridad

El archivo `.env` está en `.gitignore`: la SECRET_KEY, las credenciales de la base de datos y la contraseña de aplicación de Gmail no se suben al repositorio.

## Autor

Renato Cárdenas - INACAP La Serena
