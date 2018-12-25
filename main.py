from Classes import Ship
from Classes import ShipLoader
from FileExchange import FileExchange

from RandomGenerators import ContainerGenerator

ship = Ship(1, 250, 900, 10, 150)
ports = FileExchange.LoadAllDataFromFile('ExampleContainerList.txt')

not_resolved_ports = 0
for port in ports:
    not_resolved_ports = not_resolved_ports + port.not_resolved
while not_resolved_ports > 0:
    not_resolved_ports = 0
    for port in ports:
        not_resolved_ports = not_resolved_ports + port.not_resolved
    for port in ports:
        port.resolve_port()

FileExchange.SaveAllDataToFile('result.txt', ports)
print(str(len(ports[0].containers)) + " containers left in port 1\n")
print(str(len(ports[1].containers)) + " containers left in port 2\n")

