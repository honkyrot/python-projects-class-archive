import pytest
import employee_function


@pytest.fixture
def employee_class():
    """Make an empty employee"""
    return employee_function.Employee()


def test_set_employee(employee_class):
    """basic employee creation"""
    employee_class.set_employee("Hong", "Rot", 30000)
    assert employee_class.get_info() == "Hong Rot - Salary: 30000"


def test_give_raise(employee_class):
    """employee with default raise (5000)"""
    employee_class.set_employee("Hong", "Rot", 30000)
    employee_class.give_raise()
    assert employee_class.get_info() == "Hong Rot - Salary: 35000"


def test_give_custom_raise(employee_class):
    """employee with custom raise"""
    employee_class.set_employee("Hong", "Rot", 30000)
    employee_class.give_raise(20000)
    assert employee_class.get_info() == "Hong Rot - Salary: 50000"
