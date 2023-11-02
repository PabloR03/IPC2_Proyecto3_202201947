import xml.etree.ElementTree as ET
from flask import Flask,jsonify,request
from flask_cors import CORS
#importar mis archivos de clases
from BackEnd.Mensaje.MensajeDAO import MensajeDAO
from BackEnd.Sentimiento.SentimientoDAO import SentimientoDAO
import re

manejador_mensaje=MensajeDAO()
manejador_sentimiento=SentimientoDAO()

app= Flask(__name__)
CORS(app)

def encontrar_hashtag(cadena):
    hashtag = re.findall(r'#(.*?)#', cadena)
    return hashtag

def encontrar_usuario(cadena):
    usuario = re.findall(r'@(\w+)', cadena)
    return usuario

@app.route("/")
def index():
    return "<h1>Prueba Proyecto 3</h1>"

@app.route('/cargar/Mensajes',methods=['POST'])
def cargar_archivo_mensajes():
    if 'file' not in request.files:
        return jsonify({"Mensajes": "No se ha enviado un archivo."})
    archivo = request.files['file']
    contenido_xml=archivo.read().decode('utf-8')
    root = ET.fromstring(contenido_xml)
    for mensaje in root.findall(".//MENSAJE"):
        fecha = mensaje.find("FECHA").text
        texto = mensaje.find("TEXTO").text
        hashtag = encontrar_hashtag(texto)
        usuario = encontrar_usuario(texto)
        manejador_mensaje.nuevo_mensaje(fecha, usuario, hashtag, texto)
    #manejador_mensaje.imprimir_mensaje()
    manejador_mensaje.base_datos_mensaje()
    return jsonify({"message": "Archivo Mensajes Procesado"})

@app.route('/cargar/Configuracion', methods=['POST'])
def cargar_archivo_configuracion():
    if 'file' not in request.files:
        return jsonify({"Configuraciones": "No se ha enviado un archivo."})
    archivo = request.files['file']
    contenido_xml=archivo.read().decode('utf-8')
    root = ET.fromstring(contenido_xml)
    for sentimiento in root.findall(".//sentimientos_positivos/palabra"):
        manejador_sentimiento.nuevo_sentimiento_positivo(sentimiento.text.strip())
    for sentimiento in root.findall(".//sentimientos_negativos/palabra"):
        manejador_sentimiento.nuevo_sentimiento_negativo(sentimiento.text.strip())
    #manejador_sentimiento.imprimir_sentimiento()
    manejador_sentimiento.base_datos_configuracion()
    return jsonify({"message": "Archivo Configuraciones Procesado"})

@app.route('/consulta/Hashtag', methods=['GET'])
def consultar_hashtag():
    respuesta=manejador_mensaje.consultar_hashtag()
    return jsonify({"message": f"{respuesta}"})

@app.route('/consulta/Menciones', methods=['GET'])
def consultar_menciones():
    respuesta=manejador_mensaje.consultar_menciones()
    return jsonify({"message": f"{respuesta}"})

@app.route('/consulta/Sentimiento', methods=['GET'])
def consultar_sentimiento_mensaje():
    respuesta=manejador_sentimiento.consultar_sentimiento_mensaje(manejador_mensaje.lista_mensaje_fecha)
    return jsonify({"message": f"{respuesta}"})

@app.route('/grafica/Hashtag', methods=['GET'])
def grafica_consulta_hashtag():
    respuesta=manejador_mensaje.grafica_consular_hashtag()
    return jsonify({"message": f"{respuesta}"})

@app.route('/grafica/Menciones', methods=['GET'])
def grafica_consulta_menciones():
    respuesta=manejador_mensaje.grafica_consular_menciones()
    return jsonify({"message": f"{respuesta}"})

@app.route('/grafica/Sentimientos', methods=['GET'])
def grafica_consultar_sentimiento_mensaje():
    respuesta=manejador_sentimiento.grafica_sentimiento_mensaje(manejador_mensaje.lista_mensaje_fecha)
    return jsonify({"message": f"{respuesta}"})

@app.route('/limpiarSistema', methods=['POST'])
def resetear_datos():
    #Lista_Mensajes
    manejador_mensaje.resetear_datos_mensaje()
    #Lista_Sentimiento
    manejador_sentimiento.resetear_datos_sentimiento()
    manejador_mensaje.imprimir_mensaje()
    manejador_sentimiento.imprimir_sentimiento()
    return jsonify({"Resetar Datos": "Datos Reseteados Correctamente"})

@app.route('/informacion/Estudiante', methods=['GET'])
def informacion_estudiante():
    respuesta="PABLO ANDRES RODRIGUEZ LIMA"+"\n"+"202201947"+"\n"+"IPC2 - CUARTO SEMESTRE"+"\n"+"INGENIERIA EN CIENCIAS Y SISTEMAS"+"\n"+"SECCION D"
    return jsonify({"message": f"{respuesta}"})

if __name__=="__main__":
    app.run(threaded=True,port=5000,debug=True)