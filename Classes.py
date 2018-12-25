import pygame
import datetime
import math


WHITE = (255, 255, 255)
BASE_COLOR = {0, 0, 0}


class ShipLoader:
    @staticmethod
    def Load_ship(ship, container_list):
        container_list.sort(key=lambda x: x.timestamp.date_to_number_of_days(), reverse=False)

        containers_to_remove = []
        for contain in container_list:
            if (ship.load_container(contain) == 0):
                containers_to_remove.append(contain)

        for contain in containers_to_remove:
            container_list.remove(contain)

        for i in range(0, len(ship.decks)):
            ship.merge_deck()

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
    def __init__(self, _ID, _x, _y, _z, _capacity):
        self.ID = _ID
        self.x = _x
        self.y = _y
        self.z = _z
        self.capacity = _capacity
        self.volume = self.x * self.y * self.z
        self.current_capacity = _capacity
        self.current_volume = self.volume
        self.containers = []
        self.decks = []
        self.decks.append(Deck(_x, _y, 0, 0))

    def merge_deck(self):
        merged = 0
        for deck_1 in self.decks:
            for deck_2 in self.decks:
                if deck_1 != deck_2:
                    if deck_2.origin_y >= deck_1.origin_y:

                        if deck_1.origin_y + deck_1.y >= deck_2.origin_y and deck_2.origin_x == deck_1.origin_x + deck_1.x and deck_2.origin_y + deck_2.y >= deck_1.origin_y + deck_1.y:
                            size_of_new_deck = (deck_1.origin_y + deck_1.y - deck_2.origin_y) * (deck_1.x + deck_2.x)
                            if size_of_new_deck > deck_1.size and size_of_new_deck > deck_2.size:
                                new_deck1 = Deck(deck_1.x, deck_2.origin_y - deck_1.origin_y, deck_1.origin_x,
                                                 deck_1.origin_y)
                                new_deck2 = Deck(deck_1.x + deck_2.x, deck_1.origin_y + deck_1.y - deck_2.origin_y,
                                                 deck_1.origin_x, deck_2.origin_y, )
                                new_deck3 = Deck(deck_2.x, deck_2.origin_y + deck_2.y - deck_1.y - deck_1.origin_y,
                                                 deck_2.origin_x, deck_1.origin_y + deck_1.y)
                                self.decks.remove(deck_1)
                                self.decks.remove(deck_2)
                                if (new_deck1.size > 0):
                                    self.decks.append(new_deck1)
                                if (new_deck2.size > 0):
                                    self.decks.append(new_deck2)
                                if (new_deck3.size > 0):
                                    self.decks.append(new_deck3)
                                return 0

                    else:
                        if deck_2.origin_y + deck_2.y >= deck_1.origin_y and deck_2.origin_x == deck_1.origin_x + deck_1.x and deck_2.origin_y + deck_2.y <= deck_1.origin_y + deck_1.y:
                            size_of_new_deck = (deck_2.origin_y + deck_2.y - deck_1.origin_y) * (deck_1.x + deck_2.x)
                            if size_of_new_deck > deck_1.size and size_of_new_deck > deck_2.size:
                                new_deck1 = Deck(deck_2.x, deck_1.origin_y - deck_2.origin_y, deck_2.origin_x,
                                                 deck_2.origin_y)
                                new_deck2 = Deck(deck_1.x + deck_2.x, deck_2.origin_y + deck_2.y - deck_1.origin_y,
                                                 deck_1.origin_x, deck_2.origin_y, )
                                new_deck3 = Deck(deck_1.x, deck_1.origin_y + deck_1.y - deck_2.y - deck_2.origin_y,
                                                 deck_1.origin_x, deck_2.origin_y + deck_2.y)
                                self.decks.remove(deck_1)
                                self.decks.remove(deck_2)
                                if (new_deck1.size > 0):
                                    self.decks.append(new_deck1)
                                if (new_deck2.size > 0):
                                    self.decks.append(new_deck2)
                                if (new_deck3.size > 0):
                                    self.decks.append(new_deck3)
                                return 0

        return 1


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

    def send_ship(self):
        # TODO
        print("chuje wie co tu ma byc")

    def unload_ship(self):
        unloaded_containers = self.containers
        self.containers.clear()
        self.current_volume = self.volume

        return unloaded_containers

    def get_ship_information(self):

        ID_and_sizes = "Ship ID: " + str(self.ID) + " Sizes(x,y,z): " + str(self.x) + ", " + str(self.y) + ", " + str(
            self.z) + "\n"
        capacity_volume_current_capacity_volume = "Capacity: " + str(self.capacity) + " Volume: " + str(
            self.volume) + " Current Capacity: " + str(self.current_capacity) + " Current Volume: " + str(
            self.current_volume) + "\n"
        print(ID_and_sizes + capacity_volume_current_capacity_volume)
        return (ID_and_sizes + capacity_volume_current_capacity_volume)


    def load_container_on_deck(self, deck, container):
        if self.current_capacity == 0:
            print("Ship is full(capacity left = 0")
            return 1
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
            new_deck1 = Deck(deck.x - container.x, container.y, deck.origin_x + container.x, deck.origin_y)
            new_deck2 = Deck(container.x, deck.y - container.y, deck.origin_x, deck.origin_y + container.y)
            new_deck3 = Deck(deck.x - container.x, deck.y - container.y, deck.origin_x + container.x,
                             deck.origin_y + container.y)
            self.decks.remove(deck)
            self.decks.append(new_deck2)
            self.decks.append(new_deck1)
            self.decks.append(new_deck3)
            container.position_x = deck.origin_x
            container.position_y = deck.origin_y
            self.containers.append(container)
            self.current_volume = self.current_volume - container.volume
            self.current_capacity = self.current_capacity -1
            return 0
        else:
            return 1

    def display_ship(self):
        pygame.init()
        monitor_fullness = 0.95
        monitor_h = pygame.display.Info().current_h

        scale = monitor_fullness / ((self.y + math.floor(300 / 700 * self.y)) / monitor_h)

        screen = pygame.display.set_mode(
            (math.floor(scale * self.x), math.floor(scale * (self.y + math.floor(300 / 700 * self.y)))))
        font_size = math.floor(scale * 10)

        myfont = pygame.font.SysFont("monospace", font_size)
        clock = pygame.time.Clock()
        background = pygame.image.load("background.jpg").convert()
        background = pygame.transform.rotate(background, 90)
        background = pygame.transform.scale(background, [math.floor(scale * self.x),
                                                         math.floor(scale * (self.y + math.floor(300 / 700 * self.y)))])
        running = True
        pygame.display.set_caption('SHIP ID - ' + str(self.ID))

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
            screen.blit(background, [0, 0])

            for container in self.containers:

                if color == 1:
                    COLOR = [color_loop, 0, 0]
                elif color == 2:
                    COLOR = [0, color_loop, 0]
                else:
                    COLOR = [0, 0, color_loop]
                pygame.draw.rect(screen, COLOR, [math.floor(scale * container.position_x),
                                                 math.floor(scale * (container.position_y + math.floor(
                                                     220 / 1011 * (self.y + math.floor(300 / 700 * self.y))))),
                                                 math.floor(scale * container.x), math.floor(scale * container.y)],
                                 0)
                color_loop = color_loop + 10
                color = color + 1
                if color_loop >= 255:
                    color_loop = 100
                if color == 4:
                    color = 1
                label_ID = myfont.render(str(container.ID), 1, (0, 0, 0))
                label_month = myfont.render(str(container.timestamp.month), 1, (0, 0, 0))
                label_day = myfont.render(str(container.timestamp.day), 1, (0, 0, 0))
                label_year = myfont.render(str(container.timestamp.year), 1, (0, 0, 0))
                label_one_line = myfont.render(
                    str(container.timestamp.month) + "-" + str(container.timestamp.day) + "-" + str(
                        container.timestamp.year), 1, (0, 0, 0))
                if container.y > container.x:
                    screen.blit(label_ID, (
                    math.floor(scale * container.position_x), math.floor(scale * (container.position_y + math.floor(
                        220 / 1011 * (self.y + math.floor(300 / 700 * self.y)))))))
                    screen.blit(label_month, (math.floor(scale * container.position_x),
                                              math.floor(scale * (container.position_y + font_size + math.floor(
                                                  220 / 1011 * (self.y + math.floor(300 / 700 * self.y)))))))
                    screen.blit(label_day, (math.floor(scale * container.position_x),
                                            math.floor(scale * (container.position_y + 2 * font_size + math.floor(
                                                220 / 1011 * (self.y + math.floor(300 / 700 * self.y)))))))
                    screen.blit(label_year, (math.floor(scale * container.position_x),
                                             math.floor(scale * (container.position_y + 3 * font_size + math.floor(
                                                 220 / 1011 * (self.y + math.floor(300 / 700 * self.y)))))))
                else:
                    screen.blit(label_ID, (
                    math.floor(scale * container.position_x), math.floor(scale * (container.position_y + math.floor(
                        220 / 1011 * (self.y + math.floor(300 / 700 * self.y)))))))
                    screen.blit(label_one_line, (math.floor(scale * container.position_x),
                                                 math.floor(scale * (container.position_y + font_size + math.floor(
                                                     220 / 1011 * (self.y + math.floor(300 / 700 * self.y)))))))



            pygame.display.flip()

        pygame.quit()


