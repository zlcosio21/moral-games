# Moral Games Web

Bienvenido a Moral Games Web, una tienda de videojuegos desarrollada con Django.

## Características principales

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

## Obtener los archivos estáticos

Antes de desplegar la aplicación en Heroku, asegúrate de recopilar los archivos estáticos necesarios. Ejecuta el siguiente comando:

```bash
python manage.py collectstatic
```

## Despliegue

A continuación, se detallan los pasos para desplegar Moral Games Web en un entorno de producción. 

## Despliegue en Heroku

Para desplegar Moral Games Web en Heroku, asegúrate de tener una cuenta en [Heroku](https://www.heroku.com/).

### Configuración previa:

1. **Crear una cuenta en Heroku:**
    - Si aún no tienes una cuenta, regístrate en [Heroku](https://signup.heroku.com/).

2. **Instalar el Heroku CLI:**
    - Descarga e instala el [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).

3. **Iniciar sesión en Heroku:**
    - Ejecuta el siguiente comando e ingresa tus credenciales:
      ```bash
      heroku login
      ```

### Despliegue:

1. **Crear una nueva aplicación en Heroku:**
    ```bash
    heroku create nombre-unico-de-tu-aplicacion
    ```

2. **Configurar variables de entorno:**
    - Configura las variables de entorno necesarias en tu aplicación Heroku utilizando el comando `heroku config:set`.

3. **Desplegar la aplicación:**
    ```bash
    git push heroku master
    ```

4. **Aplicar migraciones en Heroku:**
    ```bash
    heroku run python manage.py migrate
    ```

4. **Configurar la Base de Datos en Heroku::**
Utiliza el siguiente comando para agregar una base de datos PostgreSQL como add-on en Heroku:
    ```bash
    heroku addons:create heroku-postgresql:mini
    ```

5. **Abrir la aplicación en el navegador:**
    ```bash
    heroku open
    ```

6. **¡Listo!**

    Tu aplicación Moral Games Web ahora está desplegada en Heroku.
