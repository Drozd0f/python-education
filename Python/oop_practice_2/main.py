"""This module contains exercise Python - OOP practice part 2"""
from abc import ABC, abstractmethod


class Characteristics(ABC):
    """
    This abstract class describes comparing transport characteristics
    """
    def __eq__(self, other):
        return self.weight == other.weight and self.colour == other.colour

    def __ne__(self, other):
        return self.weight != other.weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __le__(self, other):
        return self.weight <= other.weight

    def __ge__(self, other):
        return self.weight >= other.weight


class NoNegative:
    """
    This class describes a handle to positive numbers
    """
    def __set_name__(self, owner, name):
        self.name = name  # pylint: disable=W0201, # Attribute defined outside __init__

    def __set__(self, instance, value):
        if isinstance(value, int) and value < 0:
            raise ValueError('Cannot be negative')
        if isinstance(value, list):
            if value[0] < 0 or value[1] < 0:
                raise ValueError('Cannot be negative')
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]


class Engine:
    """
    This class describes the operation of the engine
    """
    _max_velocity = 0
    _info = {'work': False, 'broken': False}

    def _is_engine_broken(self, current_velocity: int) -> bool:
        if self._max_velocity <= current_velocity:
            self._info['broken'] = True
            return True
        return False

    @property
    def engine_state(self) -> bool:
        """
        This method returns work state of the engine
        """
        return self._info['work']

    @engine_state.setter
    def engine_state(self, value: bool):
        """
        This method change work state of the engine
        """
        self._info['work'] = value

    def work(self, current_velocity):
        """
        This method checks the condition of the engine
        """
        if self._is_engine_broken(current_velocity):
            raise 'Сurrent velocity exceeded the maximum velocity'  # pylint: disable=E0702
            # Raising str while only classes or instances are allowed

    @classmethod
    def change_max_velocity(cls, max_velocity):
        """
        This method change max_velocity for the same kind transport
        """
        cls._max_velocity = max_velocity


class Transport(ABC):
    """
    This abstract class describes the basic properties of the transport
    """
    _weight = 0
    position = NoNegative()
    _current_velocity = NoNegative()

    def __init__(self, colour: str, velocity: int):
        self.colour = colour
        self._current_velocity = velocity

    @abstractmethod
    def move(self, time, velocity, back=False):
        """
        This method describes the moving transport
        """
        pass

    @abstractmethod
    def stop(self):
        """
        This method describes the moving transport
        """
        pass

    @property
    def weight(self):
        """
        This method returns weight transport
        """
        return self._weight

    @weight.setter
    def weight(self, value):
        """
        This method change weight transport
        """
        self._weight = value

    @staticmethod
    def beep():
        """
        This static method describes beep transport
        """
        print('Bip Bip!')


class Airplane(Transport, Engine, Characteristics):
    """
    This class describes the properties of the airplane
    """
    _weight = 162 * 10 ** 3
    _max_velocity = 500

    def __init__(self, colour: str, velocity: int, position: list):
        if not isinstance(position, list):
            raise TypeError('Position for airplanes must be list')
        self.position = position
        super().__init__(colour, velocity)

    def move(self, time, velocity, back=False):
        self.engine_state = True
        self.work(velocity)
        position = velocity * time
        if back:
            self.position[0] -= position
        else:
            self.position[0] += position
        self.position[1] = position
        self._current_velocity = velocity
        return self

    def stop(self):
        self.position[1] = 0
        self.engine_state = False
        self._current_velocity = 0


class Car(Transport, Engine, Characteristics):
    """
    This class describes the properties of the car
    """
    _weight = 1.5 * 10 ** 3
    _max_velocity = 85

    def __init__(self, colour: str, velocity: int, position: int):
        self.position = position
        super().__init__(colour, velocity)

    def move(self, time, velocity, back=False):
        self.engine_state = True
        self.work(velocity)
        if back:
            self.position -= velocity * time
        else:
            self.position += velocity * time
        self._current_velocity = velocity
        return self

    def stop(self):
        self.engine_state = False
        self._current_velocity = 0


class Ship(Transport, Engine, Characteristics):
    """
    This class describes the properties of the ship
    """
    _weight = 215 * 10 ** 6
    _max_velocity = 80

    def __init__(self, colour: str, velocity: int, position: int):
        self.position = position
        super().__init__(colour, velocity)

    def move(self, time, velocity, back=False):
        self.engine_state = True
        self.work(velocity)
        if back:
            self.position -= velocity * time
        else:
            self.position += velocity * time
        self._current_velocity = velocity
        return self

    def stop(self):
        self.engine_state = False
        self._current_velocity = 0


class Bike(Transport, Characteristics):
    """
    This class describes the properties of the bike
    """
    _weight = 9
    _max_velocity = 15

    def __init__(self, colour: str, velocity: int, position: int):
        self.position = position
        super().__init__(colour, velocity)

    def move(self, time, velocity, back=False):
        if back:
            self.position -= velocity * time
        else:
            self.position += velocity * time
        self._current_velocity = velocity
        return self

    def stop(self):
        self._current_velocity = 0
