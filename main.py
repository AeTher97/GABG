from Classes import Ship
from Classes import ShipLoader
from FileExchange import FileExchange

from RandomGenerators import ContainerGenerator

ship = Ship(1, 250, 900, 10, 150)
ports = FileExchange.LoadAllDataFromFile('ExampleContainerList.txt')

ports[0].load_ship(1, 2, True)
ports[0].load_ship(2, 2, True)

ports[0].ships[0].display_ship()
ports[0].ships[1].display_ship()

print(str(len(ports[0].containers)) + " containers left in port 1\n")
print(str(len(ports[1].containers)) + " containers left in port 2\n")

# FileExchange.SaveShip('ExampleShip.txt',ports[0].ships[0])
# if (FileExchange.LoadShipFromFile('ExampleShip.txt') != None):
#   FileExchange.LoadShipFromFile('ExampleShip.txt').display_ship()
