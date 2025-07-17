# Proyecto TechShop - Python y Django

## Comisión 78110

Profesor: Alan Exequiel Prestia  
Tutora: Gabriela Edith Rossi

## Alumno

Nombre: Ignacio Agustín Mahfud

---

## Descripción del proyecto

TechShop es una aplicación web tipo blog/tienda que permite gestionar productos tecnológicos, publicar novedades, registrar y administrar clientes, empleados y usuarios. Incluye funcionalidades de registro, login, perfil de usuario con avatar y biografía, manejo de publicaciones con contenido enriquecido (CKEditor), y páginas informativas como "Acerca de mí" y contacto.

---

## Funcionalidades principales

- Registro, inicio y cierre de sesión de usuarios.  
- Perfil de usuario editable con avatar, biografía y fecha de nacimiento.  
- Cambio de contraseña para usuarios.  
- CRUD completo de publicaciones (con título, subtítulo, contenido enriquecido, imagen y fecha).  
- Listado y detalle de publicaciones.  
- Registro y búsqueda de clientes, productos y empleados.  
- Páginas estáticas como "Acerca de mí" y "Contacto".  
- Navbar dinámico que muestra el nombre y avatar del usuario logueado.  
- Acceso restringido a la sección de registros solo para superusuarios.  
- Mensajes de éxito/error visibles al usuario.  
- Uso de CKEditor para contenido enriquecido en publicaciones.  
- Uso de vistas basadas en clases con mixins y vistas funcionales con decoradores.

---

## Orden para probar las funcionalidades

1. Abrir la página principal en `http://localhost:8000/`.  
2. Desde el menú navegar a las secciones:  
   - "Publicaciones" para ver el blog.  
   - "Acerca de mí" para información del autor.  
   - "Contacto" para enviar mensajes.  
   - "Buscar Productos" para buscar productos registrados.  
3. Para registrar clientes, productos o empleados usar las opciones disponibles.  
4. Crear un usuario nuevo o iniciar sesión para poder crear, editar o eliminar publicaciones y editar perfil.  
5. Solo el superusuario podrá acceder a la sección "Registros" para administrar datos.

---

## Ejecución del proyecto
1. Clonar el repositorio:  
   ```bash
   git clone https://github.com/tu-usuario/techshop.git
   cd techshop

2. Crear y activar el entorno virtual:
  python -m venv venv
  # Windows
  venv\Scripts\activate
  # Linux/macOS
  source venv/bin/activate

 3. Instalar dependencias:
 pip install -r requirements.txt

4. Aplicar migraciones y ejecutar el servidor:
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

5. Acceder en el navegador a:
http://localhost:8000/

---

## Acceso al panel de administración
Para acceder al admin de Django:
1. Ejecutar el servidor con python manage.py runserver.
2. Ir a http://localhost:8000/admin/ en el navegador.
3. Si no tenés superusuario creado, crear uno con: "python manage.py createsuperuser"

---

## Archivos excludios del repositorio
El archivo db.sqlite3 (base de datos), la carpeta media/ (archivos subidos por usuarios) y los archivos compilados de Python (__pycache__, .pyc) están incluidos en .gitignore para no ser subidos al repositorio.

## Tecnologías utilizadas
- Python 3
- Django 4.0+
- Bootstrap 5
- CKEditor para contenido enriquecido
- SQLite3 (Base de datos)