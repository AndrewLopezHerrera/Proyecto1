"""
Nombre: Sistema_de_reservacion_de_boletos
Parámetros: opcion: es la opcion a la que se desea entrar.
Entradas: El sistema iniciará con ejecutando la función 'sistema_de_reservacion_de_boletos()', se abrirá el menú de opciones para el usuario,
este debe introducir alguna de las opciones descritas por el mensaje que se presentará en la pantalla. Las opciones son 1, 2 y 3.
Salidas: La opción 1 abre la funcion de seguridad de entrada para 
las opciones administrativas, la opción 2 abre las opciones normales para el usuario y la opción 3 cierra el programa.
Restricciones: Solo se permite introducir la opcion 1, 2 o 3.
"""
def sistema_de_reservacion_de_boletos() :
    print('Bienvenido al sistema de reservación de boletos')
    return sistema_de_reservacion_de_boletos2()

def sistema_de_reservacion_de_boletos2() :
    print("""\n    MENÚ PRINCIPAL
1. Opciones administrativas
2. Opciones normales de usuario
9. Salir""")
    opcion = str(input('Introduzca la opción que desea: '))
    if opcion == '1' :
        return seguridad_de_entrada()
    elif opcion == '2' :
        return opciones_normales_de_usuario()
    elif opcion == '9' :
        return print('\nLe deseamos un excelente día\n')
    else :
        print('\nPor favor, introduzca una opcion válida\n')
        return sistema_de_reservacion_de_boletos2()

#Nombre: seguridad_de_entrada
#Parametros: contrasena: es el parámetro que se utiliza para compararla con la contraseña guardada y así comprobar la identificación del usuario.
#Entradas: Debe introducir la contraseña que se le solicita. La opción salir al menú principal estará disponible,
#en caso que no se desee entrar a las opciones administrativas.
#Salidas: Si la contraseña es correcta, la función debe retornar las opciones adminsitartivas
#Restricciones: Solo se permite introducir la opción correcta para retornar las opciones administrativas.

def seguridad_de_entrada() :
    print('\nIntroduzca la contraseña \nIntroduzca 9 para ir al menú principal')
    contrasena = str(input('Introduzca la contraseña: '))
    archivoContra = open('contraseña.txt','r')
    contraguardada = archivoContra.read()
    archivoContra.close()
    if contrasena == '9' :
        return sistema_de_reservacion_de_boletos2()
    elif contrasena == contraguardada :
        return opciones_administrativas()
    else :
        print('\nContraseña incorrecta')
        return seguridad_de_entrada()

#Nombre: opcione administrativas
#Parámetros: opcion: es la opcion a la que se desea entrar.
#Entradas: Debe introducir la opción que desea realizar, debe introducir un numero del 1 al 6, dependiendo de lo que se desea realizar.
#Salidas: Si la opción es 1, debe retornar gestión de empresas. Si la opción es 2, debe retornar gestion de transporte por empresas. Si la opción es 3,
#debe retornar gestión de viaje. Si la opción es 4, debe retornar consultar historial de reservaciones. Si la opción es 5, estadísticas de viaje.
#Si la opción es 6, debe retornar cambiar contraseña. Si la opción es 9, debe salir al menú principal.
#Restricciones: Solo se permite introducir la opcion 1, 2, 3, 4, 5, 6 y 9.
def opciones_administrativas():
    print("""
       Opciones Administrativas
1. Gestión de empresas
2. Transporte por empresas
3. Gestión de viaje
4. Consultar historial de reservaciones
5. Estadísticas de viaje
6. Cambiar contraseña
9. Salir al menú principal""")
    opcion = str(input('Introduzca la opción que desea: '))
    if opcion == '1' :
        return gestión_de_empresas()
    elif opcion == '2' :
        return transporte_por_empresas()
    elif opcion == '3' :
        return gestión_de_viaje()
    elif opcion == '4' :
        return consultar_historial_de_reservaciones()
    elif opcion == '5' :
        return estadísticas_de_viaje()
    elif opcion == '6' :
        return cambiar_contraseña()
    elif opcion == '9' :
        return sistema_de_reservacion_de_boletos2()
    else :
        print('\nPor favor, introduzca una opcion válida\n')
        return opciones_administrativas()

#Nombre: gestión de empresas
#Parámetros: opcion: es la opcion a la que se desea entrar.
#Entradas: Debe introducir la opción que desea realizar, debe introducir un numero del 1 al 4, dependiendo de lo que se desea realizar. 9 sirve para salir.
#Salidas: Si la opción es 1, debe incluir empresas. Si la opción es 2, debe eliminar empresas. Si la opción es 3, debe modificar empresas
#Si la opción es 4, debe mostrar empresas. Si la opción es 9, debe salir.
#Restricciones: Solo se permite introducir la opcion 1, 2, 3, 4 y 9.
def gestión_de_empresas() :
    print("""
        Gestión de empresas
1. Incluir empresa
2. Eliminar empresa
3. Modificar empresa
4. Mostrar empresas
9. Salir""")
    opcion = str(input('Introduzca la opción que desea: '))
    if opcion == '1' :
        return incluir_empresa()
    elif opcion == '2' :
        return eliminar_empresa()
    elif opcion == '3' :
        return modificar_empresa()
    elif opcion == '4' :
        return mostrar_empresas()
    elif opcion == '9' :
        return opciones_administrativas()
    else :
        print('\nPor favor, introduzca una opcion válida\n')
        return gestión_de_empresas()

