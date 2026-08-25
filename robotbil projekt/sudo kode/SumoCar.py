import IRSensor
import TofSensor
import Motor
from time import sleep

def HvadSkalJegGøre():
    IR = IRSensor.IRsensor()
    Tof = TofSensor.TOFsensor()
    if IR <= 10 and Tof <= 50:
        sleep(1)
        return KøreEnKasseNed()
    else:
        sleep(1)
        return RetBilenUp()

def KøreEnKasseNed():
    try:
        sleep(1)
        print("Nu Køre Jeg en kasse ned løvebror")
        Motor.KøreFrem()
        Motor.KøreFrem()
        return HvadSkalJegGøre()
    except:
        KeyboardInterrupt

def RetBilenUp():
    try:
        sleep(1)
        print("Drejer lidt rundt type shit")
        return HvadSkalJegGøre()
    except:
        KeyboardInterrupt
