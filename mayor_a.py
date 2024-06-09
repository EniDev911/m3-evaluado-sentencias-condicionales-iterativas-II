import sys

ventas = {
    "Enero": 15000,
    "Febrero": 22000,
    "Marzo": 12000,
    "Abril": 17000,
    "Mayo": 81000,
    "Junio": 13000,
    "Julio": 21000,
    "Agosto": 41200,
    "Septiembre": 25000,
    "Octubre": 21500,
    "Noviembre": 91000,
    "Diciembre": 21000,
}


if len(sys.argv) == 2:
    
    umbral = sys.argv[1]

    if umbral.isdigit():
        filtrado = {}

        for k, v in ventas.items():
            if v > int(umbral):
                filtrado[k] = v
        print(filtrado)
    else:
        print("Debes ingresar solo valores númericos")
else:
  print("Debes pasarme un argumento por línea de comando")