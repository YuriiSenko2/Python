from abc import ABC, abstractmethod


class Menu(ABC):
    _menu_section = ''

    @abstractmethod
    def order_dish(self, position: int):
        """Position details will be here"""
