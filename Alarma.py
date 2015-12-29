class Alarma:
    def __init__(self):
        print("Alarma")

    def cargarAlarmas(self):
            myvar = open("logAlarma.txt", 'r')
            line = myvar.readlines()
            lines = line[-100:]
            myvar.close()
            cadena=""
            for texto in lines:
                cadena=cadena+texto
            return cadena