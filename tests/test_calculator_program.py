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

def test_calculate_power():
    assert calculate(2, 3, '^') == 8

def test_calculate_modulus():
    assert calculate(10, 3, '%') == 1

def test_calculate_modulus_by_zero():
    assert calculate(10, 0, '%') == "Ошибка: Деление на ноль."

def test_calculate_integer_division():
    assert calculate(10, 3, '//') == 3

def test_calculate_integer_division_by_zero():
    assert calculate(10, 0, '//') == "Ошибка: Деление на ноль."

def test_calculate_negation():
    assert calculate(0, 5, 'neg') == -5
