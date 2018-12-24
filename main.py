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
##ship.display_ship()
# ship.get_ship_information()

ports = FileExchange.LoadContainersFromFile('ExampleContainerList.txt')
ports[0].load_ship(1)
ports[0].load_ship(2)
for ship in ports[0].ships:
    ship.display_ship()
print()
