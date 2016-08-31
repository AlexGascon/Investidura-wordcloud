# Investidura-wordcloud
Script que genera una nube de palabras a partir de los discursos realizados por los líderes de los distintos políticos en la sesión de investidura de Mariano Rajoy del 31 de Agosto de 2016

Para ello, debe proporcionarse un fichero PDF del que se extraerá el texto. Después, realiza un pequeño procesado que incluye conversión a ASCII, eliminación de carácteres no alfabéticos (comas, exclamaciones, guiones...), pasa todo a minúsculas y descarta todas aquellas palabras de menos de 4 carácteres.

Tras esto, generamos la nube de palabras dándole forma de la fachada del Congreso de los Diputados y lo guardamos como una imagen en la carpeta results

# Ejemplos: 

## Discurso de Mariano Rajoy
![Wordcloud Rajoy](https://github.com/AlexGascon/Investidura-wordcloud/blob/master/result/rajoy_combinado.jpg)

## Discurso de Pedro Sánchez
![Wordcloud Sanchez](https://github.com/AlexGascon/Investidura-wordcloud/blob/master/result/sanchez_combinado.jpg)


Para generar el Wordcloud se utiliza la librería [word_cloud](https://github.com/amueller/word_cloud).
