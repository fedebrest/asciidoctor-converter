import os
import subprocess
import argparse
import sys
from pathlib import Path

def setup_directories():
    """Crea las carpetas de salida si no existen."""
    directories = ["documentos XML", "documentos PDF"]
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Directorio creado: {directory}")

def find_xsl_stylesheet():
    """Busca la ruta de la hoja de estilo DocBook XSL en el sistema."""
    linux_paths = [
        "/usr/share/xml/docbook/stylesheet/docbook-xsl-ns/fo/docbook.xsl",
        "/usr/share/xml/docbook/stylesheet/docbook-xsl/fo/docbook.xsl"
    ]
    if sys.platform.startswith("linux"):
        for path in linux_paths:
            if os.path.exists(path):
                return path
    return None

def run_command(command, description, env=None):
    """Ejecuta un comando de sistema y maneja errores."""
    print(f"Ejecutando: {description}...")
    try:
        # Usamos env para pasar variables como FOP_OPTS
        current_env = os.environ.copy()
        if env:
            current_env.update(env)
            
        result = subprocess.run(command, check=True, capture_output=True, text=True, env=current_env)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error en {description}:")
        print(e.stderr)
        return False
    except FileNotFoundError:
        print(f"Error: No se encontró el comando para '{description}'.")
        return False

def process_document(input_file):
    """Orquesta el flujo de Asciidoctor -> DocBook -> FOP PDF."""
    path_input = Path(input_file)
    if not path_input.exists():
        print(f"Error: El archivo {input_file} no existe.")
        return

    file_stem = path_input.stem
    xml_output = os.path.join("documentos XML", f"{file_stem}.xml")
    pdf_output = os.path.join("documentos PDF", f"{file_stem}.pdf")

    # 1. Asciidoctor -> DocBook
    adoc_to_xml = ["asciidoctor", "-b", "docbook5", "-o", xml_output, input_file]
    
    if run_command(adoc_to_xml, "Asciidoctor a DocBook XML"):
        xsl_path = find_xsl_stylesheet()
        
        # 2. DocBook XML -> FOP PDF
        xml_to_pdf = ["fop"]
        
        # CONFIGURACIÓN CRÍTICA PARA EL ERROR XPATH_LIMIT
        # Definimos variables de entorno para que Java ignore los límites de complejidad XPath
        # y aumentamos la memoria disponible.
        fop_env = {
            "FOP_OPTS": "-Djdk.xml.xpathExprGrpLimit=0 -Djdk.xml.xpathExprOpLimit=0 -Djdk.xml.xpathTotalOpLimit=0",
            "JAVA_OPTS": "-Djdk.xml.xpathExprGrpLimit=0 -Djdk.xml.xpathExprOpLimit=0 -Djdk.xml.xpathTotalOpLimit=0"
        }
        
        if xsl_path:
            print(f"Usando hoja de estilos: {xsl_path}")
            xml_to_pdf.extend(["-xml", xml_output, "-xsl", xsl_path, "-pdf", pdf_output])
        else:
            print("Advertencia: No se encontró la hoja de estilos local.")
            xml_to_pdf.extend(["-xml", xml_output, "-pdf", pdf_output])
        
        if run_command(xml_to_pdf, "DocBook XML a PDF (vía FOP)", env=fop_env):
            print("-" * 30)
            print(f"¡Éxito! Archivo PDF: {pdf_output}")
            print("-" * 30)

def main():
    parser = argparse.ArgumentParser(description="Automatización de Asciidoctor a PDF vía DocBook y FOP.")
    parser.add_argument("entrada", help="Ruta al archivo .adoc de Asciidoctor")
    args = parser.parse_args()
    setup_directories()
    process_document(args.entrada)

if __name__ == "__main__":
    main()