#Nombre: incluir empresa.
#Entradas: Primeramente debe introducir el nombre de la empresa. Segundo debe introducir la cédula jurídica. Tercero debe introducir el lugar de ubicación de la empresa
#Salidas: En caso que todo haya sido introducido correctamente, se imprimirá la empresa y se guardará la empresa, en caso que hay algo incorrecto el sistea lo
#notificará al usuario.
#Restricciones: El número de cédula jurídica debe ser de diez dígitos, solo puede contener números y no puede ser repetida.
def incluir_empresa() :
    nombreEmpresa = str(input('Introduzca el nombre de la empresa: '))
    cedulaJuridica = str(input('Introduzca la cedula juridica de la empresa: '))
    validador = comprobador_entero(cedulaJuridica, 0)
    if validador == 1 :
        print('\nEn la cedula jurídica solo puede introducir números')
        return gestión_de_empresas()
    else :
        contador = cuenta_caracteres(cedulaJuridica, 0)
        if contador == 10 :
            cedula = open('empresas.txt', 'r')
            for empresa in cedula.readlines() :
                empresa = empresa.split(';')
                if cedulaJuridica == empresa[1] :
                    print('\nEl numero de cédula ingresado ya está registrado')
                    return gestión_de_empresas()
                else :
                    cedulaJuridica
        else :
            print('\nLa cedula juridica debe tener diez digitos')
            return gestión_de_empresas()
    ubicacionEmpresa = str(input('Introduzca la ubicación de la empresa: '))
    nuevaEmpresa = nombreEmpresa + ';' + cedulaJuridica + ';' + ubicacionEmpresa + '\n'
    incluirEmpresa = open('empresas.txt', 'a')
    incluirEmpresa.write(nuevaEmpresa)
    incluirEmpresa.close()
    print('Empresa creada exitosamente')
    return gestión_de_empresas()

def comprobador_entero(dato, comparando) :
    if dato == '' :
        return 2
    elif dato[0] == str(comparando) :
        return comprobador_entero(dato[1:], 0)
    elif comparando == 10 :
        return 1
    else :
        return comprobador_entero(dato, comparando + 1)

def cuenta_caracteres(texto, contador) :
    if texto == '' :
        return contador
    else :
        return cuenta_caracteres(texto[1:], contador + 1)

#Nombre: eliminar empresa
#Entradas: Recibe la cedula jurídica y comprueba si existe en la base de datos.
#Salidas: Hay dos salidas, se imprime 'no hay coincidencias' cuando ninguna empresa hay sido encontrada, si hay una coincidencia,se procede a borrarla de la lista.
#Restricciones: El número de cédula jurídica debe ser de diez dígitos, solo puede contener números.
def eliminar_empresa() :
    cedulaJuridica = str(input('Introduzca la cedula juridica de la empresa que desea eliminar: '))
    validador = comprobador_entero(cedulaJuridica, 0)
    if validador == 1 :
        print('\nEn la cedula jurídica solo puede introducir números')
        return gestión_de_empresas()
    else :
        contador = cuenta_caracteres(cedulaJuridica, 0)
        if contador == 10 :
            contador2 = 0
            cedula = open('empresas.txt', 'r')
            for empresa in cedula.readlines() :
                empresaAux = empresa.split(';')
                if cedulaJuridica == empresaAux[1] :
                    contador2 += 1
                    print(empresaAux[0], 'ha sido eliminado')
                    cedula.close()
                else :
                    if contador2 == 0 :
                        cedula.close()
                        contador2 += 1
                        escribir_texto(empresa)
                    else :
                        cedula.close()
                        anadir_texto(empresa)
        else :
            print('\nLa cedula juridica debe tener diez digitos')
            return gestión_de_empresas()
        if contador2 == 1 :
            print('\nNo hay coincidencias')
            return gestión_de_empresas()
        else :
            return gestión_de_empresas()

def escribir_texto(empresa) :
    archivo = open('empresas.txt', 'w')
    archivo.write(empresa)
    archivo.close()

def anadir_texto(empresa) :
    archivo = open('empresas.txt', 'a')
    archivo.write(empresa)
    archivo.close()

#Nombre: modificar_empresa
#Entradas: Recibe la cedula jurídica y comprueba si existe en la base de datos.
#Salidas: Un menú que tiene dos opciones para cambiar los datos, y la opción de guardar.
#Restricciones: El número de cédula jurídica debe ser de diez dígitos, solo puede contener números.
def modificar_empresa() :
    cedulaJuridica = str(input('Introduzca la cedula juridica de la empresa que desea modifcar: '))
    validador = comprobador_entero(cedulaJuridica, 0)
    if validador == 1 :
        print('\nEn la cedula jurídica solo puede introducir números')
        return gestión_de_empresas()
    else :
        contador = cuenta_caracteres(cedulaJuridica, 0)
        if contador == 10 :
            contador2 = 0
            cedula = open('empresas.txt', 'r')
            for empresa in cedula.readlines() :
                empresaAux = empresa.split(';')
                if cedulaJuridica == empresaAux[1] :
                    contador2 += 1
                    respuesta = modificar_contacto_selecionado(empresaAux, 0)
                    empresa_mod = respuesta[0][0] + ';' + respuesta[0][1] + ';' + respuesta[0][2] + '\n'
                    cantidadCambios = respuesta[1]
                    if contador == 0 :
                        if cantidadCambios >= 1 :
                            print(empresaAux[0], 'ha sido modificado')
                            escribir_texto(empresa_mod)
                            cedula.close()
                        else:
                            print('No se han guardado los cambios')
                            escribir_texto(empresa)
                            cedula.close()
                    else :
                        if cantidadCambios >= 1 :
                            print(empresaAux[0], 'ha sido modificado')
                            anadir_texto(empresa_mod)
                            cedula.close()
                        else:
                            print('No se han guardado los cambios')
                            anadir_texto(empresa)
                            cedula.close()
                else :
                    if contador2 == 0 :
                        cedula.close()
                        contador2 += 1
                        escribir_texto(empresa)
                    else :
                        cedula.close()
                        anadir_texto(empresa)
        else :
            print('\nLa cedula juridica debe tener diez digitos')
            return gestión_de_empresas()
        if contador2 == 1 :
            print('\nNo hay coincidencias')
            return gestión_de_empresas()
        else :
            return gestión_de_empresas()

