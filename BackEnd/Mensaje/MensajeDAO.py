from BackEnd.Mensaje.Fecha_Mensaje import Fecha_Mensaje
from BackEnd.Mensaje.Contenido_Mensaje import Contenido_Mensaje
import xml.etree.ElementTree as ET
import os
def contar_hashtag(lista):
    # Crea un diccionario vacío para realizar el seguimiento de las cuentas de hashtag
    cuentas = {}
    # Recorre la lista de hashtags
    for hashtag in lista:
        # Si el hashtag ya está en el diccionario, incrementa su cuenta en 1
        if hashtag in cuentas:
            cuentas[hashtag] += 1
        else:
            # Si el hashtag no está en el diccionario, agrégalo con una cuenta de 1
            cuentas[hashtag] = 1
    return cuentas

def contar_usuarios(lista):
    # Crea un diccionario vacío para realizar el seguimiento de las cuentas de usuario
    cuentas = {}
    # Recorre la lista de usuarios
    for usuario in lista:
        # Si el usuario ya está en el diccionario, incrementa su cuenta en 1
        if usuario in cuentas:
            cuentas[usuario] += 1
        else:
            # Si el usuario no está en el diccionario, agrégalo con una cuenta de 1
            cuentas[usuario] = 1
    return cuentas

class MensajeDAO:
    def __init__(self):
        self.lista_mensaje_fecha=[]
    
    def nuevo_mensaje(self, fecha, usuario, hasthag, texto_mensaje):
        for fecha_mensaje in self.lista_mensaje_fecha:
            if fecha_mensaje.fecha==fecha:
                fecha_mensaje.lista_mensaje.append(Contenido_Mensaje(usuario, hasthag, texto_mensaje))
                return True
        lista_mensaje=[]
        lista_mensaje.append(Contenido_Mensaje(usuario, hasthag, texto_mensaje))
        nuevo_mensaje=Fecha_Mensaje(fecha, lista_mensaje)
        self.lista_mensaje_fecha.append(nuevo_mensaje)
        return True
    
    def imprimir_mensaje(self):
        print("+++++MENSAJES+++++")
        for fecha in self.lista_mensaje_fecha:
            print("---",fecha.fecha,"---")
            for mensaje in fecha.lista_mensaje:
                print(mensaje.usuario)
                print(mensaje.hashtag)
                print(mensaje.texto_mensaje)
        print("++++++++++++++++++")
    
    def resetear_datos_mensaje(self):
        self.lista_mensaje_fecha.clear()
    
    def consultar_hashtag(self):
        if len(self.lista_mensaje_fecha)==0:
            return "No Existen Archivos De Mensaje Procesados."
        lista_hashtag=[]
        respuesta=""
        for fecha in self.lista_mensaje_fecha:
            respuesta+="Fecha: "+fecha.fecha+"\n"
            for mensaje in fecha.lista_mensaje:
                for hashtag in mensaje.hashtag:
                    lista_hashtag.append(hashtag)
            consultar_hashtag=contar_hashtag(lista_hashtag)
            for hashtag, cuenta in consultar_hashtag.items():
                respuesta+=f"#{hashtag}#: {cuenta} mensajes."+"\n"
            lista_hashtag.clear()
            respuesta+="\n"
        return respuesta
    
    def grafica_consular_hashtag(self):
        if len(self.lista_mensaje_fecha)==0:
            return "No Existen Archivos De Mensaje Procesados."
        lista_hashtag=[]
        nombre_archivo = "Graficas\\Grafica_Hasthtag"
        f = open(nombre_archivo+'.dot','w')
        texto_g = """
            graph "" {bgcolor="white" gradientangle=90 label="Grafica Hashtag"
                fontname="Helvetica,Arial,sans-serif"
                node [fontname="Helvetica,Arial,sans-serif"]
                edge [fontname="Helvetica,Arial,sans-serif"]"""
        contador_nodo=1
        contador_subgrafo=1
        for fecha in self.lista_mensaje_fecha:
            fecha_mensaje="Fecha: "+fecha.fecha
            texto_g+= """subgraph cluster0"""+str(contador_subgrafo)+"""{label="""+f'"'+fecha_mensaje+f'"'+""" style="filled" gradientangle="270"\n"""
            contador_actual=contador_nodo
            contador_nodo+=1
            texto_g += """n00"""+str(contador_actual)+"""[fillcolor="white", style=filled, shape=square, label="""+f'"'+fecha.fecha+f'"'+"""];\n"""
            for mensaje in fecha.lista_mensaje:
                for hashtag in mensaje.hashtag:
                    lista_hashtag.append(hashtag)
            consultar_hashtag=contar_hashtag(lista_hashtag)
            for hashtag, cuenta in consultar_hashtag.items():
                texto_g += """n00"""+str(contador_nodo)+""" [fillcolor="white", style=filled, shape=square, label="""+f'"'+f"#{hashtag}#: {cuenta} mensajes."+f'"'+"""];\n"""
                texto_g += """n00"""+str(contador_actual)+ """--"""+ """n00"""+str(contador_nodo)+""" ;\n"""
                contador_nodo+=1
            lista_hashtag.clear()
            texto_g += """\n}\n"""
            contador_subgrafo+=1
            contador_nodo+=1
        texto_g += """\n}"""
        f.write(texto_g)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system(f'dot -Tpdf {nombre_archivo}.dot -o {nombre_archivo}.pdf')
        return "Grafica Hashtag Generada Correctamente"
    
    def base_datos_mensaje(self):
            mensajes_generales = ET.Element("BaseDataM")
            for fecha in self.lista_mensaje_fecha:
                mensaje = ET.SubElement(mensajes_generales, "Mensaje")
                fecha_ms = ET.SubElement(mensaje, "Fecha")
                fecha_ms.text = fecha.fecha
                for mensaje_fecha in fecha.lista_mensaje:
                    texto_ms = ET.SubElement(mensaje, "Texto")
                    texto_ms.text = mensaje_fecha.texto_mensaje
            datos=ET.tostring(mensajes_generales)
            datos=str(datos)
            self.xml_identado(mensajes_generales)
            arbol_xml=ET.ElementTree(mensajes_generales)
            arbol_xml.write("BackEnd/Bd/BaseDataM.xml",encoding="UTF-8",xml_declaration=True)

    def xml_identado(self, element, indent='  '):
        queue = [(0, element)]
        while queue:
            level, element = queue.pop(0)
            children = [(level + 1, child) for child in list(element)]
            if children:
                element.text = '\n' + indent * (level + 1)
            if queue:
                element.tail = '\n' + indent * queue[0][0]
            else:
                element.tail = '\n' + indent * (level - 1)
            queue[0:0] = children

    def consultar_menciones(self):
        if len(self.lista_mensaje_fecha)==0:
            return "No Existen Archivos De Mensaje Procesados."
        lista_usuario=[]
        respuesta=""
        for fecha in self.lista_mensaje_fecha:
            respuesta+="Fecha: "+fecha.fecha+"\n"
            for mensaje in fecha.lista_mensaje:
                for usuario in mensaje.usuario:
                    lista_usuario.append(usuario)
            consultar_menciones=contar_usuarios(lista_usuario)
            for usuario, cuenta in consultar_menciones.items():
                respuesta+=f"@{usuario}: {cuenta} mensajes."+"\n"
            lista_usuario.clear()
            respuesta+="\n"
        return respuesta

    def grafica_consular_menciones(self):
        if len(self.lista_mensaje_fecha)==0:
            return "No Existen Archivos De Mensaje Procesados."
        lista_usuario=[]
        nombre_archivo = "Graficas\\Grafica_Menciones"
        f = open(nombre_archivo+'.dot','w')
        texto_g = """
            graph "" {bgcolor="white" gradientangle=90 label="Grafica Menciones"
                fontname="Helvetica,Arial,sans-serif"
                node [fontname="Helvetica,Arial,sans-serif"]
                edge [fontname="Helvetica,Arial,sans-serif"]"""
        contador_nodo=1
        contador_subgrafo=1
        for fecha in self.lista_mensaje_fecha:
            fecha_mensaje="Fecha: "+fecha.fecha
            texto_g+= """subgraph cluster0"""+str(contador_subgrafo)+"""{label="""+f'"'+fecha_mensaje+f'"'+""" style="filled" gradientangle="270"\n"""
            contador_actual=contador_nodo
            contador_nodo+=1
            texto_g += """n00"""+str(contador_actual)+"""[fillcolor="white", style=filled, shape=square, label="""+f'"'+fecha.fecha+f'"'+"""];\n"""
            for mensaje in fecha.lista_mensaje:
                for usuario in mensaje.usuario:
                    lista_usuario.append(usuario)
            consultar_menciones=contar_usuarios(lista_usuario)
            for usuario, cuenta in consultar_menciones.items():
                texto_g += """n00"""+str(contador_nodo)+""" [fillcolor="white", style=filled, shape=square, label="""+f'"'+f"@{usuario}: {cuenta} mensajes."+f'"'+"""];\n"""
                texto_g += """n00"""+str(contador_actual)+ """--"""+ """n00"""+str(contador_nodo)+""" ;\n"""
                contador_nodo+=1
            lista_usuario.clear()
            texto_g += """\n}\n"""
            contador_subgrafo+=1
            contador_nodo+=1
        texto_g += """\n}"""
        f.write(texto_g)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system(f'dot -Tpdf {nombre_archivo}.dot -o {nombre_archivo}.pdf')
        return "Grafica Menciones Generada Correctamente"