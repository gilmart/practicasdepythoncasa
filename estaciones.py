mes = input(f'digite el mes: ')
if(mes == 'enero' or mes == 'febrero' or mes == 'marzo'):
    print(f'La estacion es invierno')
elif(mes == 'abril' or mes == 'mayo' or mes == 'junio'):
    print(f'La estacion es primavera')
elif(mes == 'julio' or mes == 'agosto' or mes == 'septiembre'):
    print(f'La estacion es verano')
elif(mes == 'octubre' or mes == 'noviembre' or mes == 'diciembre'):
    print(f'La estacion es otoño')
else: 
    print('digite un mes correcto')