def modificar_contacto_selecionado(empresaAux, contador) :
    print("""
    ¿Qué desea modificar?
1. Nombre de la empresa
2. Ubicación de la empresa
    Ingrese:
9. Guardar
0. Cancelar""")
    opcion = str(input('\nIngrese la opción deseada: '))
    if opcion == '1' :
        empresaAux[0] = str(input('\nIngrese el nuevo nombre: '))
        return modificar_contacto_selecionado(empresaAux, contador + 1)
    elif opcion == '2' :
        empresaAux[2] = str(input('\nIngrese la nueva ubicación: '))
        return modificar_contacto_selecionado(empresaAux, contador + 1)
    elif opcion == '9' :
        return [empresaAux, contador]
    elif opcion == '0' :
        return [empresaAux, 0]
    else :
        print('\nPor favor, introduzca una opcion válida\n')
        return modificar_contacto_selecionado(empresaAux, contador)

#Nombre: mostrar empresas
#Entradas: No posee ninguna entrada, solo debe ejecutarse.
#Salidas: La impresión de todas las empresas registradas.
#Restricciones: Ninguna.
def mostrar_empresas() :
    empresas = open('empresas.txt', 'r')
    contador = 0
    for soloEmpresa in empresas.readlines() :
        soloEmpresa = soloEmpresa.split(';')
        if soloEmpresa[1] == 'inicio' :
            empresas.close()
        else :
            contador += 1
            print(' Nombre: ', soloEmpresa[0], '\n','Cédula jurídica:', soloEmpresa[1], '\n','Ubicacion:', soloEmpresa[2])
            empresas.close()
    if contador == 0 :
        print('No hay empresas registradas')
        return gestión_de_empresas()
    else :
        return gestión_de_empresas()
        
#Nombre: transporte por empresa
#Entradas: Una de las opciones que se presenta en el mensaje.
#Salidas: Si presiona 1 retorna incluir transporte, si presiona 2 retorna eliminar transporte, si presiona 3 retorna modificar transporte,
#si presiona 4 retorna mostrar transportes, si presiona 4 retorna se decuelve a las opciones administrativas.
#Restricciones: Solo se pueden introducir los números presentados en el mensaje.
def transporte_por_empresas() :
    print("""
        Gestion de Transporte por Empresa
1. Incluir transporte
2. Eliminar transporte
3. Modificar transporte
4. Mostrar transportes
9. Salir""")
    opcion = str(input('\nIngrese la opción deseada: '))
    if opcion == '1' :
        return incluir_trasnporte()
    elif opcion == '2' :
        return eliminar_transporte()
    elif opcion == '3' :
        return modificar_transporte()
    elif opcion == '4' :
        return mostrar_transportes()
    elif opcion == '9' :
        return opciones_administrativas()
    else :
        print('\nPor favor, introduzca una opcion válida\n')
        return transporte_por_empresas()

def incluir_trasnporte() :
    placa = str(input('Ingrese la placa del vehículo: '))
    if cuenta_caracteres(placa, 0) == 6 :
        if comprobar_existencia_placa(placa) :
            marca = str(input('Ingrese la marca del vehículo: '))
            modelo = str(input('Ingrese el modelo del vehículo: '))
            año = str(input('Ingrese el año del vehículo: '))
            if comprobador_entero(año, 0) == 2 :
                if cuenta_caracteres(año, 0) == 4 :
                    empresa = str(input('Ingrese el numero de cédula jurídica de la empresa: '))
                    if comprobador_entero(empresa, 0) == 2 :
                        if cuenta_caracteres(empresa, 0) == 10 :
                            if comprobar_existencia_empresa(empresa) :
                                asientosVIP = str(input('Ingrese la cantidad de asientos VIP: '))
                                if comprobador_entero(asientosVIP, 0) == 2 :
                                    asientosNormales = str(input('Ingrese la cantidad de asientos normales: '))
                                    if comprobador_entero(asientosNormales, 0) == 2 :
                                        asientoseconomicos = str(input('Ingrese la cantidad de asientos económicos: '))
                                        if comprobador_entero(asientoseconomicos, 0) == 2 :
                                            vehiculo = (placa + ';' + marca + ';' + modelo + ';' + año + ';' + empresa + ';' + asientosVIP + ';' +
                                                        asientosNormales + ';' + asientoseconomicos + ';' + 'inactivo' + '\n')
                                            registrar = open('vehiculos.txt', 'a')
                                            registrar.write(vehiculo)
                                            print('Los datos han sido guardados')
                                            registrar.close()
                                            return transporte_por_empresas()
                                        else :
                                            print('\nError: el dato introducido solo debe poseer numeros')
                                            return transporte_por_empresas()
                                    else :
                                        print('\nError: el dato introducido solo debe poseer numeros')
                                        return transporte_por_empresas()
                                else :
                                    print('\nError: el dato introducido solo debe poseer numeros')
                                    return transporte_por_empresas()
                            else :
                                print('\nLa cédula jurídica introducida no existe')
                                return transporte_por_empresas()
                        else :
                            print('\nLa cedula juridica debe tener diez digitos')
                            return transporte_por_empresas()
                    else :
                        print('\nLa cedula juridica solo debe poseer numeros')
                        return transporte_por_empresas()
            else :
                print('\nError: el dato introducido solo debe poseer numeros')
                return transporte_por_empresas()
        else :
            print('\nLa placa introducida ya existe')
            return transporte_por_empresas()
    else :
        print('\nLa placa debe tener seis caracteres')
        return transporte_por_empresas()

