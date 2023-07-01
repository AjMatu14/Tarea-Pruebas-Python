import pytest
from main import sum, numero_mayor

def test_sum():
    assert sum(3,8) == 11
    print("La funcion suma 1 trabaja correctamente")

def test_sum2():
    assert sum(9,5) == 14
    print("La funcion suma 2 trabaja correctamente")

def test_sum3():
    assert sum(35,5) == 40
    print("La funcion suma 3 trabaja correctamente")

def test_sum4():
    assert sum(8,25) == 33
    print("La funcion suma 4 trabaja correctamente")

def test_sum5():
    assert sum(98,2) == 100
    print("La funcion suma 5 trabaja correctamente")
    
def test_numero_mayor():
    numero_mayor(9,11)
    print("La funcion numero mayor 1 no trabaja correctamente")

def test_numero_mayor1():
    numero_mayor(36,50)
    print("La funcion numero mayor 2 no trabaja correctamente")

def test_numero_mayor2():
    numero_mayor(8,100)
    print("La funcion numero mayor 3 no trabaja correctamente")

def test_numero_mayor3():
    numero_mayor(2,20)
    print("La funcion numero mayor 4 no trabaja correctamente")

def test_numero_mayor4():
    numero_mayor(97,105)
    print("La funcion numero mayor 5 no trabaja correctamente")
    
@pytest.mark.parametrize(
    "input_x, input_y, esperando",
    [
        (3, 4, 7),
        (5, sum(5,6), 16),
        (sum(2,1), 5, 8),
    ]
)
def test_sum_params(input_x, input_y, esperando):
    assert sum(input_x, input_y) == esperando
    print("Las funciones parametrizadas trabajan correctamente")
    
if __name__ == '__main__':
    test_sum()
    test_sum2()
    test_sum3()
    test_sum4()
    test_sum5()
    test_numero_mayor()
    test_numero_mayor1()
    test_numero_mayor2()
    test_numero_mayor3()
    test_numero_mayor4()