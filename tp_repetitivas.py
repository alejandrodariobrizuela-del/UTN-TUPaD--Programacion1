# Ejercicio 1


while True:
    nom = input("Ingrese su nombre: ")
    if nom.isalpha():
        break
    print("Error: solo letras, sin números ni espacios.")

while True:
    cant = input("Ingrese la cantidad de productos a comprar: ")
    if cant.isdigit() and int(cant) > 0:
        cantidad = int(cant)
        break
    print("Error: ingrese un número entero positivo.")

total_c_des = 0 
total_sin_des = 0 


for i in range(cantidad):
    print(f"\n--- Producto {i + 1} ---")

    while True:
        precio = input(f"  Precio del producto {i + 1}: $")
        if precio.isdigit() and int(precio) > 0:
            precio = int(precio)
            break
        print("Error: ingrese un precio entero positivo.")


    while True:
        descuento = input(f"  ¿Tiene descuento? (S/N): ")
        if descuento.lower() in ["s", "n"]:
            break
        print("Error: ingrese S para sí o N para no.")

    precio_final = precio  

    if descuento.lower() == "s":
        ahorro = precio * 0.10          
        precio_final = precio - ahorro  
        print(f"Descuento aplicado: -${ahorro:.2f}")

    total_sin_des += precio       
    total_c_des += precio_final  



ahorro_total = total_sin_des - total_c_des
promedio = total_c_des / cantidad  
print("\n" + "=" * 40)
print(f"  RESUMEN DE COMPRA - {nom}")
print("=" * 40)
print(f"  Total sin descuentos:  ${total_sin_des:.2f}")
print(f"  Total con descuentos:  ${total_c_des:.2f}")
print(f"  Ahorro total:          ${ahorro_total:.2f}")
print(f"  Promedio por producto: ${promedio:.2f}")
print("=" * 40)



# Ejercicio 2
usuario_correcto = "usuario"
clave_correcta = "python123"

for intento in range(1,4):
    print()
    print(f"Intento {intento}/3") 
    usuario = input("Ingrese usuario:")
    contraseña = input("Ingrese clave:")

    if usuario == usuario_correcto and contraseña == clave_correcta:
        print()
        print("Acceso Permitido.")
        break
    
    else:
        print()
        print("El usuario o la clave son incorrectos.")
else:
    print()
    print("Cuenta Bloqueada.")


while True:
    print()
    print("1. Ver estado de inscripción.")
    print("2. Cambiar Clave")
    print("3. Frase motivacional")
    print("4. Salir")
    op = input("Ingrese opción:")

    if not op.isdigit():
        print("Ingresar número válido:")
        continue
    
    op = int(op)
    if op < 1 or op > 4:
        print("Error: Opción fuera de rango (Ingrese número del  1 al 4).")

    
    if op == 1:
        print()
        print("Inscripto.")
    
    if op == 2:
        while True:
            nueva_contraseña = input("Nueva Clave:")

            if len(nueva_contraseña) < 6:
                print("Error, la clave debe tener como mínimo 6 carácteres")
                continue

            while True: 
                confirmacion = input("Confirme su clave:")
                if confirmacion != nueva_contraseña:
                    print()
                    print("Las claves no coinciden")
                else:
                    break

            clave_correcta == nueva_contraseña
            print()
            print("Clave actualizada correctamente.")
            break
    
    if op == 3:
        print("")
        print("Vive cada minuto como si fuera el último!!")
    
    if op == 4:
        print("")
        print("Saliendo...")
        break


# Ejercicio 3

while True:
    user = input("Ingrese usuario:")
    if not user.isalpha(): 
        print("Error, solo letras.")
        continue
    break

print(f"Bienvenido {user}")

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

