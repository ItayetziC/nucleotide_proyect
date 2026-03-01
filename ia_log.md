## Interacción 1
Modo: ASK
Pregunta: Me gustaría saber cómo puedo agregar al proyecto anexado una verificación para poder mandarme un mensaje de advertencia si hay caracteres distintos de A, T, G o C, por ejemplo, espacios innecesarios.
Aprendí: que para la verificación, es necesario determinar cuales son los nucleotidos validos 
para saber si hay inválidos 
invalid_chars: 
set(dna_sequence) - valid_nucleotide 
y después realizar una condición donde si invalid_chars es diferente de 0, mandar una advertencia con cuántos carácteres distintos a A, T, G y C. 
## Interacción 2
Modo: ASK
Pregunta: De que forma puedo eliminar los espacios vacios que se encuentran dentro de un string?
Aprendí: Que hay un comando que se puede remplazar un caracter por otro, sería como 
var.replace(" ", "")