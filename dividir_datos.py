import splitfolders
import sys

# 2. Configurar rutas
# Carpeta donde están tus fotos ahora (por ejemplo, con subcarpetas 'gatos' y 'perros')
input_folder = sys.argv[1]

# Carpeta donde quieres el resultado ordenado
output_folder = sys.argv[2]

if (sys.argv[1] == None) or (sys.argv[2] == None):
    print("Error: Debes proporcionar las rutas de entrada y salida.")
    print("Uso: python dividir_datos.py <ruta_entrada> <ruta_salida>")
    sys.exit(1)

input_train = float(input("Porcentaje de entrenamiento: "))
input_val = float(input("Porcentaje de validación: "))
input_test = float(input("Porcentaje de prueba: "))

if (input_train + input_val + input_test) != 100:
    print("Error: La suma de los porcentajes debe ser 100.")
    sys.exit(1)
elif (input_train < 0) or (input_val < 0) or (input_test < 0):
    print("Error: Los porcentajes no pueden ser negativos.")
    sys.exit(1)

# 3. Dividir (ratio=(train, validation, test))
splitfolders.ratio(input_folder, output=output_folder, 
                   seed=42, ratio=(input_train/100, input_val/100, input_test/100), group_prefix=True)

print(f"¡Listo! Revisa la carpeta {output_folder} para ver los datos divididos.")