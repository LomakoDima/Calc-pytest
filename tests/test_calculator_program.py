import pytest
from calculate.calculator_program import calculate

def test_calculate_addition():
    assert calculate(1, 1, '+') == 2

def test_calculate_subtraction():
    assert calculate(5, 3, '-') == 2

def test_calculate_multiplication():
    assert calculate(4, 3, '*') == 12

def test_calculate_division():
    assert calculate(8, 2, '/') == 4

def test_calculate_division_by_zero():
    assert calculate(5, 0, '/') == "Ошибка: Деление на ноль."

def test_calculate_unknown_operation():
    assert calculate(5, 5, 'unknown') == "Неизвестная операция."

def test_calculate_negative_numbers():
    assert calculate(-2, -3, '+') == -5

def test_calculate_float_result():
    assert calculate(7, 2, '/') == 3.5

def test_calculate_zero_result():
    assert calculate(3, 3, '-') == 0
