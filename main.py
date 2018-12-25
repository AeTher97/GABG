from Classes import Ship
from Classes import ShipLoader
from FileExchange import FileExchange

from RandomGenerators import ContainerGenerator

ship = Ship(1, 250, 900, 10, 150)

container_list = []
for i in range(0, 150):
    container = ContainerGenerator.GenerateContainer(i + 100, 30, 65, 10, 0, 1)
    container_list.append(container)
ShipLoader.Load_ship(ship, container_list)
ship.display_ship()

# FileExchange.SaveShip('ExampleShip.txt',ports[0].ships[0])
# if (FileExchange.LoadShipFromFile('ExampleShip.txt') != None):
#   FileExchange.LoadShipFromFile('ExampleShip.txt').display_ship()
