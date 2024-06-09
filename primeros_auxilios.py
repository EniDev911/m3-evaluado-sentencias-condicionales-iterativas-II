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