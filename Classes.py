import pygame
from math import pi

WHITE = (255, 255, 255)
BASE_COLOR = {0, 0, 0}


class ShipLoader:
    @staticmethod
    def Load_ship(ship, container_list):
        container_list.sort(key=lambda x: x.mass, reverse=True)

        containers_to_remove = []
        for contain in container_list:
            if (ship.load_container(contain) == 0):
                containers_to_remove.append(contain)

        for contain in containers_to_remove:
            container_list.remove(contain)

        if len(container_list) == 0:
            print("loaded all the containers")
        else:
            print("couldn't load all the containers")


class Ship:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y
        self.containers = []
        self.decks = []
        self.decks.append(Deck(_x, _y, 0, 0))

    def load_container(self, container):
        loaded = 0
        for deck in self.decks:
            if loaded == 0:
                if (self.load_container_on_deck(deck, container) == 0):
                    loaded = 1;

        if loaded == 1:
            print("container loaded sucesfully \n")
            return 0
        else:
            print("cannot load the container \n")
            return 1

    def load_container_on_deck(self, deck, container):
        if (container.x <= deck.x and container.y <= deck.y):
            load = 1;
        elif (container.y <= deck.x and container.x <= deck.y):
            temp = container.x
            container.x = container.y
            container.y = temp
            load = 1;
        else:
            load = 0;

        if load == 1:
            new_deck1 = Deck(deck.x - container.x, deck.y, deck.origin_x + container.x, deck.origin_y)
            new_deck2 = Deck(container.x, deck.y - container.y, deck.origin_x, deck.origin_y + container.y)
            self.decks.remove(deck)
            self.decks.append(new_deck2)
            self.decks.append(new_deck1)
            container.position_x = deck.origin_x
            container.position_y = deck.origin_y
            self.containers.append(container)
            return 0
        else:
            return 1

    def display_ship(self):
        pygame.init()
        screen = pygame.display.set_mode((self.x, self.y))

        clock = pygame.time.Clock()

        running = True

        # main loop
        while running:
            clock.tick(10)
            # event handling, gets all event from the eventqueue
            for event in pygame.event.get():
                # only do something if the event is of type QUIT
                if event.type == pygame.QUIT:
                    # change the value to False, to exit the main loop
                    running = False
            color_loop = 100
            color = 1
            for container in self.containers:
                if color == 1:
                    COLOR = [color_loop, 0, 0]
                elif color == 2:
                    COLOR = [0, color_loop, 0]
                else:
                    COLOR = [0, 0, color_loop]
                pygame.draw.rect(screen, COLOR, [container.position_x, container.position_y, container.x, container.y],
                                 0)
                color_loop = color_loop + 10
                color = color + 1
                if color_loop >= 255:
                    color_loop = 100
                if color == 4:
                    color = 1

            pygame.display.flip()

        pygame.quit()


class Deck:
    def __init__(self, _x, _y, _origin_x, _origin_y):
        self.x = _x
        self.y = _y
        self.origin_x = _origin_x
        self.origin_y = _origin_y


class Container:
    def __init__(self, _ID, _x, _y, _mass):
        self.x = _x
        self.y = _y
        self.ID = _ID
        self.mass = _mass
        self.position_x = 0;
        self.position_y = 0;
