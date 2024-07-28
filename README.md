# Moral Games

Bienvenido a Moral Games, una tienda de videojuegos desarrollada con Django.

## Descripción del Proyecto

Moral Games es una plataforma en línea que permite a los usuarios explorar, comprar y disfrutar de una amplia variedad de videojuegos. Los usuarios pueden registrarse, iniciar sesión, agregar juegos a su carrito de compras, leer blogs sobre la industria y ver trailers de juegos.

## Características Principales

- **Autenticación de usuarios:** Los usuarios pueden iniciar sesión y registrarse para acceder a funcionalidades exclusivas.
- **Historial de compras:** Los usuarios pueden revisar su historial de compras y obtener detalles de las transacciones pasadas.
- **Carrito de compras:** Agrega tus videojuegos favoritos al carrito antes de realizar la compra.
- **Pasarela de pago simulada:** Utiliza nuestra pasarela de pago simulada para realizar compras de manera segura. (Nota: Esta pasarela de pago no realiza transacciones reales, es solo para propósitos de prueba).
- **Exploración de videojuegos:** Navega por una amplia variedad de videojuegos disponibles para su compra.
- **Blogs:** Lee blogs relacionados con tus videojuegos favoritos, noticias de la industria y más.
- **Compras:** Agrega videojuegos al carrito y realiza compras seguras.
- **Trailers:** Disfruta de trailers de videojuegos directamente desde la plataforma.
- **Búsqueda:** Encuentra fácilmente videojuegos utilizando la función de búsqueda.
- **Sección de contacto:** ¿Tienes preguntas o comentarios? Visita nuestra sección de contacto para comunicarte con nosotros.
- **Galería:** Observa imágenes de videojuegos por género, por plataforma y ver las últimas imágenes incluidas.

## Configuración del Proyecto en AWS

### S3 Service

