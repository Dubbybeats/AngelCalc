import pytest
import tkinter as tk

from AngelsCalculator import SimpleCalculator


@pytest.fixture
def app():
    try:
        calc = SimpleCalculator()
        calc.withdraw()
        yield calc
        calc.destroy()
    except tk.TclError:
        pytest.skip("Tkinter cannot initialize (no display)")


def test_digit_entry(app):
    app.on_button_click('1')
    app.on_button_click('2')
    assert app.result_var.get() == '12'


def test_decimal_handling(app):
    for ch in ['1', '.', '2', '.', '3']:
        app.on_button_click(ch)
    assert app.result_var.get() == '1.23'


def test_negation(app):
    for ch in ['5', '±']:
        app.on_button_click(ch)
    assert app.result_var.get() == '-5.0'


def test_percentage(app):
    for ch in ['5', '0', '%']:
        app.on_button_click(ch)
    assert app.result_var.get() == '0.5'
