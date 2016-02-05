
from ABE_ExpanderPi import RTC
from ABE_helpers import ABEHelpers
import time
from Pin import Pin

class Alarma:
    def __init__(self):
        i2c_helper = ABEHelpers()
        bus = i2c_helper.get_smbus()
        self.rtc = RTC(bus)
        print("Alarma")

    def cargarAlarmas(self):
            myvar = open("logAlarma.txt", 'r')
            line = myvar.readlines()
            lines = line[-100:]
            myvar.close()
            cadena=""
            for texto in lines:
                cadena=cadena+texto
            print("termino")
            return cadena
            #return line

    def abrirArchivo(self, cadena):
            mylist = open("logAlarma.txt",'a')
            mylist.write(cadena + '\n')
            mylist.close()

    def verAlarma(self,pin):
        print("Este es el estado: "+str(pin.getEstado())+" "+str(0))
        print("Este es el anterior: "+str(pin.getAnterior()))
        
        if(str(pin.getEstado())==str(0) and str(pin.getAnterior())==str(1)):
			print("true")
			pin.setAnterior()
			return True
        if(str(pin.getEstado())==str(1) and str(pin.getAnterior())==str(0)):
			print("false")
			pin.setAnterior()
			return False
		
        return False

    def getMensajeAlarma(self, pin):
        if(str(pin)=="13"):
            mensaje= "LOCK FAIL\t\t"+self.rtc.read_date()
        if(str(pin)=="19"):
            mensaje= "PA FAIL\t\t"+self.rtc.read_date()
        if(str(pin)=="16"):
            mensaje= "300V FAIL\t\t"+self.rtc.read_date()
        if(str(pin)=="26"):
            mensaje= "PDM FAIL\t\t"+self.rtc.read_date()
        if(str(pin)=="20"):
            mensaje= "REFLEJADA\t\t"+self.rtc.read_date()
        if(str(pin)=="21"):
            mensaje= "SOBRECORRIENTE\t"+self.rtc.read_date()
        self.abrirArchivo(mensaje)
        return mensaje