def comprobar_existencia_placa(placa) :
    vehiculo = open('vehiculos.txt', 'r')
    for comparacion in vehiculo.readlines() :
        comparacion = comparacion.split(';')
        vehiculo.close()
        if comparacion[0] == placa :
            return False
    return True

def comprobar_existencia_empresa(cedulaJurídica) :
    empresa = open('empresas.txt', 'r')
    for comparacion in empresa.readlines() :
        comparacion = comparacion.split(';')
        empresa.close()
        if comparacion[1] == cedulaJurídica :
            return True  
    return False

#Nombre: eliminar transporte
#Entradas: el numero de placa del vehículo a eliminar.
#Salidas: El mensaje de que el vehículo ha sido eliminado o el mensaje que no se ha encontrado coincidencias.
#Restricciones: La placa ingresada debe ser de seis caracteres y debe existir en la base de datos.
def eliminar_transporte() :
    placa = str(input('Ingrese la placa del vehículo que desea eliminar: '))
    if cuenta_caracteres(placa, 0) == 6 :
        if comprobar_existencia_placa_eliminar(placa) :
            contador = 0
            vehiculo = open('vehiculos.txt', 'r')
            for informacion in vehiculo.readlines() :
                informacionAux = informacion.split(';')
                vehiculo.close()
                if informacionAux[0] ==  placa :
                    if contador == 0 :
                        contador += 1
                        if informacionAux[8] == 'reservado\n' :
                            print('\nEl vehículo', informacionAux[1], 'no se puede eliminar. \nSe encuentra reservado para un viaje')
                            escribir_texto_vehiculo(informacion)
                        else :
                            print('El vehículo', informacionAux[1], 'con placa', informacion[0], 'ha sido eliminado')
                    else :
                        if informacionAux[8] == 'reservado\n' :
                            print('\nEl vehículo', informacionAux[1], 'no se puede eliminar. \nSe encuentra reservado para un viaje')
                            anadir_texto_vehiculo(informacion)
                        else :
                            print('El vehículo', informacionAux[1], 'con placa', informacionAux[0], 'ha sido eliminado')
                else :
                    if contador == 0 :
                        contador += 1
                        escribir_texto_vehiculo(informacion)
                    else :
                        anadir_texto_vehiculo(informacion)
            return transporte_por_empresas()
        else :
            print('\nNo hay coincidencias')
            return transporte_por_empresas()
    else :
        print('\nLa placa debe tener seis caracteres')
        return transporte_por_empresas()
                
def escribir_texto_vehiculo(vehiculo) :
    archivo = open('vehiculos.txt', 'w')
    archivo.write(vehiculo)
    archivo.close()

def anadir_texto_vehiculo(vehiculo) :
    archivo = open('vehiculos.txt', 'a')
    archivo.write(vehiculo)
    archivo.close()               

def comprobar_existencia_placa_eliminar(placa) :
    vehiculo = open('vehiculos.txt', 'r')
    for comparacion in vehiculo.readlines() :
        comparacion = comparacion.split(';')
        vehiculo.close()
        if comparacion[0] == placa :
            return True
    return False

#Nombre: modificar transporte
#Entradas: se introduce el número de placa para encontrar el vehículo que se desea nodificar
#Salidas: Debe guardar la información del vehículo modificado o bien la misma informacion, en caso de que se cancele la modificación.
#Restricciones: La placa debe ser de seis caracteres.
def modificar_transporte():
    placa = str(input('Ingrese la placa del vehículo que desea modificar: '))
    if cuenta_caracteres(placa, 0) == 6 :
        if comprobar_existencia_placa_eliminar(placa) :
            vehiculo = open('vehiculos.txt', 'r')
            contador = 0
            for informacion in vehiculo.readlines() :
                informacionAux = informacion.split(';')
                if informacionAux[0] == placa :
                    print('Modificando al vehículo marca', informacionAux[1])
                    vehiculoModificado = modificar_transporteAux(informacionAux, informacionAux)
                    if contador == 0 :
                        contador += 1
                        escribir_texto_vehiculo(vehiculoModificado)
                    else :
                        anadir_texto_vehiculo(vehiculoModificado)
                else :
                    if contador == 0 :
                        contador += 1
                        escribir_texto_vehiculo(informacion)
                    else :
                        anadir_texto_vehiculo(informacion)
            return transporte_por_empresas()
        else :
            print('No hay coincidencias')
            return transporte_por_empresas()
    else :
        print('\nLa placa debe tener seis caracteres')
        return transporte_por_empresas()

