# NumNest
https://ricardodurans.github.io/NumNest/WEB/index.html

NumNest es un proyecto educativo diseñado para enseñar matemáticas básicas a niños de 5 a 12 años de edad de una manera interactiva y divertida. El proyecto consta de tres partes principales: un videojuego desarrollado en Unity, una página web interactiva y una API Flask que actúa como intermediario entre el videojuego y la página web, gestionando la base de datos y proporcionando funcionalidades clave.

## Funcionamiento del Proyecto

### Videojuego en Unity 
- El videojuego, denominado "Viaje Intermatemático", tiene como objetivo principal enseñar conceptos matemáticos básicos, así como figuras, volumen, áreas y perímetros. Utiliza una interfaz interactiva y amigable para involucrar a los niños en el aprendizaje.
- Conecta con una API Flask para validar usuarios y actualizar los puntajes de los usuarios a medida que avanzan en el juego, proporcionando así una retroalimentación instantánea sobre su progreso.

### Pagina Web
- La página web realiza operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en una base de datos a través de una API Flask, brindando a los usuarios una plataforma accesible para interactuar con el juego y su información.
 
- Permite a los usuarios descargar el juego de manera gratuita, facilitando su acceso y distribución.
  
- Para maestros, despliega información detallada sobre varios estudiantes, incluyendo datos estadísticos útiles para medir el progreso de los alumnos, como el tiempo dedicado al juego y los temas con los que tienen más dificultades. Además, proporciona la capacidad de modificar la información de los estudiantes para adaptarse a sus necesidades específicas.

- Para alumnos, ofrece estadísticas personalizadas sobre su propio progreso en el juego, lo que les permite identificar áreas de mejora y establecer metas educativas concretas.

### API Flask
- Actúa como intermediario entre el videojuego y la página web, gestionando todas las operaciones de la base de datos de manera eficiente y segura.

- Utiliza un modelo DAO (Data Access Object) para separar las responsabilidades y hacer el código más modular y mantenible, lo que facilita la escalabilidad y la incorporación de nuevas funcionalidades en el futuro.
  
- Proporciona funcionalidades de autenticación de usuarios, validación de puntajes y gestión de información tanto para el videojuego como para la página web, garantizando una experiencia de usuario fluida y coherente en todas las plataformas.

## Aprendizajes Relevantes
El desarrollo de NumNest ha proporcionado una serie de aprendizajes significativos en diversas áreas:

- Integración de Tecnologías: Aprender a integrar diferentes tecnologías, como Unity, Flask y SQLite, para construir una solución completa y funcional que aborde las necesidades educativas específicas del proyecto.

- Arquitectura DAO: Utilizar una arquitectura DAO ha demostrado ser una estrategia efectiva para separar las responsabilidades y mejorar la modularidad del código, lo que facilita su mantenimiento y extensión en el tiempo.

- API Development: Desarrollar una API Flask ha sido fundamental para facilitar la comunicación entre el videojuego, la página web y la base de datos, permitiendo una experiencia de usuario integrada y coherente que mejora la usabilidad y la eficacia del proyecto en su conjunto.

Este proyecto representa un esfuerzo colaborativo para crear una herramienta educativa innovadora que haga que el aprendizaje de las matemáticas sea más accesible y atractivo para los niños. La combinación de tecnologías y metodologías utilizadas ha permitido desarrollar una solución robusta, escalable y centrada en el usuario que tiene el potencial de impactar positivamente en la educación de los niños en todo el mundo.






