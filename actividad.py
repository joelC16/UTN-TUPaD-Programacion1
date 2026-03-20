# EJERCICIO 1 - CAJA DEL KIOSCO
nombre = ""
cantProd = 0


while not nombre.isalpha():
    nombre = input("Ingrese su nombre: ")
    if not nombre.isalpha():
        print("Error: solo letras, sin espacios ni vacío")
    
while cantProd <= 0:
    cantProd = input("Ingrese la cantidad de productos a comprar: ")
    if cantProd.isdigit():
        cantProd = int(cantProd)
    else:
        cantProd = 0


totalSinDescuentos = 0
totalConDescuentos = 0
for i in range(1, cantProd + 1):
    precioProd = ""
    while not precioProd.isdigit():
        precioProd = input(f"Ingrese el precio del producto {i}: ")
    totalSinDescuentos += int(precioProd)
    isDescuento = ""
    while True:
        isDescuento = input("Tiene descuento? S/N: ").upper()
        if isDescuento == "S":
            precioProd = float(precioProd)
            precioProd = precioProd - (precioProd*10)/100
            break
        elif isDescuento == "N":
            break
        else:
            print("Error: ingrese S o N")
    totalConDescuentos += int(precioProd)
    
promedioProd = totalConDescuentos/cantProd
print(f"Total sin descuento: ${totalSinDescuentos}")
print(f"Total con descuento: ${totalConDescuentos}")
print(f"Ahorro total: ${totalSinDescuentos - totalConDescuentos}")
print(f"Promedio por producto: ${promedioProd:.2f}")





# EJERCICIO 2 - ACCESO AL CAMPUS Y MENÚ SEGURO
usuario = "alumno"
contraseña = "python123"
intentos = 0

while intentos < 3:
    print(f"Intento {intentos+1}/3")
    usuarioNombre = input("Usuario: ")
    contraseñaUsuario = input("Clave: ")

    if usuarioNombre == usuario and contraseñaUsuario == contraseña:
        print("Acceso concedido.")
        break
    else:
        print("Error: credenciales inválidas.")
        intentos += 1

if intentos == 3:
    print("Cuenta bloqueada")
else:
    seleccionMenu = 0
    while seleccionMenu != 4:
        opcion = input("\n1) Estado  2) Cambiar clave  3) Mensaje  4) Salir\nOpción: ")

        if not opcion.isdigit():
            print("Error: ingrese un número válido.")
            continue

        seleccionMenu = int(opcion)

        if seleccionMenu < 1 or seleccionMenu > 4:
            print("Error: opción fuera de rango.")
        elif seleccionMenu == 1:
            print("Inscripto")
        elif seleccionMenu == 2:
            nuevaClave = input("Nueva clave: ")

            if len(nuevaClave) < 6:
                print("Error: mínimo 6 caracteres.")
                continue

            confirmacionClave = input("Confirmar clave: ")

            if nuevaClave == confirmacionClave:
                contraseña = nuevaClave
                print("Clave cambiada correctamente.")
            else:
                print("Error: las claves no coinciden.")
        elif seleccionMenu == 3:
            print("Seguí así, vas a romperla 💪")
        elif seleccionMenu == 4:
            print("Saliendo...")
            
            
            
# EJERCICIO 3 - AGENDA DE TURNOS CON NOMBRES

# TURNOS
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

while True:
    operador = input("Nombre del operador: ")
    if operador.isalpha():
        break
    else:
        print("Error: solo letras")

while True:
    opcion = input("\n1) Reservar 2) Cancelar 3) Ver agenda 4) Resumen 5) Salir\nOpción: ")

    if not opcion.isdigit():
        print("Error: ingrese un número")
        continue

    opcion = int(opcion)

    if opcion == 1:
        dia = input("Día (1=Lunes, 2=Martes): ")

        if dia not in ["1", "2"]:
            print("Error")
            continue

        while True:
            nombre = input("Nombre del paciente: ")
            if nombre.isalpha():
                break
            else:
                print("Error: solo letras")

        if dia == "1":
            if nombre in [lunes1, lunes2, lunes3, lunes4]:
                print("Ya existe ese paciente")
            elif lunes1 == "":
                lunes1 = nombre
            elif lunes2 == "":
                lunes2 = nombre
            elif lunes3 == "":
                lunes3 = nombre
            elif lunes4 == "":
                lunes4 = nombre
            else:
                print("No hay turnos disponibles")

        else:
            if nombre in [martes1, martes2, martes3]:
                print("Ya existe ese paciente")
            elif martes1 == "":
                martes1 = nombre
            elif martes2 == "":
                martes2 = nombre
            elif martes3 == "":
                martes3 = nombre
            else:
                print("No hay turnos disponibles")

    elif opcion == 2:
        dia = input("Día (1=Lunes, 2=Martes): ")

        while True:
            nombre = input("Nombre a cancelar: ")
            if nombre.isalpha():
                break
            else:
                print("Error")

        if dia == "1":
            if lunes1 == nombre:
                lunes1 = ""
            elif lunes2 == nombre:
                lunes2 = ""
            elif lunes3 == nombre:
                lunes3 = ""
            elif lunes4 == nombre:
                lunes4 = ""
            else:
                print("No encontrado")

        elif dia == "2":
            if martes1 == nombre:
                martes1 = ""
            elif martes2 == nombre:
                martes2 = ""
            elif martes3 == nombre:
                martes3 = ""
            else:
                print("No encontrado")

    elif opcion == 3:
        dia = input("Día (1=Lunes, 2=Martes): ")

        if dia == "1":
            print("Lunes:")
            print("1:", lunes1 if lunes1 != "" else "(libre)")
            print("2:", lunes2 if lunes2 != "" else "(libre)")
            print("3:", lunes3 if lunes3 != "" else "(libre)")
            print("4:", lunes4 if lunes4 != "" else "(libre)")
        elif dia == "2":
            print("Martes:")
            print("1:", martes1 if martes1 != "" else "(libre)")
            print("2:", martes2 if martes2 != "" else "(libre)")
            print("3:", martes3 if martes3 != "" else "(libre)")

    elif opcion == 4:
        ocupadosLunes = sum([lunes1 != "", lunes2 != "", lunes3 != "", lunes4 != ""])
        ocupadosMartes = sum([martes1 != "", martes2 != "", martes3 != ""])

        print(f"Lunes: {ocupadosLunes}/4 ocupados")
        print(f"Martes: {ocupadosMartes}/3 ocupados")

        if ocupadosLunes > ocupadosMartes:
            print("Día con más turnos: Lunes")
        elif ocupadosMartes > ocupadosLunes:
            print("Día con más turnos: Martes")
        else:
            print("Empate")

    elif opcion == 5:
        print("Sistema cerrado")
        break

    else:
        print("Opción inválida")
        
        
        
        
