"""This module contains exercise Python - OOP practice"""
from abc import ABC
from typing import List, Optional
from datetime import datetime
from dataclasses import dataclass
from random import choice


@dataclass
class Dish:
    """This data class describes information about the dish"""
    dish_name: str
    quantity: int
    price: float


class Order:
    """This class describes the work with the order"""
    __number: int = 0

    def __new__(cls, *args, **kwargs):
        cls.__number += 1
        return super(Order, cls).__new__(cls, *args, **kwargs)

    def __init__(self, remote: bool):
        self.number = self.__number
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.remote = remote
        self.status = False
        self.dishes: List[Dish] = []

    def add_dish(self, dish_name: str, quantity: int):
        """This method adds a dish to the dishes list"""
        self.dishes.append(Dish(dish_name=dish_name, quantity=quantity, price=10.0))

    def update_status(self, status):
        """This method update order status"""
        self.status = status


class Customer:
    """This class describes the capabilities of the customer"""

    def __init__(self, name: str, phone: str = '', address: str = ''):
        self._name: str = name
        self._remote = False
        if phone != '' and address != '':
            self._phone = phone
            self._address = address
            self._remote = True
        self.order: Optional[Order] = None
        self.is_order_taken: bool = False

    def create_order(self, **dishes):
        """This method create order"""
        self.order = Order(self._remote)
        for dish_name, quantity in dishes.items():
            self.order.add_dish(dish_name, quantity)

    def accept_order(self, order) -> Optional[str]:
        """This method update status taken order at the customer"""
        if self.order.number == order.number:
            self.is_order_taken = True
            return None
        return 'Это не мой заказ'


class Staff:
    """This class describes the possibilities staff"""
    class StaffList:
        """This class describes work with staff list"""
        staff = {}

        def __init__(self, position: str, info):
            if position not in self.staff:
                self.staff.update({position: [info]})
            else:
                self.staff[position].append(info)

        def get_all_staff(self) -> dict:
            """This method return staff list as dict"""
            return self.staff

    def __init__(self, name, salary):
        self._name = name
        self._salary = salary
        self._position = type(self).__name__
        self._staff_list = Staff.StaffList(self._position, self)

    def call_staff(self, position: str):
        """This method return person of staff with the right position """
        staff = self._staff_list.get_all_staff()
        return choice(staff[position])


class OrdersList(ABC):
    """Abstract class which contains lists of orders and methods for working with them"""
    _orders: List[Order] = []
    _ready_orders: List[Order] = []

    def get_order(self, ready: bool = False):
        """This method takes in a argument ready, return order from ready orders or orders lists"""
        return self._ready_orders.pop(0) if ready else self._orders.pop(0)

    def update_orders_list(self, order: Order):
        """This method takes in a argument order,
        append order in ready orders or orders lists by status
        """
        if order.status:
            self._ready_orders.append(order)
        else:
            self._orders.append(order)


class Operator(Staff, OrdersList):
    """This class describes opportunities operator"""
    _customers = {}

    def checkout(self, customer: Customer):
        """This method update orders list and informs cook about new order"""
        super().update_orders_list(customer.order)
        self._customers[customer.order] = customer
        _cook = self.call_staff('Cook')
        _cook.cook()

    def get_delivery_info(self, order: Order) -> Customer:
        """This method takes in a order, return customers who ordered this order"""
        return self._customers[order]


class Driver(Staff):
    """This class describes opportunities driver"""
    def drive_order(self, order: Order):
        """This method takes in a order, and drive order to customer"""
        _operator = self.call_staff('Operator')
        customer = _operator.get_delivery_info(order)
        customer.accept_order(order)


class Waiter(Staff):
    """This class describes opportunities waiter"""
    def bring_order(self, order: Order):
        """This method takes in a order, and bring order to customer"""
        _operator = self.call_staff('Operator')
        customer = _operator.get_delivery_info(order)
        customer.accept_order(order)


class Manager(Staff, OrdersList):
    """This class describes opportunities manager"""
    def choose_type_delivery(self):
        """This method get order and call driver or waiter by remote status"""
        order = super().get_order(True)
        if order.remote:
            self.call_staff('Driver').drive_order(order)
        else:
            self.call_staff('Waiter').bring_order(order)


class Cook(Staff, OrdersList):
    """This class describes opportunities cook"""
    def call_manager(self):
        """This method call manager"""
        _manager = self.call_staff('Manager')
        _manager.choose_type_delivery()

    def cook(self):
        """This method update status order and orders list
        informing the manager at the end of cooking
        """
        order = super().get_order()
        order.update_status(True)
        super().update_orders_list(order)
        self.call_manager()


if __name__ == '__main__':
    # Customers
    dan = Customer(name='Dan', phone='32123', address='Dsasda')
    vadim = Customer(name='Vadim')

    # Staff
    operator = Operator(name='Valera', salary='100$')
    cook = Cook(name='Nikita', salary='200$')
    manager = Manager(name='Alex', salary='300$')
    driver = Driver(name='Vova', salary='50$')
    waiter = Waiter(name='Bohgdan', salary='20$')

    dan.create_order(pizza=2, icecream=1)
    vadim.create_order(shawarma=3)

    operator.checkout(dan)
    operator.checkout(vadim)
