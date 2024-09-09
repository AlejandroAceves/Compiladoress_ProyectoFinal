# Lenguaje y Compilador Especializados en Organización de Carpetas

## Resumen
Este proyecto consiste en el desarrollo de un lenguaje y un compilador especializados en la organización de archivos dentro de una carpeta seleccionada. La herramienta permite clasificar archivos por fecha de creación, tamaño, palabras en el nombre del archivo y tipo de archivo. Además, ofrece funciones para modificar carpetas mediante comandos como `move`, `delete`, `duplicate`, y `copy`.

## Motivación y Problema a Resolver

### Descripción del Problema
El proyecto busca enseñar a los usuarios, a través de un lenguaje sencillo, una nueva forma de organizar archivos en su dispositivo local, facilitando la gestión y manipulación de archivos sin la necesidad de conocimientos previos en programación.

### Importancia
En el ámbito laboral, muchas personas no saben utilizar terminales para organizar archivos debido a la complejidad del lenguaje y la falta de conocimientos en programación, lo que puede resultar en pérdida de tiempo en el manejo de archivos.

### Casos de Uso
La herramienta permitirá a los usuarios organizar archivos de manera más eficiente. Algunos casos de uso incluyen:
- Modificar la localización y cantidad de documentos disponibles (cambiando la posición en el directorio, eliminando, duplicando o copiando archivos).
- Organizar documentos dentro de una carpeta según las preferencias del usuario.

## Objetivos del Proyecto
- **Objetivo 1:** Mejorar la eficiencia en la organización y gestión de archivos.
- **Objetivo 2:** Proveer una herramienta accesible para usuarios sin experiencia en programación.
- **Objetivo 3:** Reducir el tiempo y esfuerzo dedicados a la gestión manual de archivos.
- **Objetivo 4:** Facilitar la implementación de operaciones complejas sobre archivos y carpetas con comandos simples.

## Comparación con Compiladores y Herramientas Similares

### Batch y Shell Scripts
Lenguajes de scripting como Batch en Windows y Shell (Bash) en Unix/Linux permiten automatizar la gestión de archivos a través de comandos como `move`, `copy`, `rm`, y `cp`. Son flexibles y ampliamente utilizados en entornos de desarrollo y administración de sistemas.

### PowerShell
PowerShell es una herramienta avanzada en Windows que permite la automatización de tareas administrativas, incluida la organización de archivos, utilizando comandos como `Move-Item`, `Remove-Item`, `Copy-Item`, y funciones avanzadas de scripting.

### Python
Python, con bibliotecas como `os` y `shutil`, permite escribir scripts para gestionar archivos y carpetas. Es un lenguaje versátil que puede ser utilizado para tareas complejas de organización y manipulación de archivos.

### Herramientas Automatizadas de Gestión de Archivos
Existen aplicaciones con interfaces gráficas para organizar archivos, como Hazel en macOS, que permite a los usuarios definir reglas para la clasificación automática de archivos. Sin embargo, estas herramientas suelen estar limitadas a plataformas específicas y no ofrecen la flexibilidad de un lenguaje de programación.

## Limitaciones de Soluciones Actuales
- **Curva de Aprendizaje Elevada:** Herramientas como Bash, PowerShell y Python requieren conocimientos de programación o scripting, lo que puede ser un obstáculo para usuarios no técnicos.
- **Falta de Simplicidad y Usabilidad:** Las soluciones existentes no están diseñadas específicamente para la organización de archivos de manera intuitiva.
- **Compatibilidad Limitada:** Muchas herramientas están restringidas a ciertos sistemas operativos o requieren software adicional.
- **Flexibilidad vs. Usabilidad:** Las herramientas con interfaces gráficas carecen de la flexibilidad necesaria para satisfacer necesidades específicas o complejas.

## Justificación del Nuevo Compilador
- **Accesibilidad para Usuarios No Técnicos:** Ofrecerá un lenguaje sencillo y accesible para la organización de archivos, reduciendo la barrera de entrada para usuarios sin conocimientos técnicos.
- **Enfoque Específico en la Organización de Archivos:** Diseñado específicamente para optimizar la experiencia del usuario en la gestión de archivos.
- **Multiplataforma y Fácil de Usar:** Compatible con múltiples sistemas operativos, priorizando la usabilidad y eliminando la necesidad de aprender comandos complejos.
- **Solución Flexible y Personalizable:** Proporciona suficiente flexibilidad para que los usuarios personalicen la organización de archivos según sus necesidades, permitiendo tanto tareas sencillas como operaciones avanzadas.

