from flask import Flask,jsonify,request
from flask_cors import CORS
import re
import xml.etree.ElementTree as ET
import base64
app= Flask(__name__)
CORS(app)

#@app.route("/grabarMensaje",methods=['POST'])
def file_upload():
    response={}
    xml = "\\prueba.xml"
    xml=request.json['xmlFile']
    xml_bytes = base64.b64decode(xml)
    xml_string=xml_bytes.decode('utf-8')
    root=ET.fromstring(xml_string)
    for mensaje_temporal in xml_string.findall('MENSAJE'):
        fecha_mensaje=fecha_mensaje.text
        texto_mensaje=texto_mensaje.text
        print("Mensaje",fecha_mensaje,'\n',texto_mensaje)
    response={
        "state":"perfect",
        "message":"El archivo fue leido con éxito"
    }
    return response

'''
if __name__=="__main__":
    app.run(threaded=True,port=5000,debug=True)


@app.route('/upload_file',methods=['POST'])
def upload_file():
    if 'file' not in request.files:
    return jsonify({
        "message": "No se ha enviado un archivo, intente de nuevo :("
    })
file = request.files['file']
file_contents=file.read().decode('utf-8')
print(file_contents)
return jsonify({
    "message": "El archivo fue cargado exitosamente y fue leido:)"
    })  
@app.route('/flask_response',methods=['GET'])
def get_response_from_flask():
    response_data={"message":"Mañana es feriado"}
    return jsonify(response_data)
@app.route('/flask_response2',methods=['GET'])
def get_response_from_flask2():
    response_data={"message":"Nos vemos del otro lado!"}
    return jsonify(response_data)
'''





