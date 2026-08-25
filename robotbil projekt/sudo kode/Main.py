import Fodbold
import SumoCar
import WallFollow

print("Initiating Sigma webserver")
print("Connecting controller")
print("Commense gooning")

while True:
    valg = input("Hvilken mode vil du bruge: ")
    match valg:
        case "fodbold":
            Fodbold.SigmaMode()

        case "sumobil":
            SumoCar.HvadSkalJegGøre()

        case "wallfollow":
            WallFollow.decisionmaking()