def modificar_transporteAux(informacion, informacionOriginal) :
    print("""
¿Qué desea modificar?
1. Placa
2. Marca
3. Modelo
4. Año
5. Asientos VIP
6. Asientos normales
7. Asientos económicos
9. Guardar
0. Cancelar""")
    opcion = str(input('\nIngrese la opción deseada: '))
    if opcion == '1' :
        placa = str(input('\nIngrese la nueva placa del vehículo: '))
        if cuenta_caracteres(placa, 0) == 6 :
            if comprobar_existencia_placa_eliminar(placa) :
                print('La placa introducida ya existe, debe poner una diferente')
                return modificar_transporteAux(informacion, informacionOriginal)
            else :
                informacion[0] = placa
                print('Placa asignado')
                return modificar_transporteAux(informacion, informacionOriginal)
        else :
            print('Las placas deben de ser de seis caracteres')
            return modificar_transporteAux(informacion, informacionOriginal)
    elif opcion == '2' :
        marca = str(input('\nIngrese la nueva marca del vehículo: '))
        informacion[1] = marca
        print('Marca asignada')
        return modificar_transporteAux(informacion, informacionOriginal)
    elif opcion == '3' :
        modelo = str(input('\nIngrese la nueva modelo del vehículo: '))
        informacion[2] = modelo
        print('Modelo asignado')
        return modificar_transporteAux(informacion, informacionOriginal)
    elif opcion == '4' :
        año  = str(input('\nIngrese el nuevo año del vehículo: '))
        if comprobador_entero(año, 0) == 2 :
            if cuenta_caracteres(año, 0) == 4 :
                informacion[3] = año
                print('Año asignado')
                return modificar_transporteAux(informacion, informacionOriginal)
            else :
                print('El año debe tener cuatro digitos')
                return modificar_transporteAux(informacion, informacionOriginal)
        else :
            print('\nDebe ingresar un número entero')
            return modificar_transporteAux(informacion, informacionOriginal)
    elif opcion == '5' :
        VIP = str(input('Ingrese la nueva cantidad de asientos VIP: '))
        if comprobador_entero(VIP, 0) == 2 :
            informacion[5] = VIP
            print('Asientos VIP asignados')
            return modificar_transporteAux(informacion, informacionOriginal)
        else :
            print('\nDebe ingresar un número entero')
            return modificar_transporteAux(informacion, informacionOriginal)
    elif opcion == '6' :
        normales = str(input('Ingrese la nueva cantidad de asientos VIP: '))
        if comprobador_entero(normales, 0) == 2 :
            informacion[5] = normales
            print('Asientos normales asignados')
            return modificar_transporteAux(informacion, informacionOriginal)
        else :
            print('\nDebe ingresar un número entero')
            return modificar_transporteAux(informacion, informacionOriginal)
    elif opcion == '7' :
        economicos = str(input('Ingrese la nueva cantidad de asientos VIP: '))
        if comprobador_entero(economicos, 0) == 2 :
            informacion[5] = economicos
            print('Asientos económicos asignados')
            return modificar_transporteAux(informacion, informacionOriginal)
        else :
            print('\nDebe ingresar un número entero')
            return modificar_transporteAux(informacion, informacionOriginal)
    elif opcion == '9' :
        nuevaInformacion = (informacion[0] + ';' + informacion[1] + ';' + informacion[2] + ';' + informacion[3] + ';' + informacion[4] + ';' + informacion[5] + ';' +
                            informacion[6] + ';' + informacion[7] + ';' + informacion[8])
        print('Se han guardado los cambios')
        return nuevaInformacion
    elif opcion == '0' :
        informacionAntigua = (informacionOriginal[0] + ';' + informacionOriginal[1] + ';' + informacionOriginal[2] + ';' + informacionOriginal[3] + ';' +
                              informacionOriginal[4] + ';' + informacionOriginal[5] + ';' + informacionOriginal[6] + ';' + informacionOriginal[7] + ';' +
                              informacionOriginal[8])
        print('No se han guardado los cambios')
        return informacionAntigua
    else :
        print('\nPor favor, introduzca una opcion válida\n')
        return transporte_por_empresas()
#Nombre: mostrar transportes
#Se ejecuta y muestra todos los transportes registrados
def mostrar_transportes():
    transportes = open('vehiculos.txt', 'r')
    for vehiculo in transportes.readlines() :
        vehiculo = vehiculo.split(';')
        print('Placa:', vehiculo[0])
        print('Marca:', vehiculo[1])
        print('Modelo:', vehiculo[2])
        print('Año:', vehiculo[3])
        print('Empresa:', vehiculo[4])
        print('Asientos VIP:', vehiculo[5])
        print('Asientos normales:', vehiculo[6])
        print('Asientos economicos:', vehiculo[7])
        print('Estado:', vehiculo[8])
    return transporte_por_empresas()

#Nombre: gestion de viaje
#Entradas: Ingresa una de las opciones que se presentan en el menú
#Salidas: Una de las dunciones seleccionadassegún el menú, ya sea, incluir viajes, eliminar viajes, modificar viajes o mostrar viajes.
#Restrcciones: Solo se permite ingresar de las opciones que se muestran en el menú.
def gestión_de_viaje() :
    print("""
        Gestiòn de viajes
1. Incluir viajes
2. Eliminar viajes
3. Modificar viajes
4. Mostrar Viajes
9. Salir""")
    opcion = str(input('\nIngrese la opción deseada: '))
    if opcion == '1' :
        return incluir_viajes()
    elif opcion == '2' :
        return eliminar_viajes()
    elif opcion == '3' :
        return modificar_viajes()
    elif opcion == '4' :
        return mostrar_viajes()
    elif opcion == '9' :
        return opciones_administrativas()
    else :
        print('\nPor favor, introduzca una opcion válida\n')
        return gestión_de_viaje()

