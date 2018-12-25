from random import randint
from Classes import Container
from Classes import Timestamp
import math


class ContainerGenerator:

    @staticmethod
    def GenerateContainer(ID, size_x, size_y, size_z, deviation, destination):
        deviation_random = randint(-deviation, deviation)
        deviation_percentage = deviation_random / 100
        container_size_x = math.floor(size_x + size_x * deviation_percentage)
        container_size_y = math.floor(size_y + size_y * deviation_percentage)
        container_size_z = size_z

        container = Container(ID, container_size_x, container_size_y, container_size_z,
                              Timestamp(randint(1, 12), randint(1, 30), randint(2019, 2022)), destination)
        return container