## Arquitectura y Diseño del Compilador
- **Diagrama de bloques:**
    - https://drive.google.com/file/d/1n5fFAuvSHq6quBxfa6XKAuDULbauceNO/view?usp=drive_link
    - https://www.canva.com/design/DAGP2JyK5CQ/OI_ijP0oY6DJ0F-oxyt2jQ/edit?utm_content=DAGP2JyK5CQ&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton 

- **Explicación del flujo de datos:**
    - Entrada del usuario: Comandos en lenguaje accesible.
    - Análisis léxico: Identificación de tokens.
    - Análisis sintáctico: Validación de la estructura de los comandos.
    - Análisis semántico: Comprobación del significado y contexto.
    - Generación de código intermedio: Creación de instrucciones abstractas.
    - Optimización: Mejora de la eficiencia de las operaciones.
    - Generación de código de máquina: Traducción a comandos específicos del sistema operativo.
    - Ejecución: Operaciones sobre los archivos.
    - Reporte: Retroalimentación sobre las operaciones realizadas.
- **Decisiones de diseño:**
Las decisiones de diseño para este proyecto pueden enfocarse en varios aspectos claves:
    - Lenguaje accesible: El lenguaje está diseñado para que usuarios no técnicos puedan utilizarlo fácilmente. Esto significa usar palabras clave simples y comandos claros, como move, delete, y sort, en lugar de complejas líneas de código.
    - Compatibilidad multiplataforma: Se tomó la decisión de diseñar el compilador de manera que funcione tanto en Windows como en Unix/Linux. Esto implica que la traducción de los comandos debe generar el código adecuado para cada sistema operativo.
    - Modularidad: El compilador estará estructurado de manera modular, con componentes independientes para cada fase del proceso (análisis léxico, análisis sintáctico, análisis semántico, etc.). Esto facilita la futura expansión del proyecto y la incorporación de nuevas características.
    - Simplicidad vs. Flexibilidad: Aunque el objetivo es crear un lenguaje accesible, también se consideró la necesidad de permitir operaciones avanzadas para usuarios más experimentados. Por lo tanto, el diseño del compilador permite que comandos simples se combinen o se configuren para realizar tareas más complejas.
    - Errores manejables: El sistema está diseñado para proporcionar mensajes de error claros y manejables para los usuarios. Por ejemplo, si un comando es malformado o una operación no es válida, el compilador brindará una sugerencia de corrección o describirá la causa del error. 
  Las decisiones de tokens para las diferentes funciones en el compilador son:
    - Identifier: `Organize`,`Modify`
    - OPERATOR: `+`,`-`,`=`
    - KEYWORDS: `Date`, `Size`, `Text`, `Move`, `Delete`, `Copy`, `filetype`
    - PUNCTUATORS: `/`, `.`, `;`
    
  ## Análisis Léxico
- **Análisis léxico:** 
    - Tokenización, identificación de palabras clave, operadores, etc.
    Las decisiones de tokens para las diferentes funciones en el compilador son:
    - IDENTIFIERS: `organize`,`modify`
    - OPERATOR: `+`,`-`,`=`
    - KEYWORDS: `date`, `size`, `text`, `move`, `delete`, `copy`, `filetype`
    - PUNCTUATORS: `/`, `.`, `;`
Palabras clave: Estas son las palabras reservadas del lenguaje que indican acciones o categorías importantes. Por ejemplo:
    move: Mover archivos de un lugar a otro.
    delete: Eliminar archivos.
    copy: Copiar archivos a otra ubicación.
    duplicate: Duplicar un archivo en el mismo directorio o en otro.
Tipos de archivo: El compilador debe reconocer las extensiones de archivos como:
    .jpg, .pdf, .txt, etc.
Puntuación: El compilador utiliza signos de puntuación para indicar principio o fin de ciertos comandos.
    ; (indica el fin de un comando).
    : (indica el inicio de la dirección de un archivo).
    . (indica el inicio de la extensión de un archivo).
    Identificación de tokens / palabras clave / operadores / etc:
    -Autómata y programa disponible en el repositorio
