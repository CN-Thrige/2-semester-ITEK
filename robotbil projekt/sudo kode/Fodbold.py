from time import sleep

def SigmaMode():
    try:
        print("What the sigma, jeg bliver fjernstyret af en controller")
        sleep(1)
        return SigmaMode()
    except KeyboardInterrupt:
        pass