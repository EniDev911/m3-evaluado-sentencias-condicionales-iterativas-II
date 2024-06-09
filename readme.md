<a href="https://colab.research.google.com/gist/EniDev911/5d0cfe981eef12369582a6d1386bd39e/sentencias-iterativas-condicionales-ii.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

## Actividad 1 - Filtrado Compacto

Una empresa provee de los balances del año anterior un diccionario como se muestra a continuación:

```py
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
```

Se solicita devolver un informe resumido que exponga los meses que **superan un cierto umbral**. El programa debe **retornar un diccionario** con el mes y el valor asociado siempre y cuando superen el umbral especificado.


```python
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


umbral = input("Introduce el umbral para operar: ")
filtrado = {}


if umbral.isdigit():
  for k, v in ventas.items():
    if v > int(umbral):
      filtrado[k] = v

  print(filtrado)

else:
  print("Debes ingresar solo valores númerico")
```

    Introduce el umbral para operar: 55000
    {'Mayo': 81000, 'Noviembre': 91000}


## Actividad 2 - Primeros auxilios

### Anunciado

En cualquier momento puede haber una emergencia y hay que estar preparados ¿sabrías como reaccionar en caso de que alguien necesite de primeros auxilios?.

Es muy probable que mucha gente no conozca cuáles son los pasos a seguir en caso de emergencia. Es por eso que se solicita construir una aplicación que permita indicar los pasos a seguir ante una emergencia. Debido a que no se espera a que usted sea un experto en el tema se provee un diagrama que explica las distintas instancias a la que está sometido durante una emergencia.

Tal como lo muestra el siguiente diagrama:

![img - p_auxilios](https://github.com/EniDev911/assets/blob/main/png/p_auxilios.png?raw=true)

Se requiere la construcción de una aplicación interactiva que entregue los distintos pasos a seguir dependiendo de las respuestas que el usuario entrega en tiempo real.



```python
estimulos = input("¿Responde a Estímulos?: ").lower()

if estimulos == "si":
    print("Valorar la necesidad de llevarlo al hospital más cercano")

elif estimulos == "no":
    print("Abrir la vía Aérea")
    respira = input("¿Respira?: ").lower()

    if respira == "si":
        print("Permitirle posición de suficiente vetilación")

    elif respira == "no":
        print("Administrar 5 ventilaciones y llamar a la ambulancia")

        llegada = False
        while not llegada:
            signos_vitales = input("¿Signos de Vida?: ").lower()

            if signos_vitales == "si":
                print("Reevaluar a la espera de la Ambulancia")

            elif signos_vitales == "no":
                print("Administrar Compresiones Torácicas hasta que llegue la Ambulancia")
            ambulancia = input("¿Llegó la ambulancia?: ")

            if ambulancia == "si":
                llegada = True

print("Fin")
```

    ¿Responde a Estímulos?: no
    Abrir la vía Aérea
    ¿Respira?: no
    Administrar 5 ventilaciones y llamar a la ambulancia
    ¿Signos de Vida?: si
    Reevaluar a la espera de la Ambulancia
    ¿Llegó la ambulancia?: no
    ¿Signos de Vida?: si
    Reevaluar a la espera de la Ambulancia
    ¿Llegó la ambulancia?: no
    ¿Signos de Vida?: no
    Administrar Compresiones Torácicas hasta que llegue la Ambulancia
    ¿Llegó la ambulancia?: si
    Fin


## Actividad 3 - Fuerza Bruta

### Enunciado

¿Que tan seguro es tu password? ¿Intentamos hackear un password?. Mediante el siguiente desafío se busca utilizar un algoritmo muy sencillo, llamado fuerza bruta para determinar cuántos intentos son necesarios para encontrar combinaciones numéricas en minúscula.

Determinar cuántos intentos son necesarios para encontrar combinaciones numéricas en minúscula. El programa debe intentar todas las combinaciones de letras posibles, en orden alfabético, hasta que la combinación de letras sea igual a la de la contraseña indicada. Deberá hacer este proceso letra por letra, de izquierda a derecha.

Otro aspecto que nos solicitan es que la contraseña se pueda ingresar de forma segura. Python proporciona la función `getpass()` del módulo con el mismo nombre, esta función solicita al usuario una contraseña sin hacer *eco*. En nuestro caso estaremos tratando de hacer comprobaciones sobre una entrada de tipo `string` por lo que podemos utilizar un bucle `for` para recorrer la entrada *el password ingresado* y otro bucle `for` anidado sobre el *abcedario* que lo traeremos desde la constante `ascii_lowercase` desde el módulo `string`.


```python
from string import ascii_lowercase
import getpass

password = getpass.getpass("Introduce la contraseña a forzar: ")
intentos = 0

for i in password:
	for j in ascii_lowercase:
		intentos += 1
		if j == i:
			break

print("La contraseña fue forzada en", intentos, "intentos")
```

    Introduce la contraseña a forzar: ··········
    La contraseña fue forzada en 40 intentos

