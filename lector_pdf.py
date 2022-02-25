
## Lector de textos en pdf ##

# importamos librerias
from mimetypes import init
import PyPDF2
import pyttsx3

# Cargamos el archivo pdf
libro=open('archivo.pdf', 'rb')
lector=PyPDF2.PdfFileReader(libro)

# creamos una instancia de voz, cargamos la pagina del texto en pdf y extraemos su texto
# numero_pagina corresponde a la página del libro que queremos tranformar a voz 
voz=pyttsx3.init()
pagina=lector.getPage(#numero_pagina)
texto=pagina.extractText()

# cargams el texto para que voz.say lo reproduzca en voz 
voz.setProperty('rate', 140)
voz.say(texto)
voz.runAndWait()



if __name__ == '__main__':