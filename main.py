from Classes import Ship
from Classes import Container
from Classes import ShipLoader

ship = Ship(1, 200, 500)
container = Container(432, 30, 65, 1950)
container2 = Container(443, 30, 65, 1950)
container3 = Container(443, 30, 65, 1950)
container4 = Container(443, 100, 200, 20000)
container5 = Container(443, 300, 100, 30000)

container_list = []
containers_to_remove = []
container_list.append(container)
container_list.append(container2)
container_list.append(container5)
container_list.append(container4)
container_list.append(container3)

ShipLoader.Load_ship(ship, container_list)

ship.display_ship()