while True:
    print("")
    print("1. Reservar turno.")
    print("2. Cancelar turno")
    print("3. Ver agenda del día.")
    print("4. Ver resumen general.")
    print("5. Cerrar sistema")
    op = input("Ingrese opción:")

    if not op.isdigit():
        print("La opción debe ser un número.")
        continue

    op = int(op)

    if op < 1 or op > 5:
        print("Opción inválida.")
        continue


    if op == 1:

        dia = input("Elegir día (1=Lunes, 2=Martes).")
        if not dia.isdigit():
            print("La opción debe ser un número.")
            continue

        else: 
            dia = int(dia)

            if dia < 1 or dia > 2:
                print("Día inválido.")
            else:
                while True:
                    paciente = input("Ingrese paciente:")
                    if not paciente.isalpha():
                        print("Solo letras por favor")
                        continue
                    break

                if dia == 1:
                    if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                        print("Error, el paciente ya tiene turno agendado el Lunes")
                    
                    elif lunes1 == "":
                        lunes1 = paciente
                        print("Turno 1 de Lunes reservado.")

                    elif lunes2 == "":
                        lunes2 = paciente
                        print("Turno 2 de Lunes reservado.")
                    
                    elif lunes3 == "":
                        lunes3 = paciente
                        print("Turno 3 de Lunes reservado.")
                    
                    elif lunes4 == "":
                        lunes4 = paciente
                        print("Turno 4 de Lunes reservado.")

                    else:
                        print("Error, no hay turnos disponibles el Lunes")
                
                elif dia == 2:
                    if paciente == martes1 or paciente == martes2 or paciente == martes3:
                        print("Error, el paciente ya tiene turno agendado el martes.")
                    
                    elif martes1 == "":
                        martes1 = paciente
                        print("Turno 1 de Martes reservado.")
                    
                    elif martes2 == "":
                        martes2 = paciente
                        print("Turno 2 de Martes reservado.")
                    
                    elif martes3 == "":
                        martes3 = paciente
                        print("Turno 3 de Martes reservado.")

                    else:
                        print("Error, no hay tunos disponibles el martes.")

    if op == 2:
        dia = input("Elegir día (1=Lunes, 2=Martes).")
        if not dia.isdigit():
            print("La opción debe ser un número.")
            continue

        else: 
            dia = int(dia)

            if dia < 1 or dia > 2:
                print("Día inválido.")
            else:
                while True:
                    paciente = input("Ingrese paciente:")
                    if not paciente.isalpha():
                        print("Solo letras por favor")
                        continue
                    break
                if dia == 1:
                    if paciente == lunes1:
                        lunes1 = ""
                        print("Turno cancelado.")

                    elif paciente == lunes2:
                        lunes2 = ""
                        print("Turno cancelado.")

                    elif paciente == lunes3:
                        lunes3 = ""
                        print("Turno cancelado.")

                    elif paciente == lunes4:
                        lunes4 = ""
                        print("Turno cancelado.")

                    else:
                        print("Paciente no encontrado en Lunes.")
                
                elif dia == 2:
                    if paciente == martes1:
                        martes1 = ""
                        print("Turno cancelado.")

                    elif paciente == martes2:
                        martes2 = ""
                        print("Turno cancelado.")

                    elif paciente == martes3:
                        martes3 = ""
                        print("Turno cancelado.")

                    else:
                        print("Paciente no encontrado en Martes.")

    if op == 3:
        dia = input("Elegir día (1=Lunes, 2=Martes).")
        if not dia.isdigit():
            print("La opción debe ser un número.")
            continue

        else: 
            dia = int(dia)

            if dia < 1 or dia > 2:
                print("Día inválido.")
            else:
                if dia == 1:
                    print()
                    print("-----Agenda de Lunes-----")
                    print(f"Turno 1: {lunes1 if lunes1 != '' else '(libre)'}")
                    print(f"Turno 2: {lunes2 if lunes2 != '' else '(libre)'}")
                    print(f"Turno 3: {lunes3 if lunes3 != '' else '(libre)'}")
                    print(f"Turno 4: {lunes4 if lunes4 != '' else '(libre)'}")
                
                elif dia == 2:
                    print()
                    print("-----Agenda de Martes-----")
                    print(f"Turno 1: {martes1 if martes1 != '' else '(libre)'}")
                    print(f"Turno 2: {martes2 if martes2 != '' else '(libre)'}")
                    print(f"Turno 3: {martes3 if martes3 != '' else '(libre)'}")

    if op == 4:
        ocupados_lunes = 0
        if lunes1 != "": ocupados_lunes += 1
        if lunes2 != "": ocupados_lunes += 1
        if lunes3 != "": ocupados_lunes += 1
        if lunes4 != "": ocupados_lunes += 1

        ocupados_martes = 0
        if martes1 != "": ocupados_martes += 1
        if martes2 != "": ocupados_martes += 1
        if martes3 != "": ocupados_martes += 1

        print(f"\nLunes   → Ocupados: {ocupados_lunes} | Disponibles: {4 - ocupados_lunes}")
        print(f"Martes  → Ocupados: {ocupados_martes} | Disponibles: {3 - ocupados_martes}")

        if ocupados_lunes > ocupados_martes:
            print("Día con más turnos: Lunes")
        elif ocupados_martes > ocupados_lunes:
            print("Día con más turnos: Martes")
        else:
            print("Empate entre Lunes y Martes")

    if op == 5:
        print()
        print("Cerrando sistema...")
        break


# Ejercicio 4
energia = 100 
tiempo = 12 
cerraduras_abiertas = 0 
alarma = False 
codigo_parcial = ""
veces_forzado = 0

while True:
    
    agente = input("Ingrese nombre del agente:")

    if not agente.isalpha():
        print("Error: Solo se permiten letras.")
        continue
    break
print()
print(f"Bienvenido, agente {agente}")


