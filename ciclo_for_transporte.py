'''Un empresario del transporte cuenta con 30 vehículos entre buses, busetas y colectivos. 
Al final del día se elabora por cada vehículo un registro con la placa, 
el tipo (1= bus, 2= buseta, 3= colectivo) y el número de pasajeros transportados. 

Elabore un algoritmo que imprima por cada vehículo la placa, 
 el dinero recolectado y el pago para el conductor que es el 20 % del total recolectado. 
 También tenga en cuenta que el precio del pasaje en Bus es de $2200.oo, 
en Buseta es de $ 2500.oo y en Colectivos es de $3500.oo.
'''
abus = 0
abuseta = 0
acolectivo = 0

for i in range (30):
    placa = input('Ingrese placa del vehiculo: ')
    tipo = int(input('Ingrese tipo de vehiculo, 1 = bus, 2 = buseta, 3 = colectivo, : '))
    pasajeros = int(input('Ingrese el numero de pasajeros: '))

    if tipo == 1:
        abus = abus + pasajeros
        print('Numero de placa bus: ',placa)
        print()

    elif tipo == 2:
        abuseta = abuseta + pasajeros
        print('Numero de placa buseta: ',placa)
        print()
    
    elif tipo == 3:
        acolectivo = acolectivo + pasajeros
        print('Numero de placa colectivo: ',placa)
        print()
    
    else:
        print('Error ingrese los datos nuevamente')
    


print('Dinero recolectado bus: ',2200 * abus)
print('Pago del conductor bus: ', ((2200 * abus) * 0.2))

print('----------------------------------------------------')

print('Dinero recolectado buseta: ',2500 * abuseta)
print('Pago del conductor buseta: ', ((2500 * abuseta) * 0.2))

print('----------------------------------------------------')

print('Dinero recolectado colectivo: ',3500 * acolectivo)
print('Pago del conductor colectivo: ', ((3500 * acolectivo) * 0.2))

