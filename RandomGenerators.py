from random import randint
from Classes import Container
import math


class ContainerGenerator:

    @staticmethod
    def GenerateContainer(size_x, size_y, size_z, deviation):
        deviation_random = randint(0, deviation)
        deviation_percentage = deviation_random / 100
        container_size_x = math.floor(size_x + size_x * deviation_percentage)
        container_size_y = math.floor(size_y + size_y * deviation_percentage)
        container_size_z = size_z

        container = Container(randint(0, 5000), container_size_x, container_size_y, container_size_z)
        return container