while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not alarma:
    print(f"\n--- Estado ---")
    print(f"Energía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}/3")
    print(f"Alarma: {'ACTIVA' if alarma else 'off'} | Código parcial: {codigo_parcial}")


    print("\n1. Forzar cerradura.")
    print("2. Hackear panel.")
    print("3. Descansar")
    op = input("Ingrese opción:")

    if not op.isdigit():
        print("\nError, la opción debe ser un número.")
        continue
    else:
        op = int(op)
        if op < 1 and op > 3:
            print("\nOpción inválida.")
    
    if op == 1:
        energia -= 20
        tiempo -= 2
        veces_forzado += 1

        if veces_forzado == 3:
            alarma == True 

        else:
            if energia < 40:
                print("\nRiesgo de alarma.")
                while True:
                    print()
                    n = input("Ingrese número del 1 al 3:")
                    if not n.isdigit():
                        print("\nQue sea un número por favor.")
                        continue
                    else:
                        n = int(n)
                        if n < 1 or n > 3:
                            print("\nNúmero inválido")
                            continue
                        break

                if n == 3:
                    alarma == True
                    print("\nAlarma activada!!!!")
                else:
                    cerraduras_abiertas += 1
                    print(f"\nCerradura abierta. Total: {cerraduras_abiertas}/3")
            else:
                cerraduras_abiertas += 1
                print(f"\nCerradura abierta. Total: {cerraduras_abiertas}/3")


    elif op == 2:
        energia -= 10
        tiempo -= 3
        veces_forzado = 0

        print("Hackeando panel...")
        for pasos in range(4):
            codigo_parcial += "A"
            print(f"  Paso {pasos}/4 → Código: {codigo_parcial}")

        
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
        print(f"\nCerradura abierta. Total: {cerraduras_abiertas}/3")


    elif op == 3:
        tiempo -= 1
        veces_forzado = 0
        if alarma == True:
            energia -= 10
        else:
            energia += 15
            if energia > 100:
                energia = 100

    if alarma == True and tiempo <= 3 and cerraduras_abiertas < 3:
        print("\nDERROTA, Sistema bloqueado :´(")
        break

if cerraduras_abiertas == 3:
    print(f"\nVICTORIA!! Has abierto la boveda, felicitaciones agente {agente}")
elif energia <= 0:
    print("\nDERROTA, te has quedado sin energía :´(")
elif tiempo <= 0:
    print("\nDERROTA,  te has quedado sin timepo :´(")
elif alarma == True and tiempo <= 3:
        print("\nDERROTA, Sistema bloqueado :´(")


# Ejercicio 5
vida_gladiador = 100
vida_enemigo = 100
pociones_de_vida = 3
ataque_pesado = 15
daño_enemigo = 12
turno_gladiador = True

while True:
    gladiador = input("Ingrese su nombre, gladiador: ")

    if not gladiador.isalpha():
        print("\nERROR: Solo se permiten letras.")
        continue
    break

print(f"\nBienvenido, gladiador {gladiador}")

print("\n=== INICIO DE COMBATE ===")

while vida_enemigo > 0 and vida_gladiador > 0:
        print(f"\n{gladiador} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones_de_vida}")
        print("\n1. Ataque Pesado.")
        print("2. Ráfaga Veloz")
        print("3. Curar")

        op = input("Ingrese opción: ")

        if not op.isdigit():
            print("Ingrese un número, por favor.")
            continue
        else:
            op = int(op)
            if op < 1 or op > 4:
                print("Opción inválida.")

        if op == 1:
            print("Ataque Pesado")
            if vida_enemigo < 20:
                critico = ataque_pesado * 1.5
                print(f"¡Atacaste al enemigo por {critico} puntos de daño!")
            else:
                critico = ataque_pesado
                print(f"¡Atacaste al enemigo por {critico} puntos de daño!")

            vida_enemigo -= critico


        if op == 2:
            print("Ráfaga de Golpes")
            for ataques in range(3):
                vida_enemigo -= 5
                print("\n > Golpe conectado por 5 de daño")

        if op == 3:
            print("Curando...")
            if pociones_de_vida > 0:
                vida_gladiador += 30
                if vida_gladiador > 100:
                    vida_gladiador = 100

                pociones_de_vida -= 1
                print(f"\n¡Has usado una poción! HP: {vida_gladiador} | Pociones restantes: {pociones_de_vida}")

            else:
                print("\n¡No quedan pociones!")

        if vida_enemigo > 0:
            vida_gladiador -= daño_enemigo
            print(f"\nEl enemigo te ha infligido {daño_enemigo}, tienes {vida_enemigo} puntos de vida.")


if vida_gladiador > 0:
    print(f"\nVICTORIA! {gladiador} ha ganado la batalla.")
elif vida_gladiador <= 0:
    print("\nDERROTA. Has caído en combate.")