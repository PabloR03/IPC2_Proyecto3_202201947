import xml.etree.ElementTree as ET

def parse_xml_file(file_path):
    messages = []
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        for mensaje_temporal in root.findall('.//MENSAJE'):
            fecha_mensaje = mensaje_temporal.find('FECHA').text
            texto_mensaje = mensaje_temporal.find('TEXTO').text
            messages.append({
                "FECHA": fecha_mensaje,
                "TEXTO": texto_mensaje
            })
    except Exception as e:
        print(f"Error al analizar el archivo: {e}")

    return messages

# Llamada a la función con la ruta de tu archivo XML
file_path = "aqui va el link del archivo de entrada"
messages = parse_xml_file(file_path)

# Imprimir la lista de mensajes
for message in messages:
    print("FECHA:", message["FECHA"])
    print("TEXTO:", message["TEXTO"])
    print()
