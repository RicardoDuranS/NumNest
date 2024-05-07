# NumNest
https://ricardodurans.github.io/NumNest/WEB/index.html

Este proyecto consiste en una página web interactiva diseñada para desplegar información sobre el progreso de los estudiantes en un juego educativo llamado "NumNest". El juego tiene como objetivo principal enseñar y reforzar conceptos matemáticos básicos en niños de entre 5 y 12 años.

## Características Principales
- Integración con Unity: El juego "Viaje Intermatemático", desarrollado en Unity, permite a los niños aprender matemáticas de manera interactiva y divertida.
- Base de Datos SQLite: Utiliza una base de datos SQLite para almacenar información sobre los usuarios (estudiantes y maestros), sus puntajes y su progreso en el juego.
- API Flask: Una API Flask alojada en PythonAnywhere se encarga de interactuar con la base de datos y proporcionar los datos necesarios para la página web.
- Despliegue de Información: La página web despliega los puntajes y el progreso de los estudiantes, permitiendo a los maestros y a los propios estudiantes realizar un seguimiento de su rendimiento en el juego.

## API Flask para Viaje Intermatemático
La API Flask desarrollada en Python es una parte fundamental del proyecto Viaje Intermatemático. Alojada en PythonAnywhere, esta API se encarga de gestionar una variedad de funciones para la página web, incluyendo autenticación de usuarios, obtención y actualización de información en la base de datos, y comunicación entre el juego de Unity y la página web.

### Funcionalidades Principales
1. Autenticación de Usuarios
La API Flask maneja la autenticación de usuarios, validando las credenciales proporcionadas por los estudiantes y maestros al iniciar sesión en la página web. Utiliza métodos de encriptación para garantizar la seguridad de la información de inicio de sesión.

2. Manipulación de Datos en la Base de Datos
Mediante métodos HTTP POST y GET, la API interactúa con la base de datos SQLite para realizar diversas operaciones, como:

    - Obtener puntajes y progreso de los estudiantes.
    - Actualizar puntajes y progreso de los estudiantes después de cada juego.
    - Registrar nuevos usuarios en la base de datos.
   
3. Arquitectura DAO
La API Flask está diseñada siguiendo la arquitectura de Acceso a Datos (DAO), lo que permite separar la lógica de negocio de la lógica de acceso a datos. Para lograr esto, se utiliza una clase ConnectionFactory para crear conexiones a la base de datos, y luego se implementan clases DAO (Data Access Object) para interactuar con la base de datos de manera modular y organizada. Estas clases DAO son invocadas por clases Controller, lo que facilita la separación de preocupaciones y la escalabilidad del código.

4. Comunicación con la Página Web y el Juego Unity
La API Flask se encarga de proporcionar los datos necesarios a la página web y al juego Unity, permitiendo una experiencia de usuario integrada y coherente. A través de solicitudes HTTP, la API envía información de puntajes y progreso a la página web, y recibe actualizaciones de puntajes del juego Unity para su registro en la base de datos.

Con la API Flask correctamente implementada, el proyecto Viaje Intermatemático puede ofrecer una experiencia educativa interactiva y efectiva para estudiantes y maestros, facilitando el aprendizaje y el seguimiento del progreso en matemáticas de una manera divertida y estimulante.
