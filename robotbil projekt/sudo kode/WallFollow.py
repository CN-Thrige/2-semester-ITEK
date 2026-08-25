import Motor
import TofSensor
from time import sleep

def decisionmaking():
    try:
        tof = TofSensor.TOFsensor()
        print(tof)
        if tof >= 60:
            sleep(1)
            return KomTætterPåMur()

        if tof >= 11 and tof <= 59:
            sleep(1)
            return ForsætDetGodeArbejde()

        if tof <= 10:
            sleep(1)
            return KomLidtVækFraMur()
    except:
        KeyboardInterrupt

def KomTætterPåMur():
    sleep(1)
    Motor.DrejTilHøjre()
    Motor.KøreFrem()
    Motor.DrejTilVenstre()
    return decisionmaking()

def KomLidtVækFraMur():
    sleep(1)
    Motor.DrejTilVenstre()
    Motor.KøreFrem()
    Motor.DrejTilHøjre()
    return decisionmaking()


def ForsætDetGodeArbejde():
    sleep(1)
    Motor.KøreFrem()
    return decisionmaking()