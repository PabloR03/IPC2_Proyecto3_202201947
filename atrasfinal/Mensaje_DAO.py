from Mensajes import Mensaje
def Obtener_Hashtag(self, text):
    cadena="""sdfsd f#sisa le#dsfd
        sf"""
    buffer=""
    buffer2=""
    state=0
    for c in cadena:
        if state==0:
            if c=="#":
                #aqui empieza un hashtag
                buffer+=c
                state=1
                continue
        if state==1:
            if c!="#":
                buffer+=c
                continue
            else:
                buffer+=c
                print("Llegamos al final del hashtag:", buffer)
                state=0
                continue
    print(buffer)