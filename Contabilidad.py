#Precio neto
#Total precio sin IVA, Refleja los impuestos

# Mi funcion
def precioIVA (IVA,precio_neto):
    resultado2 = precio_neto * IVA
    return resultado2

def precioNeto (porcentaje,precio_bruto):
    resultado = precio_bruto/porcentaje
    return resultado

# Ejemplo
# Datos del productos botella de agua
precio_bruto = 5
porcentaje = 1.12
precio_neto = precioNeto (porcentaje,precio_bruto)

# Ejemplo
# Datos de una pizza grande
precio_bruto = 100
porcentaje = 1.12
IVA = 0.12
precio_neto = precioNeto (porcentaje, precio_bruto) 
IVA_total = precioIVA(IVA,precio_neto)
print(f"Nombre del producto: Pizza,  precio bruto:  Q{precio_bruto},  precio neto:  Q{precio_neto},  Impuesto IVA:  Q{IVA_total}")