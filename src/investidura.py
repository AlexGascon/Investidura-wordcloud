# -*- coding: utf-8 -*-
from wordcloud import WordCloud
import PyPDF2
import unicodedata
import re
import numpy as np
from PIL import Image


generic_PDF = "D:\Python projects\Investidura wordcloud\PDF\{}.pdf"
generic_output = "D:\Python projects\Investidura wordcloud\\result\{}_wordcloud.bmp"

#Array con los filename de todos los archivos a analizar
politicos = ["Rajoy", "Sanchez"]

for politico in politicos:

	#Obtenemos los nombres de los archivos que necesitaremos
	discurso = generic_PDF.format(politico)
	resultado = generic_output.format(politico)
	
	#PARTE 1: PROCESADO DEL TEXTO
	#Abrimos el discurso
	pdf = PyPDF2.PdfFileReader(open(discurso, "rb"))

	#Extraemos el texto
	text = ""
	for page in pdf.pages:
		text = text + page.extractText()

	#Eliminamos los carácteres no unicode
	text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore')

	#Eliminamos carácteres no alfabéticos
	regex = re.compile('[^a-zA-Z ]')
	text = regex.sub("", text)

	#Pasamos todo a minúsculas
	text = text.lower()

	#Eliminamos las palabras cortas (menos de 4 letras)
	pattern = r"\b\w{1,4}\b"
	text = re.sub(pattern, "", text)


	#PARTE 2: CREACIÓN DEL WORDCLOUD
	#Utilizamos el Congreso como máscara
	mask_filename = "D:\Python projects\Investidura wordcloud\img\government-mask.jpg"
	mask = np.array(Image.open(mask_filename))

	#Instanciamos el objeto WordCloud
	wc = WordCloud(background_color = "white", mask = mask)
	#Generamos el wordcloud
	wc.generate(text)
	im = wc.to_image()

	outname = generic_output.format(politico)
	im.save(outname)