class Deck:
    def __init__(self, _x, _y, _origin_x, _origin_y):
        self.x = _x
        self.y = _y
        self.origin_x = _origin_x
        self.origin_y = _origin_y
        self.size = self.x * self.y


class Container:
    def __init__(self, _ID, _x, _y, _z, _timestamp, _destination):
        self.timestamp = _timestamp
        self.x = _x
        self.y = _y
        self.z = _z
        self.volume = self.x * self.y * self.z
        self.ID = _ID
        self.mass = self.x * self.y * self.z * 1000
        self.position_x = 0
        self.position_y = 0
        self.destination = _destination

    def show_timestamp(self):
        print(str(self.timestamp.month) + "-" + str(self.timestamp.day) + "-" + str(self.timestamp.year) + "\n")

    def get_container_information(self):
        ID_and_sizes = "Container ID: " + str(self.ID) + " Sizes(x,y,z): " + str(self.x) + ", " + str(
            self.y) + ", " + str(
            self.z) + "\n"
        volume = "Volume: " + str(self.volume) + "\n"
        print(ID_and_sizes + volume)
        return (ID_and_sizes + volume)

class Timestamp:
    def __init__(self, _month, _day, _year):
        self.month = _month
        self.day = _day
        self.year = _year

    def date_to_number_of_days(self):
        return self.year * 365 + self.month * 31 + self.day

    def get_string(self):
        return (str(self.month) + "-" + str(self.day) + "-" + str(self.year))




class Port:
    def __init__(self, _ID, _ship_capacity):
        self.containers = []
        self.ID = _ID
        self.ship_capacity = _ship_capacity
        self.ships = []

    def add_ship(self, ship):
        self.ships.append(ship)

    def add_conatiner(self, container):
        self.containers.append(container)

    def send_ship(self, ship_id, dest_port_id):
        # TODO
        print("lolz")

    def dock_ship(self, ship):
        if len(self.ships) < self.ship_capacity:
            self.add_ship(ship)
            return 0
        else:
            return 1

    def get_ships(self):
        return self.ships

    def load_ship(self, ship_id):
        for x in self.ships:
            if x.ID == ship_id:
                ShipLoader.Load_ship(x, self.containers)
                print("loaded ship")
                break
        else:
            x = None
            print("couldn't find ship")
            return 1
