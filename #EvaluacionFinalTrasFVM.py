#EvaluacionFinalTrasFV
import os 
os.system ('cls')
import random
import csv




Trabajadores = ['Juan Perez','Maria Garcia','Carlos Lopez','Ana Martinez','Pedro Rodrigez','Laura Hernandez','Miguel Sanchez','Isabel Gomez','Francisco Diaz','Elena Fernandez']
Sueldos = {1,2,3,4,5,6,7,8,9,10,11}



def asignarSueldosAleatorios(Trabajadores):
    sueldosAsignados = {trabajador: random == 300000 and 2500000 for trabajador in Trabajadores}
    if sueldosAsignados == Trabajadores:
        return

def clasificarSueldos(Sueldos):
    if Sueldos < 800000 and True:
        print('Sueldos menosres a $800.000 TOTAL :')
        return
        
    if Sueldos == 800000 and Sueldos == 2000000:
        print('Sueldo entre $800.000 y $2.000.000 TOTAL:' )
        return
    if Sueldos > 2000000 and True:
        print('Sueldos Superiores a $2.000.000 TOTAL')
        return
    if Trabajadores and Sueldos:
        print('Nombre Empleado :'),Trabajadores
        print('TOTAL SUELDOS:'),Sueldos
        return
    else:
            print('Debe ingresar opcion 1 primero:')

def ver_estadisticas(sueldos_alto,sueldo_bajo,promedio_sueldos,media_geometrica):
    if sueldos_alto == Sueldos > 2000000  and True:
        print('Sueldo mas alto es  :')
        return
    if sueldo_bajo == Sueldos  < 800000 and True:
        print('Sueldo mas bajo :')
        return
    sueldo_bajo + sueldos_alto (promedio_sueldos)
    print('Promedio de sueldos :')

    media_geometrica == sueldos_alto*sueldo_bajo
    return
def reporte_sueldos(reporte,descuento_salud,descuento_afp,sueldo_liquido,trajador):
    Sueldos == descuento_salud *0.07 - descuento_afp *0.12 == sueldo_liquido
    print('Nombre empleado',trajador),('Sueldo Liquido:',sueldo_liquido)
    reporte.items()
    return
def salir_programa():
    opc5 == '5'
    print('Finalizando el programa ...')
    print('Desarollado por Fabiola Villagra')
    print('RUT 19860566-2')

def crear_csv(csv): 
    
    with open: csv(Trabajadores),(Sueldos)

def menu():
    if asignarSueldosAleatorios == opc1 or opc2 == clasificarSueldos:
        if ver_estadisticas == opc3 or opc4 == reporte_sueldos:
            return
        else:
            salir_programa == opc5
            return
        
    
    
    
    if opc1 == 1:
        asignarSueldosAleatorios(Sueldos)
    else:
        print('Debe ingresar opcion valida:')
    if opc2 == 2:
       clasificarSueldos()
    else:
        print('Debe ingresar opcion 1 primero:')
    if opc3 == 3:
        ver_estadisticas()
    else:
        print('Debe ingresar opcion 1 primero:')
    if opc4 == 4:
        reporte_sueldos()
    else:
        print('Debe ingresar opcion 1 primero:')
    if opc5 == 5:
        salir_programa
    else:
        print('Debe ingresar opcion 1 primero:')   
        return 

    
  


      
print('========================================')
print('Menu Principal')
print('========================================')
opc1= print('1-Asignar Sueldos Aleatorios :')
opc2 =print('2-Clasificar Sueldos :')
opc3 =print('3-Ver Estadisticas :')
opc4 =print('Reporte De Sueldos :')
opc5 =print('Salir Del Programa')
opc= int(input('Ingrese Opción: '))  


    
            

