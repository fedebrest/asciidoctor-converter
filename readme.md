🚀 AsciiDoc to PDF Pipeline

Este repositorio proporciona un orquestador automatizado en Python para transformar documentos técnicos escritos en AsciiDoc a formato PDF con calidad profesional, utilizando el estándar DocBook XML y Apache FOP.

A diferencia de otros convertidores simples, este flujo permite un control total sobre la estructura semántica y el diseño final mediante hojas de estilo XSL.

🛠️ Requisitos de Sistema

Para que el script funcione, necesitas instalar las siguientes herramientas. El script de Python actúa como un puente entre ellas.

🐧 Linux (Ubuntu/Debian)

Es la plataforma más sencilla de configurar. Ejecuta el siguiente comando para instalar todo, incluyendo las hojas de estilo necesarias para evitar errores de transformación:

sudo apt update
sudo apt install -y asciidoctor fop docbook-xsl-ns python3


Nota Crítica: El paquete docbook-xsl-ns es indispensable para que FOP sepa cómo convertir los elementos XML en formato visual para el PDF.

🍏 macOS

Utilizando Homebrew:

brew install asciidoctor fop docbook-xsl


🪟 Windows

Python: Descárgalo de python.org.

Asciidoctor:

Instala Ruby.

Ejecuta en la terminal: gem install asciidoctor.

Apache FOP:

Descarga el binario de Apache FOP.

Descomprime y añade la carpeta /bin a tus Variables de Entorno (PATH).

Hojas de Estilo XSL (Indispensable):

Descarga las DocBook XSL Stylesheets.

Extrae los archivos y asegúrate de que la ruta coincida con la configurada en converter.py.

📦 Instalación del Proyecto

Clona este repositorio en tu máquina local:

git clone https://github.com/tu-usuario/nombre-del-repo.git
cd nombre-del-repo


El script utiliza únicamente la librería estándar de Python (subprocess, argparse, pathlib), por lo que no requiere instalar librerías adicionales con pip.

🚀 Guía de Uso Paso a Paso

1. Preparar el archivo

Asegúrate de tener tu archivo .adoc listo (por ejemplo, prueba.adoc) en la carpeta del proyecto.

2. Ejecutar el script

Abre tu terminal en la carpeta del proyecto y ejecuta:

En Linux/macOS:

python3 converter.py prueba.adoc


En Windows:

python converter.py prueba.adoc


3. ¿Qué hace el script internamente?

Validación: Comprueba que el archivo de entrada existe.

Organización: Crea automáticamente las carpetas /documentos XML y /documentos PDF.

Generación XML: Llama a asciidoctor para crear un archivo DocBook 5.

Búsqueda XSL: Localiza las hojas de estilo en el sistema para dar formato al documento.

Renderizado PDF: Llama a fop para unir el XML y el XSL en el PDF final.

📂 Estructura de Salida

documentos XML/ ➡️ Contiene el archivo .xml intermedio (útil para depuración técnica).

documentos PDF/ ➡️ Contiene tu documento final listo para distribuir.

💡 Solución de Problemas Comunes

Error: "XSLT file must be specified": Este error ocurre si no tienes instalado el paquete docbook-xsl-ns. Revisa la sección de requisitos de Linux arriba.

Comando no encontrado: Verifica que tanto fop como asciidoctor estén en tu variable de entorno PATH. Prueba ejecutando fop -version en la terminal.

Caracteres especiales: Asegúrate de que tus archivos .adoc estén guardados con codificación UTF-8.

Desarrollado para entusiastas de la Documentación como Código (Docs-as-Code).
