# Presupuesto para sueldo

# Guarda los valores de cada ingreso

peya = 0
bk = 1000000
sueldo = bk + peya

# La funcion para calcular y mostrar el presupuesto

def calcular_presupuesto(sueldo):
    print(f"Saldo Total : ${sueldo:,}\n--------------")
    gastos_fijos = round(sueldo * 0.55)
    gastos_libres = round(sueldo * 0.15)
    educacion = round(sueldo * 0.10)
    ahorro = round(sueldo * 0.10)
    inversion = round(sueldo * 0.10)
    division_cuentas = educacion + ahorro + inversion + gastos_libres

    print(f"Gastos fijos - ${gastos_fijos:,}\nEducación - ${educacion:,}\nDiversion - ${gastos_libres:,}\nAhorros - ${ahorro:,}\nInversión - ${inversion:,}")
    #print(f"Gastos fijos = ${gastos_fijos:,}")
    #print(f"Otros gastos = ${division_cuentas:,}")

#Ejecucion

calcular_presupuesto(sueldo)