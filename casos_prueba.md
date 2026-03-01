### 🧪 Casos de prueba manuales

| Entrada        | Resultado esperado                  |
|---------------|-------------------------------------|
| "ATGC"        | A=1, T=1, G=1, C=1, longitud=4      |
| "aaaa"        | A=4, longitud=4                     |
| " at gc "     | A=1, T=1, G=1, C=1, longitud=4      |
| ""            | longitud=0                          |

### ✅ Resultados (completa al correr el programa)

- Caso 1 ("ATGC"):
  - Obtuve: 
count A: 1
count T: 1
count G: 1
count C: 1
Length: 4
  - ¿Coincide? Sí 

- Caso 2 ("aaaa"):
  - Obtuve:
count A: 4
count T: 0
count G: 0
count C: 0
Length: 4
  - ¿Coincide? Sí

- Caso 3 (" at gc "):
  - Obtuve: 
count A: 1
count T: 1
count G: 1
count C: 1
Length: 5
  - ¿Coincide? No (length es de 5 y debería ser 4)

- Caso 4 (""):
  - Obtuve:
count A: 0
count T: 0
count G: 0
count C: 0
Length: 0
  - ¿Coincide? Sí