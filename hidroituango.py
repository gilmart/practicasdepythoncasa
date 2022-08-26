#ENTRADA DEL PROBLEMA
nivelAgua=int(input('digite el nivel de agua de la prsa: '))

#PROCESO DEL PROBLEMA
if(nivelAgua >=0 and nivelAgua<20):
    print(f'el nivel de agua {nivelAgua} es optimo')
elif(nivelAgua >=20 and nivelAgua <400):
    print(f'el nivel de agua {nivelAgua} es muy alto')
elif(nivelAgua >= 400):
    print(f'el nivel de agua {nivelAgua} es peligroso')
else:
    print(f'ingrese una opcion valida')