import re
import pandas as pd
from Classes import Port, Ship, Container, Timestamp


def ParseLine(line, rx):
    for key, rx in rx.items():
        match = rx.search(line)
        if match:
            return key, match

    return None, None


class FileExchange:

    @staticmethod
    def LoadContainersFromFile(path):
        port_list = []
        data = []
        rx_dict = {
            'port': re.compile(r'Port (?P<PortID>\d+) Capacity: (?P<Capacity>\d+)'),
            'ship': re.compile(
                r'Ship ID: (?P<ShipID>\d+) X: (?P<X>\d+) Y: (?P<Y>\d+) Z: (?P<Z>\d+) Capacity: (?P<Capacity>\d+)\n'),
            'container': re.compile(
                r'Container ID: (?P<ContainerID>\d+) X: (?P<X>\d+) Y: (?P<Y>\d+) Z: (?P<Z>\d+) Timestamp:(?P<Month>\d+)-(?P<Day>\d+)-(?P<Year>\d+) DestinationID: (?P<DestinationID>\d+)')
        }
        with open(path, "r") as file_object:
            line = file_object.readline()
            while line:

                key, match = ParseLine(line, rx_dict)
                if key == 'port':
                    port_id = int(match.group('PortID'))
                    port_capacity = int(match.group('Capacity'))
                    print("PORT ID: " + str(port_id))
                    port_object = Port(port_id, port_capacity)
                    line = file_object.readline()
                    while line.strip():
                        key, match = ParseLine(line, rx_dict)
                        if key == 'ship':
                            ship = int(match.group('ShipID'))
                            x = int(match.group('X'))
                            y = int(match.group('Y'))
                            z = int(match.group('Z'))
                            ship_capacity = int(match.group('Capacity'))
                            ship_ID = int(ship)
                            print("SHIP ID: " + str(ship_ID) + " X: " + str(x) + " Y: " + str(y) + " Z: " + str(
                                z) + " Capacity: " + str(ship_capacity))
                            ship_object = Ship(ship, x, y, z, ship_capacity)
                            port_object.add_ship(ship_object)

                        if key == 'container':
                            container = int(match.group('ContainerID'))
                            x = int(match.group('X'))
                            y = int(match.group('Y'))
                            z = int(match.group('Z'))
                            month = int(match.group('Month'))
                            day = int(match.group('Day'))
                            year = int(match.group('Year'))
                            destination = int(match.group('DestinationID'))
                            timestamp = Timestamp(month, day, year)
                            print("CONTAINER ID: " + str(container) + " X: " + str(x) + " Y: " + str(y) + " Z: " + str(
                                z) + " Date: " + str(month) + "-" + str(day) + "-" + str(year) + " Destination: " + str(
                                destination))
                            container_object = Container(container, x, y, z, timestamp, destination)
                            port_object.add_conatiner(container_object)
                        line = file_object.readline()

                    port_list.append(port_object)
                line = file_object.readline()
        print("readey")
        return port_list

    @staticmethod
    def SaveDataToFile(path):
        file = open(path, "w")