# EJERCICIO 4 - ESCAPE ROOM: LA BOVEDA
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
racha_forzar = 0

while True:
    agente = input("Nombre del agente: ")
    if agente.isalpha():
        break
    else:
        print("Error: solo letras")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:

    if alarma and tiempo <= 3:
        print("Sistema bloqueado por alarma. DERROTA.")
        break

    print(f"\nEnergía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas} | Alarma: {alarma}")

    opcion = input("1) Forzar  2) Hackear  3) Descansar\nOpción: ")

    if not opcion.isdigit():
        print("Error")
        continue

    opcion = int(opcion)

    if opcion == 1:
        energia -= 20
        tiempo -= 2
        racha_forzar += 1

        if racha_forzar == 3:
            print("La cerradura se trabó. Alarma activada.")
            alarma = True
            continue

        if energia < 40:
            num = input("Riesgo! Elegí número 1-3: ")

            while not num.isdigit() or int(num) < 1 or int(num) > 3:
                num = input("Ingrese 1, 2 o 3: ")

            if int(num) == 3:
                alarma = True
                print("Activaste la alarma!")
                continue

        if not alarma:
            cerraduras_abiertas += 1
            print("Cerradura abierta!")

    elif opcion == 2:
        energia -= 10
        tiempo -= 3
        racha_forzar = 0  

        for i in range(4):
            codigo_parcial += "A"
            print(f"Progreso hackeo: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("Hackeo exitoso, cerradura abierta")

    elif opcion == 3:
        tiempo -= 1
        racha_forzar = 0  

        energia += 15
        if energia > 100:
            energia = 100

        if alarma:
            energia -= 10

        print("Descansaste")

    else:
        print("Opción inválida")

if cerraduras_abiertas == 3:
    print("VICTORIA, Abriste la boveda.")
elif energia <= 0 or tiempo <= 0:
    print("DERROTA. Te quedaste sin recursos.")
    
    
    
    
    
    
# EJERCICIO 5 - ESCAPE ROOM: LA ARENA DEL GRADIADOR
print("BIENVENIDO A LA ARENA")

while True:
    nombre = input("Nombre del Gladiador: ")
    if nombre.isalpha():
        break
    else:
        print("Error: Solo se permiten letras.")

vidaJugador = 100
vidaEnemigo = 100
pociones = 3
dañoJugador = 15
dañoEnemigo = 12
turnoJugador = True

print("INICIO DEL COMBATE")

while vidaJugador > 0 and vidaEnemigo > 0:

    print(f"\n{nombre} (HP: {vidaJugador}) vs Enemigo (HP: {vidaEnemigo}) | Pociones: {pociones}")
    
    print("Elige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")

    opcion = input("Opción: ")

    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        print("Error: Ingrese un número válido.")
        opcion = input("Opción: ")

    opcion = int(opcion)

    if opcion == 1:
        dañoFinal = dañoJugador

        if vidaEnemigo < 20:
            dañoFinal = dañoJugador * 1.5

        vidaEnemigo -= dañoFinal
        print(f"Atacaste al enemigo por {dañoFinal} de daño")

    elif opcion == 2:
        print(">> ¡Inicias una ráfaga de golpes")
        for i in range(3):
            vidaEnemigo -= 5
            print("> Golpe conectado por 5 de daño")

    elif opcion == 3:
        if pociones > 0:
            vidaJugador += 30
            pociones -= 1
            print("Te curaste 30 de vida")
        else:
            print("¡No quedan pociones!")

    if vidaEnemigo > 0:
        vidaJugador -= dañoEnemigo
        print(f"El enemigo te atacó por {dañoEnemigo} puntos de daño")

if vidaJugador > 0:
    print(f"VICTORIA, {nombre} ha ganado la batalla")
else:
    print("DERROTA. Has caído en combate")