from abc import ABC, abstractmethod


class IMathFunc(ABC):

    @abstractmethod
    def my_sum(self, x, y):
        raise NotImplementedError

    @abstractmethod
    def my_dif(self, x, y):
        raise NotImplementedError

    @abstractmethod
    def my_mul(self, x, y):
        raise NotImplementedError

    @abstractmethod
    def my_division(self, x, y):
        raise NotImplementedError
