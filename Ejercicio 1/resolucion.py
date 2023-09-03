sueldo_enero_a_junio = 300 * 6
sueldo_julio_a_octubre = 500 * 4
sueldo_noviembre_diciembre = 700 * 2

sueldo_total = sueldo_enero_a_junio + sueldo_julio_a_octubre + sueldo_noviembre_diciembre

sueldo_promedio = sueldo_total / 12

if sueldo_promedio < 300:
    categoria = "Sueldo bajo"
elif 300 <= sueldo_promedio <= 900:
    categoria = "Sueldo normal"
else:
    categoria = "Sueldo mejor de lo normal"

print(f"Sueldo promedio de Juan: {sueldo_promedio} dólares")
print(f"Categoría de sueldo: {categoria}")
