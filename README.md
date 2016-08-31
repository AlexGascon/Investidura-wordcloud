# Investidura-wordcloud
Script que genera una nube de tags a partir de los discursos realizados por los líderes de los distintos políticos en la sesión de investidura de Mariano Rajoy del 31 de Agosto de 2016

Para ello, debe proporcionarse un fichero PDF del que se extraerá el texto. Después, realiza un pequeño procesado que incluye conversión a ASCII, eliminación de carácteres no alfabéticos (comas, exclamaciones, guiones...), pasa todo a minúsculas y descarta todas aquellas palabras de menos de 4 carácteres.


# Ejemplos: 

## Discurso de Mariano Rajoy
![Wordcloud Rajoy](https://github.com/AlexGascon/Investidura-wordcloud/blob/master/result/Rajoy_wordcloud.bmp)

## Discurso de Pedro Sánchez
![Wordcloud Sanchez](https://github.com/AlexGascon/Investidura-wordcloud/blob/master/result/Sanchez_wordcloud.bmp)


Para generar el Wordcloud se utiliza la librería [word_cloud](https://github.com/amueller/word_cloud).
