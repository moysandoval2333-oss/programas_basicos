def calcular_salario_neto(bruto, porcentaje_imp, deduc):
    impuestos = bruto * (porcentaje_imp / 100)
    return bruto - impuestos - deduc

salario_bruto = float(input("Salario bruto: "))
tasa_impuesto = float(input("Porcentaje de impuestos: "))
otras_deducciones = float(input("Otras deducciones: "))

resultado = calcular_salario_neto(salario_bruto, tasa_impuesto, otras_deducciones)
print(f"Salario neto: ${resultado:.2f}")
