# PRE-ENTREGRA 3 - DANIELA SOLER COLLAO

Este proyecto se pasará con link directo de la plataforma de GitHub.
Para bajar la información del proyecto, copiar el url y escribir en la consola de Visual Studio Code (dentro del directorio deseado):

**`git clone linkGitHuB`**

Asegurarse que el link termine en .git

Este proyecto se encuentra respaldado en su totalidad, con excepción del entorno virtual. Por lo que se debe crear el entrono virtual para poder acceder directamente al proyecto.Ejecute

**`python -m venv .venv`**

Luego de creado el entorno virtual (se encontrará dentro de la carpeta .venv), activar el entorno de la siguiente forma. Para Windows ejecutar:

**`.venv/Scripts/activate`**

Para Mac o Linux ejecutar:

**`.venv\bin\activate`**

Una vez activo el entorno (aparecerá al principio del directorio `(.venv)`), debemos ejecutar archivo requirements.txt, el cual instalará dentro del entorno virtual lo necesario para correr el proyecto.

**`pip install -r requirements.txt`**

El cual fue creado con el comando `pip freeze >> requirements.txt`.
Para finalizar, hacemos correr el servidor, el cual nos dará una url local para visualizar la página web creada. Este comando debe ejecutarse DENTRO de la carpeta project para que encuentre el archivo manage.py

**`python manage.py runserver`**

Para finalizar la ejecución del servidor, pulse las teclas `CTRL + C`.

# Sobre el Proyecto

Este consta de 7 apps, siendo Home la página principal. Para poder agregar información a la base de datos de cualquier app (excepto Home) y ser visualizada directo en la página web, se debe ingresar al admin de la página web `http://127.0.0.1:8000/admin/`.

Usuario: `admin`
Contraseña: `1234`

Aquí se entra al administrador de Django, donde se puede añadir información a las 6 apps (con excepción de Home). 
La única url que no se visualizable directamente de la página web es la que muestra las subscripciones realizadas. Éstas se pueden ver en `http://127.0.0.1:8000/subscribete/SUBSCRIPCIONES/`.

# Cosas a mejorar

- Aspecto de colores de la página web, el cuál se encuentra en código .css
- Lograr encadenar las imágenes puestas detro de las apps de forma más eficiente (a través de herencia) y así no se repita la imagen.
- Respecto al punto anterior, no se si es posible agregar imágenes con el administrados de Django.
- Se podría hacer más eficiente el código utilizando menos apps, ya que las apps `Juegos`, `Libreria`, `Lugares` y `series_peliculas` se basan en el mismo template, por lo que podría disminuirse el código.
