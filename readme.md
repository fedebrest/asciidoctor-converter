# 🚀 AsciiDoc to PDF Pipeline

Este repositorio proporciona un orquestador automatizado en Python para transformar documentos técnicos escritos en AsciiDoc a formato PDF con calidad profesional, utilizando el estándar DocBook XML y Apache FOP.

A diferencia de otros convertidores simples, este flujo permite un control total sobre la estructura semántica y el diseño final mediante hojas de estilo XSL.

## 🛠️ Requisitos de Sistema

Para que el script funcione, necesitas instalar las siguientes herramientas. El script de Python actúa como un puente entre ellas.

#### **🐧 Linux (Ubuntu/Debian)**

Es la plataforma más sencilla de configurar. Ejecuta el siguiente comando para instalar todo, incluyendo las hojas de estilo necesarias para evitar errores de transformación:

```bash
sudo apt update
sudo apt install -y asciidoctor fop docbook-xsl-ns libxalan2-java libxerces2-java python3
```

**Notas**: 
* Las librerías ```libxalan2-java``` y ```libxerces2-java``` son necesarias para que FOP procese correctamente las hojas de estilo complejas de DocBook.
* El paquete ```docbook-xsl-ns``` es indispensable para que FOP sepa cómo convertir los elementos XML en formato visual para el PDF.

#### **🍏 macOS**

Utilizando [Homebrew](https://brew.sh):

```bash
brew install asciidoctor fop docbook-xsl
```

#### **🪟 Windows**

**1. Python**: Descargar desde [python.org](https://www.python.org/).

**2. Asciidoctor**:

* Instalar [Ruby](https://rubyinstaller.org/).

* Ejecutar en la terminal: 
```bash
gem install asciidoctor
```

**3. Apache FOP y Java**:

* Descargar e instalar el [JRE de Java](https://www.java.com/es/)

* Descargar el binario de [Apache FOP](https://xmlgraphics.apache.org/fop/download.html) y añadir la carpeta ```/bin``` al  PATH.

**4. Hojas de Estilo XSL (Indispensable)**:

* Descargar las [DocBook XSL Stylesheets](https://sourceforge.net/projects/docbook/files/docbook-xsl-ns/).

* Extraer los archivos y asegurarse de que la ruta coincida con la configurada en converter.py.

#### **📦 Instalación del Proyecto**

Clonar este repositorio en la máquina local:

```bash
git clone https://github.com/tu-usuario/nombre-del-repo.git
cd nombre-del-repo
```

El script utiliza únicamente la librería estándar de Python (```subprocess```, ```argparse```, ```pathlib```), por lo que *no requiere instalar librerías adicionales con pip*.

#### **🚀 Guía de Uso Paso a Paso**


##### **1. Preparar el archivo**

Asegurarse de tener el archivo ```.adoc``` listo (por ejemplo, ```prueba.adoc```) en la carpeta del proyecto.

##### **2. Ejecutar el script**

Abrir la terminal en la carpeta del proyecto y ejecutar:

**En Linux/macOS**:

```bash
python3 converter.py prueba.adoc
```

**En Windows:**:

```bash
python converter.py prueba.adoc
```

##### **3. ¿Qué hace el script internamente?**

**1. Validación:** Comprueba que el archivo de entrada existe.

**2. Organización:** Crea automáticamente las carpetas ```/documentos XML``` y ```/documentos PDF```.

**3. Generación XML:** Llama a ```sciidoctor``` para crear un archivo DocBook 5.

**4. Búsqueda XSL:** Localiza las hojas de estilo en el sistema para dar formato al documento.

**5. Renderizado PDF:** Llama a ```fop``` para unir el XML y el XSL en el PDF final.

**6. XPATH_LIMIT:** El script inyecta variables de entorno ```(FOP_OPTS)``` para desactivar los límites de recursividad de Java en expresiones XPath complejas.

**7. XSLT Lookup:** Localiza automáticamente las hojas de estilo en rutas estándar de Linux.

**8. Java Memory:** Optimizado para manejar documentos de gran tamaño sin desbordar la memoria.

#### **📂 Estructura de Salida**

* ```documentos XML/``` ➡️ Contiene el archivo ```.xml``` intermedio (útil para depuración técnica).

* ```documentos PDF/``` ➡️ Contiene tu documento final listo para distribuir.

#### **💡 Solución de Problemas Comunes**

* Error: "XSLT file must be specified": Este error ocurre si se tiene instalado el paquete ```docbook-xsl-ns``` . Revisar la sección de requisitos de Linux arriba.

* Comando no encontrado: Verificar que tanto ```fop``` como ```asciidoctor``` estén en la variable de entorno PATH. Probar ejecutando ```fop -version``` en la terminal.

* Caracteres especiales: Asegurarse de que los archivos ```.adoc``` estén guardados con codificación UTF-8.
