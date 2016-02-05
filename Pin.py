import RPi.GPIO as GPIO
class Pin:
    def __init__(self,numero,estado):
        GPIO.setup(numero, GPIO.IN)
        #print "estado:" + str(GPIO.input(numero))
        self.pin = numero
        self.nombre = "pin"+str(numero)
        self.estado = estado
        self.alarma = estado

    def getNumero(self):
        return self.pin

    def getEstado(self):
        #capturar de la libreria
        #return self.estado
        return GPIO.input(self.pin)

    def getAnterior(self):
        return self.alarma

    def getNombre(self):
        return self.nombre

    def setEstado(self,est):
        self.estado=est

    def setAnterior(self):
        self.alarma=self.estado