1. **Crear un Bucket en S3**
   - [Crear Bucket en S3](https://us-east-1.console.aws.amazon.com/s3/bucket/create?region=us-east-1&bucketType=general)
     - Asegúrate de seleccionar la región donde deseas desplegar el proyecto.
   - En "Tipo de bucket", selecciona "Uso General".
   - Selecciona un nombre único para el bucket.
   - En "Propiedad de objeto", selecciona "ACL deshabilitadas (recomendado)".
   - **Importante:** En "Configuración de bloqueo de acceso público para este bucket", deselecciona "Bloquear todo el acceso público".
     - Selecciona "Reconozco que la configuración actual puede provocar que este bucket y los objetos que contiene se vuelvan públicos".
   - En "Control de versiones de buckets", selecciona "Desactivar".
   - Deja las demás opciones por defecto y crea el bucket.
   - Una vez creado, haz clic en el nombre del bucket y dirígete a "Permisos".
   - Edita la política del bucket y pega el siguiente JSON, reemplazando `ARN_BUCKET` por el ARN de tu bucket:

     ```json
     {
         "Version": "2012-10-17",
         "Id": "Policy1721957700099",
         "Statement": [
             {
                 "Sid": "Stmt1721957651307",
                 "Effect": "Allow",
                 "Principal": "*",
                 "Action": "s3:GetObject",
                 "Resource": "ARN_BUCKET/*"
             }
         ]
     }
     ```

   - Guarda los cambios.
   - Edita "Uso compartido de recursos entre orígenes (CORS)" y pega el siguiente JSON:

     ```json
     [
         {
             "AllowedHeaders": ["*"],
             "AllowedMethods": ["GET"],
             "AllowedOrigins": ["*"],
             "ExposeHeaders": []
         }
     ]
     ```

   - Para más información sobre políticas y CORS:
     - [Generador de Políticas AWS](https://awspolicygen.s3.amazonaws.com/policygen.html)
     - [Ejemplos de Políticas de Bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-bucket-policies.html?icmpid=docs_amazons3_console)

### IAM Service

1. **Crear un Usuario en IAM**
   - [Crear Usuario en IAM](https://us-east-1.console.aws.amazon.com/iam/home?region=us-east-1#/users)
     - Asegúrate de seleccionar la región donde deseas desplegar el proyecto.
   - Crear un usuario y agregar un nombre de usuario.
   - Activar "Proporcione acceso de usuario a la consola de administración de AWS".
   - En "Tipo de usuario", selecciona "Quiero crear un usuario IAM".
   - Agregar una contraseña personalizada o generada automáticamente.
   - (Opcional) Desactivar "Los usuarios deben crear una nueva contraseña en el siguiente inicio de sesión".
   - En "Opciones de permisos", seleccionar "Adjuntar políticas directamente".
   - Buscar en políticas de permisos y seleccionar "AmazonS3FullAccess".
   - Crear el usuario.
   - (Opcional) Descargar el CSV con la información del usuario creado.
   - Seleccionar el nombre del usuario creado.
   - Crear una clave de acceso y en "Caso de uso" seleccionar "Código local".
   - Confirmar la opción "Entiendo la recomendación anterior y deseo proceder a la creación de una clave de acceso".
   - Crear clave de acceso.
   - **Importante:** Guardar la clave de acceso y la clave de acceso secreta en un lugar seguro o descargar el archivo CSV.
   - Estas claves serán utilizadas para conectar la app de Django a un bucket de S3.

### EC2 Service

1. **Crear y Configurar una Instancia EC2**
   - [Lanzar Instancia EC2](https://us-east-1.console.aws.amazon.com/ec2/home?region=us-east-1#LaunchInstances:)
     - Asegúrate de seleccionar la región donde deseas desplegar el proyecto.
   - Agregar un nombre a la instancia.
   - Seleccionar sistema operativo Amazon Linux (o el de tu preferencia).
   - Seleccionar tipo de instancia `t2.micro` para la capa gratuita (puedes elegir otra si lo prefieres).
   - **Importante:** Crear un nuevo par de claves.
     - Agregar un nombre a la clave.
     - Seleccionar tipo RSA.
     - Seleccionar formato de archivo `.pem`.
     - Crear y guardar la clave en un directorio accesible.
   - Volver a la creación de la instancia y seleccionar la clave creada.
   - Permitir tráfico HTTPS e HTTP desde Internet.
   - Lanzar la instancia.
   - Conectarse a la instancia.
     - Seleccionar cliente SSH.
     - En la terminal, ejecutar el comando:

       ```sh
       chmod 400 "NOMBRE_DE_LA_CLAVE.pem"
       ```

     - Conectar a la instancia con el comando:

       ```sh
       ssh -i "NOMBRE_DE_LA_CLAVE.pem" ec2-user@dns_de_la_instancia.amazonaws.com
       ```

     - Más detalles en la sección de conectar mediante SSH en la consola de AWS.

   - Actualizar paquetes:

     ```sh
     sudo yum update -y
     ```

   - Instalar Python y pip:

     ```sh
     sudo yum install python3 python3-pip -y
     ```

   - Instalar virtualenv:

     ```sh
     pip install virtualenv
     ```

   - Instalar Nginx:

     ```sh
     sudo yum install -y nginx
     ```

   - Instalar Git:

     ```sh
     sudo yum install git
     ```

   - Clonar el proyecto:

     ```sh
     git clone https://github.com/zlcosio21/Moral-Games
     ```

   - Acceder al proyecto:

     ```sh
     cd Moral-Games
     ```

   - Crear un entorno virtual:

     ```sh
     virtualenv venv
     ```

   - Activar el entorno virtual:

     ```sh
     source venv/bin/activate
     ```

   - Instalar las librerías del proyecto:

     ```sh
     pip install -r requirements.txt
     ```

   - Realizar las migraciones:

     ```sh
     python manage.py migrate
     ```

   - (Opcional) Crear un superusuario:

     ```sh
     python manage.py createsuperuser
     ```

   - Crear un archivo `.env`:

     ```sh
     touch .env
     ```

   - Acceder y editar el archivo `.env`:

     ```sh
     nano .env
     ```

     - Ajusta el contenido con tus claves y email:

       ```env
       PASSWORD_DJANGO="contraseña_de_django"
       EMAIL="tu_email"
       PASSWORD="contraseña_de_aplicación"
       AWS_ACCESS_KEY_ID="clave_de_acceso"
       AWS_SECRET_ACCESS_KEY="clave_de_acceso_secreta"
       AWS_STORAGE_BUCKET_NAME="nombre_bucket"
       ```

   - Configurar Nginx:

     ```sh
     sudo nano /etc/nginx/nginx.conf
     ```

     - Reemplazar el contenido por lo siguiente, asegurándote de poner la IP de tu instancia EC2:

       ```nginx
       user nginx;
       worker_processes auto;
       error_log /var/log/nginx/error.log notice;
       pid /run/nginx.pid;

       include /usr/share/nginx/modules/*.conf;

       events {
           worker_connections 1024;
       }

       http {
           log_format main '$remote_addr - $remote_user [$time_local] "$request" '
                           '$status $body_bytes_sent "$http_referer" '
                           '"$http_user_agent" "$http_x_forwarded_for"';

           access_log /var/log/nginx/access.log main;

           sendfile on;
           tcp_nopush on;
           tcp_nodelay on;
           keepalive_timeout 65;
           types_hash_max_size 2048;
           client_max_body_size 20M;

           include /etc/nginx/mime.types;
           default_type application/octet-stream;

           include /etc/nginx/conf.d/*.conf;

           server {
               listen 80;
               server_name <tu-direccion-ip-publica>;

               location / {
                   proxy_pass http://127.0.0.1:8000;
                   proxy_set_header Host $host;
                   proxy_set_header X-Real-IP $remote_addr;
                   proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                   proxy_set_header X-Forwarded-Proto $scheme;
               }
           }
       }
       ```

   - Iniciar Nginx:

     ```sh
     sudo systemctl start nginx
     ```

   - Habilitar Nginx:

     ```sh
     sudo systemctl enable nginx
     ```

   - Recopilar archivos estáticos:

     ```sh
     python manage.py collectstatic
     ```

   - Servir la aplicación:

     ```sh
     gunicorn --bind 127.0.0.1:8000 moral_games.wsgi:application
     ```

   - Acceder a la aplicación en tu navegador:

     ```sh
     http://<tu-direccion-ip-publica>
     ```
