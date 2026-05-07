# Documentación: AsciiDoc a PDF

Este repositorio contiene un script de Python diseñado para automatizar la transformación de documentos técnicos. El flujo de trabajo es el siguiente:
`AsciiDoc (.adoc)` -> `DocBook XML` -> `PDF (usando Apache FOP)`.

## Requisitos Previos

Para que el script funcione, es indispensable que el sistema tenga instalados los motores de renderizado originales. El script de Python actúa como un puente (wrapper) entre estas herramientas.

### 1. Instalación de Dependencias de Sistema

#### **Windows**
1. **Asciidoctor**:
   - Instala [Ruby](https://rubyinstaller.org/).
   - En una terminal, ejecuta: `gem install asciidoctor`.
2. **Apache FOP**:
   - Descargar el binario desde [Apache FOP Project](https://xmlgraphics.apache.org/fop/download.html).
   - Descomprir el archivo y añadir la carpeta `bin` al **PATH de variables de entorno**.
   - Requiere Java (JRE) instalado.
3. **Python**: Se puede descargar desde python.org e instalarlo marcando "Add Python to PATH".

#### **macOS**
Usar [Homebrew](https://brew.sh/):
```bash
# Instalar Asciidoctor
brew install asciidoctor

# Instalar Apache FOP y Java
brew install fop
```

#### **Linux (Ubuntu/Debian)**
```bash
sudo apt update
# Instalar Asciidoctor
sudo apt install asciidoctor

# Instalar Apache FOP y Java
sudo apt install fop
```

---

## Instalación del Repositorio

1. Clonar este repositorio:
   ```bash
   git clone [https://github.com/tu-usuario/nombre-repo.git](https://github.com/tu-usuario/nombre-repo.git)
   cd nombre-repo
   ```
2. No se requieren librerías de terceros (pip), el script utiliza librerías estándar de Python 3.

---

## Cómo Ejecutar el Script

El script recibe como parámetro el archivo `.adoc` que se desea procesar.

### En Windows (PowerShell o CMD)
```powershell
python converter.py manual.adoc
```

### En macOS y Linux
```bash
python3 converter.py manual.adoc
```

### Resultados
Al finalizar la ejecución, el script generará automáticamente dos carpetas si no existen:
- `/documentos XML`: Contendrá el archivo intermedio en formato DocBook 5.0.
- `/documentos PDF`: Contendrá el archivo final listo para distribución.

---

## Solución de Problemas (Troubleshooting)

1. **Error: "No se encontró el comando"**: Asegurarse de que al escribir `fop -version` o `asciidoctor -v` en la terminal, se obtenga una respuesta. Si no, las herramientas no están correctamente instaladas o no están en el PATH.
2. **Error de Java**: Apache FOP necesita Java. Si se usa Linux o macOS, las dependencias suelen instalarse solas, en Windows asegurarse de tener instalado el JDK o JRE.
3. **Estilos PDF**: Por defecto, FOP utiliza estilos básicos. Para personalización avanzada, se requeriría pasar un archivo XSL de transformación adicional (DocBook XSL stylesheets), pero para conversiones estándar, el comando base es suficiente.
