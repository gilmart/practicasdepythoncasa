edad=int(input('Digite la edad: '))

if(edad >=0 and edad < 15):
    print('etapa niño')
elif(edad >=15 and edad <28):
    print('etapa jove')
elif(edad >=28 and edad <61):
    print('etapa adulto')
elif(edad >=61 and edad <111):
    print('etapa adulto mayor')
elif(edad <0 or edad >110):
    print('edad incorrecta')
else:
    print('intente nuevamente, ingrese un numero correcto')