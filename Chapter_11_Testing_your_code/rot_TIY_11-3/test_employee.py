import pytest
import employee_main


@pytest.fixture
def employee():
    """Make an empty employee"""
    return employee_main.Employee()


def test_set_employee_1(employee):
    """Make a basic employee"""
    employee.set_employee("Hong", "Rot", 50000)
    assert "Hong Rot - Salary: 50000" == employee.get_employee_info()


def test_employee_1_give_raise(employee):
    """Give a salary to employee."""
    employee.set_employee("Hong", "Rot", 50000)
    employee.give_raise()
    assert "Hong Rot - Salary: 55000" == employee.get_employee_info()


def test_employee_1_give_custom_raise(employee):
    """Give a custom salary to employee."""
    employee.set_employee("Hong", "Rot", 50000)
    employee.give_raise(20000)
    assert "Hong Rot - Salary: 70000" == employee.get_employee_info()
