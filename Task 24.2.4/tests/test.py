import pytest
from app.calc import Calculator
class TestCalc:
    def setup(self):
        self.calc = Calculator
    def test_adding_succes(self):
        '''проверка функции сложения при вводе корректных данных'''
        assert self.calc.adding(self, 1, 1) == 2
    def test_zero_division(self):
        '''проверка функции деления на ноль с отображением ошибки ZeroDivisionError '''
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)
    def test_multiply_success(self):
        '''проверка функции умножения при вводе корректных данных'''
        assert self.calc.multiply(self,2,5) == 10
    def test_division_success(self):
        '''проверка функции деления при вводе корректных данных'''
        assert  self.calc.division(self,8,4) == 2

    def test_subtraction_success(self):
        '''проверка функции вычитания при вводе корректных данных'''
        assert  self.calc.subtraction(self,7,2) == 5

    def teardown(self):
        print("Выполнение метода Teardown")