#Nombre: Incluir viajes
#Sirve para incluir viajes en la carpeta viajes.txt y así guardarlos para manipular su información en otras opciones.
def incluir_viajes() :
    ciudadSalida = str(input('Introduzca la ciudad de salida: '))
    ciudadLlegada = str(input('Introduzca la ciudad de llegada: '))
    añoSalida = str(input('Introduzca el año de salida: '))
    if comprobador_entero(añoSalida, 0) == 2 :
        if cuenta_caracteres(añoSalida, 0) == 4 :
            mesSalida = str(input('Introduzca el mes de salida: '))
            if comprobador_entero(mesSalida, 0) == 2 :
                if int(mesSalida) <= 12 and int(mesSalida) > 0 :
                    diaSalida = str(input('Introduzca el día de salida: '))
                    if comprobador_entero(diaSalida, 0) == 2 :
                        if int(diaSalida) <= 31 and int(diaSalida) > 0 :
                            horaSalida = str(input('Introduzca la hora de salida (Formato 24 horas): '))
                            if comprobador_entero(horaSalida, 0) == 2 :
                                if int(horaSalida) <= 23 and int(horaSalida) >= 0 :
                                    minutoSalida = str(input('Introduzca el minuto de salida: '))
                                    if comprobador_entero(minutoSalida, 0) == 2 :
                                        if int(minutoSalida) <= 59 and int(minutoSalida) >= 0 :
                                            añoLlegada = str(input('Introduzca el año de llegada: '))#A partir de aqui empienza la fecha de salida
                                            if comprobador_entero(añoLlegada, 0) == 2 :
                                                if cuenta_caracteres(añoLlegada, 0) == 4 :
                                                    mesLlegada = str(input('Introduzca el mes de llegada: '))
                                                    if comprobador_entero(mesLlegada, 0) == 2 :
                                                        if int(mesLlegada) <= 12 and int(mesLlegada) > 0 :
                                                            diaLlegada = str(input('Introduzca el día de llegada: '))
                                                            if comprobador_entero(diaLlegada, 0) == 2 :
                                                                if int(diaLlegada) <= 31 and int(diaLlegada) > 0 :
                                                                    horaLlegada = str(input('Introduzca la hora de llegada (Formato 24 horas): '))
                                                                    if comprobador_entero(horaLlegada, 0) == 2 :
                                                                        if int(horaLlegada) <= 23 and int(horaLlegada) >= 0 :
                                                                            minutoLlegada = str(input('Introduzca el minuto de llegada: '))
                                                                            if comprobador_entero(minutoSalida, 0) == 2 :
                                                                                if int(minutoSalida) <= 59 and int(minutoSalida) >= 0 :
                                                                                    montoVIP = str(input('Ingrese el monto del asiento VIP: '))
                                                                                    if comprobador_entero(montoVIP, 0) == 2 :
                                                                                        montoNormal = str(input('Ingrese el monto del asiento normal: '))
                                                                                        if comprobador_entero(montoNormal, 0) == 2 :
                                                                                            montoEconomico = str(input('Introduzca el monto económico: '))
                                                                                            if comprobador_entero(montoEconomico, 0) == 2 :
                                                                                                empresa = str(input('Ingrese la cédula jurídica de la empresa que realiza el viaje: '))
                                                                                                if comprobador_entero(empresa, 0) == 2 :
                                                                                                    if cuenta_caracteres(empresa, 0) == 10 :
                                                                                                        if comprobar_existencia_empresa(empresa) :
                                                                                                            vehiculo = str(input('Ingrese la placa del vehículo que desea usar: '))
                                                                                                            if cuenta_caracteres(vehiculo, 0) == 6 :
                                                                                                                if comprobar_existencia_placa_eliminar(vehiculo) :
                                                                                                                    if comprobar_reservacion_de_vehiculo(vehiculo) :
                                                                                                                        from datetime import datetime
                                                                                                                        fecha1 = datetime(int(añoSalida), int(mesSalida), int(diaSalida), int(horaSalida),
                                                                                                                                          int(minutoSalida))
                                                                                                                        fecha2 = datetime(int(añoLlegada), int(mesLlegada), int(diaLlegada),
                                                                                                                                          int(horaLlegada), int(minutoLlegada))
                                                                                                                        if fecha2 > fecha1 :
                                                                                                                            numeroViaje = verificar_numero_de_viaje()
                                                                                                                            informacionViaje = (numeroViaje + ';' + ciudadSalida + ';' + ciudadLlegada +
                                                                                                                                                ';' + añoSalida + ';' + mesSalida + ';' + diaSalida + ';'
                                                                                                                                                + horaSalida + ';' + minutoSalida + ';' + añoLlegada + ';'
                                                                                                                                                + mesLlegada + ';' + diaLlegada + ';' + horaLlegada + ';'
                                                                                                                                                + minutoLlegada + ';' + empresa + ';' + vehiculo + ';'
                                                                                                                                                + montoVIP + ';' + montoNormal + ';' +
                                                                                                                                                montoEconomico + '\n')
                                                                                                                            registrarViaje = open('viajes.txt', 'a')
                                                                                                                            registrarViaje.write(informacionViaje)
                                                                                                                            registrarViaje.close()
                                                                                                                            print('Se ha añadido el viaje #',numeroViaje)
                                                                                                                            reservar_vehiculo(vehiculo)
                                                                                                                            return gestión_de_viaje()
                                                                                                                        else :
                                                                                                                            print('\nLa fecha de llegada no puede ser menor que la fecha de salida')
                                                                                                                            return gestión_de_viaje()
                                                                                                                    else :
                                                                                                                        print('El vehículo no se puede usar, debido a que se encuentra reservado para otro viaje')
                                                                                                                        return gestión_de_viaje()
                                                                                                                else :
                                                                                                                    print('La placa ingresada no posee coincidencias')
                                                                                                                    return gestión_de_viaje()
                                                                                                            else :
                                                                                                                print('La placa del vehículo debe tener seis dígitos')
                                                                                                                return gestión_de_viaje()
                                                                                                        else :
                                                                                                            print('La jurídica ingresada no posee coincidencias')
                                                                                                            return gestión_de_viaje()
                                                                                                    else :
                                                                                                        print('La cédula jurídica debe ser de seis dígitos')
                                                                                                        return gestión_de_viaje()
                                                                                                else :
                                                                                                    print('La cedula jurídica deben de ser números')
                                                                                                    return gestión_de_viaje()
                                                                                            else :
                                                                                                print('El precio económico debe de ser números')
                                                                                                return gestión_de_viaje()
                                                                                        else :
                                                                                            print('El precio normal debe de ser números')
                                                                                            return gestión_de_viaje()
                                                                                    else :
                                                                                        print('El precio VIP debe de ser números')
                                                                                        return gestión_de_viaje()
                                                                                else :
                                                                                    print('Los minutos de llegada deben ser mayores o iguales que cero y menores o iguales que cincuenta y nueve')
                                                                                    return gestión_de_viaje()
                                                                            else :
                                                                                print('Los minutos deben de ser números')
                                                                                return gestión_de_viaje()
                                                                        else :
                                                                            print('La hora de llegada debe ser mayor o igual que cero y menor o igual que veinti tres')
                                                                            return gestión_de_viaje()
                                                                    else :
                                                                        print('La hora deben de ser numeros')
                                                                        return gestión_de_viaje()
                                                                else :
                                                                    print('El dia de llegada debe de ser mayor que cero y menor o igual que treinta y uno')
                                                                    return gestión_de_viaje()
                                                            else :
                                                                print('El dia de llegada debe ser un número entero')
                                                                return gestión_de_viaje()
                                                        else :
                                                            print('El mes de llegada debe ser mayor que cero y menor o igual que 12')
                                                            return gestión_de_viaje()
                                                    else :
                                                        print('El mes de llegada debe ser un número')
                                                        return gestión_de_viaje()
                                                else :
                                                    print('El año de llegada debe tener cuatro dígitos')
                                                    return gestión_de_viaje()
                                            else :
                                                print('El año de llegada debe ser un número')
                                                return gestión_de_viaje()
                                        else :
                                            print('Los minutos de salida deben ser mayores o iguales que cero y menores o iguales que cincuenta y nueve')
                                            return gestión_de_viaje()
                                    else :
                                        print('Los minutos de salida deben de ser números')
                                        return gestión_de_viaje()
                                else :
                                    print('La hora de salida debe ser mayor o igual que cero y menor o igual que veinti tres')
                                    return gestión_de_viaje()
                            else :
                                print('La hora deben de ser numeros')
                                return gestión_de_viaje()
                        else :
                            print('El dia de salida debe de ser mayor que cero y menor o igual que treinta y uno')
                            return gestión_de_viaje()
                    else :
                        print('El dia de salida debe ser un número entero')
                        return gestión_de_viaje()
                else :
                    print('El mes de salida debe ser mayor que cero y menor o igual que 12')
                    return gestión_de_viaje()
            else :
                print('El mes de salida debe ser un número')
                return gestión_de_viaje()
        else :
            print('El año de salida debe tener cuatro dígitos')
            return gestión_de_viaje()
    else :
        print('El año de salida debe ser un numero')

