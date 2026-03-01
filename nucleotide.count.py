# Hardcoded sequence
dna_sequence = " at gc "

# Limpieza
dna_sequence = dna_sequence.strip()
dna_sequence = dna_sequence.replace(" ", "") #Comando proporcionado por la IA
dna_sequence = dna_sequence.upper()

# Verificación de caracteres no válidos
# Verificación de caracteres válidos
valid_nucleotides = set("ATGC")
invalid_chars = set(dna_sequence) - valid_nucleotides

if invalid_chars:
    print(f"Caracteres inválidos detectados: {invalid_chars}")
else:
    print("Secuencia válida")


# Conteos
count_a = dna_sequence.count("A")
count_t = dna_sequence.count("T")
count_g = dna_sequence.count("G")
count_c = dna_sequence.count("C")
print(f"count A:", count_a)
print(f"count T:", count_t)
print(f"count G:", count_g)
print(f"count C:", count_c)

# Longitud
length = len(dna_sequence)
print(f"Length:", length) 