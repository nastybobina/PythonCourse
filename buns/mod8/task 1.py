class Transport:
    def __init__(self, coordinates, speed, brand, year, number):
        self.coordinates = coordinates
        self.speed = speed
        self.brand = brand
        self.year = year
        self.number = number

    @property
    def coordinates(self):
        return self._coordinates

    @coordinates.setter
    def coordinates(self, value):
        if isinstance(value, list) and len(value) == 4:
            if (isinstance(value[0], int)
                    and isinstance(value[1], int)
                    and isinstance(value[2], int)
                    and isinstance(value[3], int)):
                if (value[0] >= 0
                        and value[1] >= 0
                        and value[2] >= 0
                        and value[3] >= 0):
                    self._coordinates = value
                else:
                    raise Exception('Invalid argument value.'
                                    'Координаты задаются списком из 4 int значений > 0')
            else:
                raise Exception('Invalid argument value.'
                                'Координаты задаются списком из 4 int > 0')
        else:
            raise Exception('Invalid argument value.'
                            'Координаты задаются списком из 4 int > 0')

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        if (isinstance(value, int)
                and value >= 0):
            self._speed = value
        else:
            raise Exception('Invalid argument value.'
                            'Скорость задаётся int >= 0')

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if isinstance(value, str):
            self._brand = value
        else:
            raise Exception('Invalid argument value.'
                            'Название бренда задаётся str')

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if (isinstance(value, int)
                and 0 <= value < 2024):
            self._year = value
        else:
            raise Exception('Invalid argument value.'
                            'Год задаётся значением int'
                            'от 0 до 2023')

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        if (isinstance(value, int)
                and 0 < value <= 9999999):
            self._number = value
        else:
            raise Exception('Invalid argument value. '
                            'Номер задаётся значением int'
                            'от 0 до 9999999')

    def __str__(self):
        return (f"Transport: coordinates: "
                f"x: {self.coordinates[0]} "
                f"y: {self.coordinates[1]} "
                f"length: "
                f"{self.coordinates[2]} "
                f"width: {self.coordinates[3]}, "
                f"speed: {self.speed}mph, "
                f"brand: {self.brand}, "
                f"year: {self.year}, "
                f"number: {self.number}")

    def isInArea(self, pos_x, pos_y, length, width) -> bool:
        return (self._coordinates[0] == pos_x
                and self._coordinates[1] == pos_y
                and self._coordinates[2] == length
                and self._coordinates[3] == width)

class Passenger:
    def __init__(self, passengers_capacity, number_of_passengers):
        self.passengers_capacity = passengers_capacity
        self.number_of_passengers = number_of_passengers

    @property
    def passengers_capacity(self):
        return self._passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, value):
        if (isinstance(value, int)
                and value > 0):
            self._passengers_capacity = value
        else:
            raise Exception('Invalid argument value.'
                            'Значение вместимости пассажиров задаётся int > 0')

    @property
    def number_of_passengers(self):
        return self._number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, value):
        if isinstance(value, int) and value >= 0:
            self._number_of_passengers = value
        else:
            raise Exception('Invalid argument value.'
                            'Значение количества пассажиров задаётся'
                            'int >= 0')

    def __str__(self):
        return (f"Passenger: "
                f"passengers capacity: {self.passengers_capacity}, "
                f"number of passengers: {self.number_of_passengers}")

class Cargo:
    def __init__(self, carrying):
        self.carrying = carrying

    @property
    def carrying(self):
        return self._carrying

    @carrying.setter
    def carrying(self, value):
        if isinstance(value, int) and value > 0:
            self._carrying = value
        else:
            raise Exception('Invalid carrying value Argument. '
                            'Значение грузоподъёмности задаётся '
                            'int > 0')


class Plane(Transport):
    def __init__(self, coordinates, speed, brand, year, number, height):
        super().__init__(coordinates, speed, brand, year, number)
        self.height = height

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if isinstance(value, int) and value >= 0:
            self._height = value
        else:
            raise Exception('Invalid port value Argument. '
                            'Значение высоты задаётся int > 0')

class Auto(Transport):
    def __init__(self, coordinates, speed, brand, year, number, license_plate):
        super().__init__(coordinates, speed, brand, year, number)
        self.license_plate = license_plate

    @property
    def license_plate(self):
        return self._license_plate

    @license_plate.setter
    def license_plate(self, value):
        if (isinstance(value, str)
                and len(value) == 6):
            self._license_plate = value
        else:
            raise Exception(
                'Invalid port value Argument. '
                'Значение номера автомобиля задаётся '
                'str длиной в 6 элементов')

class Ship(Transport):
    def __init__(self, coordinates, speed, brand, year, number, port):
        super().__init__(coordinates, speed, brand, year, number)
        self.port = port

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, value):
        if isinstance(value, str):
            self._port = value
        else:
            raise Exception('Invalid port value Argument. '
                            'Значение порта задаётся str')


class Car(Auto):
    def __init__(self, coordinates, speed, brand, year, number, license_plate):
        super().__init__(coordinates, speed, brand, year, number, license_plate)

class Bus(Auto, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, license_plate,
                 passengers_capacity, number_of_passengers):
        Auto.__init__(self, coordinates, speed, brand, year, number, license_plate)
        Passenger.__init__(self, passengers_capacity, number_of_passengers)

class CargoAuto(Auto, Cargo):
    def __init__(self, coordinates, speed, brand, year, number, license_plate, carrying):
        Auto.__init__(self, coordinates, speed, brand, year, number, license_plate)
        Cargo.__init__(self, carrying)

class Boat(Ship):
    def __init__(self, coordinates, speed, brand, year, number, port):
        super().__init__(coordinates, speed, brand, year, number, port)

class PassengerShip(Ship, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, port, passengers_capacity, number_of_passengers):
        Ship.__init__(self, coordinates, speed, brand, year, number, port)
        Passenger.__init__(self, passengers_capacity, number_of_passengers)

class CargoShip(Ship, Cargo):
    def __init__(self, coordinates, speed, brand, year, number, port, carrying):
        Ship.__init__(self, coordinates, speed, brand, year, number, port)
        Cargo.__init__(self, carrying)

class Biplane(Plane):
    def __init__(self, coordinates, speed, brand, year, number, height):
        super().__init__(coordinates, speed, brand, year, number, height)

class PassengerPlane(Plane, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, height, passengers_capacity, number_of_passengers):
        Plane.__init__(self, coordinates, speed, brand, year, number, height)
        Passenger.__init__(self, passengers_capacity, number_of_passengers)

class CargoPlane(Plane, Cargo):
    def __init__(self, coordinates, speed, brand, year, number, height, carrying):
        Plane.__init__(self, coordinates, speed, brand, year, number, height)
        Cargo.__init__(self, carrying)