def verificar_numero_de_viaje() :
    numeroViaje = open('numeroViaje.txt', 'r')
    numero = numeroViaje.read()
    numeroViaje.close()
    numeroViajeActual = int(numero) + 1
    guardarNumero = open('numeroViaje.txt', 'w')
    guardarNumero.write(str(numeroViajeActual))
    guardarNumero.close()
    return str(numeroViajeActual)

def comprobar_reservacion_de_vehiculo(placa) :
    informacion = open('vehiculos.txt', 'r')
    for vehiculo in informacion.readlines() :
        vehiculo = vehiculo.split(';')
        informacion.close()
        if vehiculo[0] == placa :
            if vehiculo[8] == 'reservado\n' :
                return False
            else :
                vehiculo
        else :
            vehiculo
    return True

def reservar_inactivar_vehiculo(placa) :
    contador = 0
    informacion = open('vehiculos.txt', 'r')
    for vehiculo in informacion.readlines() :
        vehiculoAux = vehiculo.split(';')
        informacion.close()
        if vehiculoAux[0] == placa :
            if vehiculoAux[8] == 'reservado\n' :
                vehiculoAux[8] = 'inactivo\n'
                vehiculoReservado = (vehiculoAux[0] + ';' + vehiculoAux[1] + ';' + vehiculoAux[2] + ';' + vehiculoAux[3] + ';' + vehiculoAux[4] + ';' + vehiculoAux[5] + ';' + vehiculoAux[6]
                                 + ';' + vehiculoAux[7] + ';' + vehiculoAux[8])
                if contador == 0 :
                    contador += 1
                    escribir_texto_vehiculo(vehiculoReservado)
                else :
                    anadir_texto_vehiculo(vehiculoReservado)

            else :
                vehiculoAux[8] = 'reservado\n'
                vehiculoReservado = (vehiculoAux[0] + ';' + vehiculoAux[1] + ';' + vehiculoAux[2] + ';' + vehiculoAux[3] + ';' + vehiculoAux[4] + ';' + vehiculoAux[5] + ';' + vehiculoAux[6]
                                     + ';' + vehiculoAux[7] + ';' + vehiculoAux[8])
                if contador == 0 :
                    contador += 1
                    escribir_texto_vehiculo(vehiculoReservado)
                else :
                    anadir_texto_vehiculo(vehiculoReservado)
        else :
            if contador == 0 :
                contador += 1
                escribir_texto_vehiculo(vehiculo)
            else :
                anadir_texto_vehiculo(vehiculo)

