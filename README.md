# Proyecto final de organización computacional

**Profesores:**

* Yolanda Cham Yuen

* Diego David Avalos de la Torre

**Integrantes:**

* Hermes Espínola González (A01631677)

* Andés Barro Encinas (A00226225)

![Tec logo](http://sitios.itesm.mx/identidad/img/logotipo/secundario.jpg)

## Objetivo del dispositivo

Estimular la coordinación visomotora ojo-mano en niños de corta edad (de 3 a 8 años) mediante el reconocimiento de figuras y colores llamativos así como su asociación con distintos movimientos y acciones, además de ayudarlo a familiarizarse con interfaces comunes para la interacción con dispositivos electrónicos.

## Introducción

### ¿Qué es?

Es un juego destinado a niños de corta edad que tiene como objetivo la estimulación de la coordinación visomotora ojo-mano. El juego es una caja con diferentes colores en cada lado de la carcasa, en donde se puede encontrar un botón, una perilla, un touch o un micrófono, junto con una figura que sirve como indicio de la acción que se tiene que realizar con cada lado. En cara superior de la caja se encuentra un display led que cambia de color para indicar la acción a realizar, junto a un botón para reiniciar el juego.

### ¿Quién o quienes lo construyeron?

El juego fue diseñado, construido y programado por Hermes Espínola González y Andrés Barro Encinas.

### ¿Cuál es el objetivo del dispositivo?

Estimular la coordinación visomotora ojo-mano en niños de corta edad (de 3 a 8 años) mediante el reconocimiento de figuras y colores llamativos así como su asociación con distintos movimientos y acciones, además de ayudarlo a familiarizarse con interfaces comunes para la interacción con dispositivos electrónicos.

### ¿Cómo es el funcionamiento del dispositivo?

El juego consiste en sensores conectados a una Edison, que ejecuta el juego automáticamente cuando es encendida, cuando el juego empieza se hace un ajuste al micrófono dependiendo del ruido del ambiente.

Después empieza el juego mostrando al niño un color en la pantalla lcd y texto que dice que tiene que hacer y su puntaje (para los niños que sepan leer, más no afecta en el juego). Entonces el niño relaciona el color en la pantalla con un lado del juguete y una imagen en ese lado del juguete con una acción, la cual tendrá que realizar con el sensor que se encuentre en dicho lado del juguete. Si el niño acierta se suman puntos, se reproduce un sonido como retroalimentación y cambia el color de la pantalla. Si el niño no asienta, se reproduce un sonido diferente (dos beeps) para darle a entender que se requiere de una acción diferente y espera a que realice la correcta. Mediante la retroalimentación se ayuda al niño a relacionar los colores y acciones necesarias para asegurarse que la coordinación ojo-mano se está desarrollando correctamente.

## Desarrollo

### Lista de componentes y elementos empleados

* Intel Edison Development Board

* Base Shield v2

* Buzzer

* Botones x 2

* Potenciómetro

* Sensor de sonido

* Sensor touch

* Pantalla LCD RGB Backlight

* Caja de plástico steren

### Código

El código fuente del juego se encuentra en [https://github.com/hermesespinola/PopGame](https://github.com/hermesespinola/PopGame).

### Análisis, diseño, esquema circuito y conexiones

Se optó por utilizar una interfaz independiente de una computadora porque deseábamos que el niño fuera capaz de mover el dispositivo libremente y mantener su concentración en el mismo dispositivo. La forma cuadrada es debido a que con esta forma es fácil de introducir y afianzar todos los componentes dentro de la carcasa, además de que es una figura fácil de sostener con firmeza.

Se utilizó colores fácilmente distinguibles entre sí en la caja y en la pantalla para crear una fácil asociación visual entre las diferentes caras del juguete. Cada lado de la caja tiene una imagen o figura que funciona como indicio de qué acción se debe realizar. Así se crea una relación de color a un espacio físico en el juguete y de una imagen en este espacio a una acción. El objetivo de este diseño es crear una cadena de relaciones visomotrices que apoyen a los niños de corta edad a desarrollar sus habilidades.

Las conexiones son realmente simples gracias al shield que se conectó sobre la placa, permite conectar los sensores y la pantalla mediante conectores Grove. Con estos conectores no se tuvo que diseñar ningún circuito para el juguete, simplemente se conectan y están listos para utilizarse desde el código mediante una librería para leer y escribir mediante los conectores Grove. Los botones, sensores touch y el buzzer se conectaron a entradas/salidas digitales, el potenciómetro y el sensor de sonido se conectaron a entradas analógicas y la pantalla se conectó a al Grove para comunicación I2C.

### Bitácora de desarrollo

Todos los avances del proyecto, desde ideas iniciales, desarrollo, muestras en video, fotos y conclusiones están registradas de forma cronológica en el siguiente blog: [http://www.pop-game.tumblr.com](http://www.pop-game.tumblr.com).

## Conclusiones

### Conocimientos, técnicas y metodologías

1. Conocimientos:

    * Aplicamos conocimientos sobre microcontroladores, sensores y circuitos, además también se aplicaron conocimientos sobre el Linux y programación orientada a objetos.

2. Técnicas:

    * Aplicamos la técnica de diseño de la caja de cristal.

        1. Éramos conscientes de cada paso que dábamos en el desarrollo del proyecto y tenía una explicación lógica.

        2. Identificamos objetivos, variables y criterios.

        3. Primero analizamos el problema, después buscamos una solución, la validamos y comenzamos a desarrollarla.

3. Metodología:

    * Utilizamos la metodología Megon:

        4. Identificamos y definimos la problemática del usuario.

        5. Planificamos el sistema para la solución.

        6. Analizamos los requisitos de la solución propuesta.

        7. Implementamos la solución propuesta.

        8. Mejoramos la solución y corregimos errores.

        9. La solución es entregada.

### Análisis final

El desarrollo de la solución fué satisfactoria y dieron buenos resultados, se probó el producto final para validar su funcionamiento, funciona correctamente y el diseño cumple con su objetivo, los usuarios identifican los colores y las imágenes con las acciones a realizar. La elección de utilizar conexiones Grove fue acertada, pues la conexiones se mantienen aún cuando la caja es agitada.

### Observaciones

Nos dimos cuenta de que la caja cúbica no es la mejor opción para un juguete que se tiene que sostener, se tiene que desarrollar una interfaz más ergonómica y con un tamaño acorde a las manos de los niños pequeños. Podemos notar también que los sensores y los botones no son completamente amigables para los usuarios, debido a que no son llamativos y hasta podrían considerarse feos. Para ser un prototipo consideramos que estos son problemas menores y no afectan al funcionamiento del producto.

### Conclusiones

Durante el proyecto aprendimos sobre la terminal de Linux, sobre microcontroladores y sobre diferentes interfaces para conectar sensores y dispositivos al shield. Pero sobre todo, desarrollamos un proyecto de manera organizada utilizando la metodología Megon, fuimos capaces de identificar problemáticas, proponer una solución viable y desarrollar el proyecto de tal forma que el resultado final puede tener un impacto benéfico en la problemática que se identificó.
