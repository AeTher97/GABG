from Classes import Ship
from Classes import ShipLoader
from FileExchange import FileExchange

from RandomGenerators import ContainerGenerator

# ship = Ship(1, 250, 550, 10, 100)
# container_list = []

# for i in range(1, 100):
# container = ContainerGenerator.GenerateContainer(30, 65, 10, 10)
#  container_list.append(container)
# print("number of containers to load " + str(len(container_list)) + "\n")

# ShipLoader.Load_ship(ship, container_list)
# print("number of containers to load " + str(len(container_list)) + "\n")
# ship.display_ship()
# ship.get_ship_information()


# for ship in ports[0].ships:
# ship.display_ship()

ports = FileExchange.LoadAllDataFromFile('ExampleContainerList.txt')
ports[0].load_ship(1)
ports[0].load_ship(2)
ports[1].load_ship(3)
ports[1].load_ship(4)
print(str(len(ports[0].containers)) + " containers left in port 1\n")
print(str(len(ports[1].containers)) + " containers left in port 2\n")
for ship in ports[0].ships:
    ship.display_ship()
for ship in ports[1].ships:
    ship.display_ship()

# FileExchange.SaveShip('ExampleShip.txt',ports[0].ships[0])
if (FileExchange.LoadShipFromFile('ExampleShip.txt') != None):
    FileExchange.LoadShipFromFile('ExampleShip.txt').display_ship()