#Nombre: eliminar viajes
#Entradas: introduce el numero de viaje
#Salidas: Elimina del sistema el viaje, liberando el vehiculo que estaba.
def eliminar_viajes() :
    numeroViaje = str(input('Itroduzca el número de viaje que desea eliminar: '))
    if comprobador_entero(numeroViaje, 0) == 2 :
        contador = 0
        coincidencias = 0
        registrarViaje = open('viajes.txt', 'r')
        for informacion in registrarViaje.readlines() :
            informacionAux = informacion.split(';')
            registrarViaje.close()
            if informacionAux[0] == numeroViaje :
                coincidencias += 1
                reservar_inactivar_vehiculo(informacionAux[14])
                print('El viaje ha sido eliminado')
            else :
                if contador == 0 :
                    contador += 1
                    escribir_viaje(informacion)
                else :
                    anadir_viaje(informacion)
        if coincidencias == 0 :
            print('No se han encontrado coincidencias')
            return gestión_de_viaje()
        else :
            return gestión_de_viaje()
    else :
        print('Debe introducir un NUMERO de viaje')

def escribir_viaje(informacion) :
    viaje = open('viajes.txt', 'w')
    viaje.write(informacion)
    viaje.close()

def anadir_viaje(informacion) :
    viaje = open('viajes.txt', 'a')
    viaje.write(informacion)
    viaje.close()

#
def modificar_viaje() :
    numeroViaje = str(input('Ingrese el número de viaje que desea modificar: '))
    if comprobador_entero(numeroViaje, 0) == 2 :
        contador = 0
        coincidencias = 0
        viaje = open('viajes.txt', 'r')
        for informacion in viaje.readlines() :
            informacionAux = informacion.split(';')
            viaje.close()
            if informacionAux[0] == numeroViaje :
                nuevaInformacion = modificando_viaje(informacionAux, informacion)
                if contador == 0 :
                    coincidencias += 1
                    escribir_viaje(nuevaInformacion)
                else :
                    anadir_viaje(nuevaInformacion)
            else :
                if contador == 0 :
                    coincidencias += 1
                    escribir_viaje(informacion)
                else :
                    anadir_viaje(informacion)
    if coincidencias == 0 :
        print('No hay coincidencias')
        return gestión_de_viaje()
    else :
        return gestión_de_viaje()

def modificando_viaje(informacion, informacionOriginal) :
    print("""
        Modificando Viaje
1. Ciudad de salida
2. Ciudad de llegada
3. Fecha de salida
4. Fecha de llegada
5. Vehículo
6. Monto VIP
7. Monto Normal
8. Monto económico
9. Guardar
0. Cancelar""")
    opcion = str(input('\nIngrese la opción deseada: '))
    if opcion == '1' :
        return modificando_viaje(informacion, informacionOriginal)
    elif opcion == '2' :
        return modificando_viaje(informacion, informacionOriginal)
    elif opcion == '3' :
        return modificando_viaje(informacion, informacionOriginal)
    elif opcion == 4 :
        return modificando_viaje(informacion, informacionOriginal)
    elif opcion == 5 :
        return modificando_viaje(informacion, informacionOriginal)
    elif opcion == 6 :
        return modificando_viaje(informacion, informacionOriginal)
    elif opcion == 7 :
        return modificando_viaje(informacion, informacionOriginal)
    elif opcion == 8 :
        return modificando_viaje(informacion, informacionOriginal)
    elif opcion == 9 :
        nuevaInformacion = (informacion[0] + ';' + informacion[1] + ';' + informacion[2] + ';' + informacion[3] + ';' + informacion[4] + ';' +
                            informacion[5] + ';' + informacion[6] + ';' + informacion[7] + ';' + informacion[8] + ';' + informacion[9] + ';' +
                            informacion[10] + ';' + informacion[11] + ';' + informacion[12] + ';' + informacion[13] + ';' + informacion[14] + ';' +
                            informacion[15] + ';' + informacion[16] + ';' + informacion[17])
        print('Cambios guardados')
        return nuevaInformacion
    elif opcion == 0 :
        print('Cambios descartados')
        return informacionOriginal
    else :
        print('\nIngrese una opcion valida')
        return modificando_viaje(informacion, informacionOriginal)
    

#
def mostrar_viajes() :
    contador = 0
    viajes = open('viajes.txt', 'r')
    for informacion in viajes.readlines() :
        informacion = informacion.split(';')
        if informacion[0] == 'inicio':
            viajes.close()
        else :
            viajes.close()
            print('Número de viaje:', informacion[0])
            print('Ciudad de salida:', informacion[1])
            print('Ciudad de llegada:', informacion[2])
            print('Fecha de salida:', informacion[5],'/', informacion[4],'/', informacion[3],' ', informacion[6],':', informacion[7])
            print('Fecha de llegada:', informacion[10],'/', informacion[9],'/', informacion[8],' ', informacion[11],':', informacion[12])
            print('Empresa:', mostrar_nombre_empresa(informacion[13]))
            print('Placa del vehículo:', informacion[14])
            print('Precio asiento VIP:', informacion[15])
            print('Precio asiento normal', informacion[16])
            print('Precio asiento económico', informacion[17])
            contador += 1
    if contador == 0 :
        print('No hay viajes registrados')
        return gestión_de_viaje()
    else :
        return gestión_de_viaje()

def mostrar_nombre_empresa(cedula) : #Muestra el nombre de la empresa introduciendo el numero de cedula juridica
    empresa = open('empresas.txt', 'r')
    for informacion in empresa.readlines() :
        informacion = informacion.split(';')
        empresa.close()
        if informacion[1] == cedula :
            return informacion[0]
        else :
            None
