# this is the unit testing for Arab2Rom.py

from Arb2Rom import arb2rom

def test_lowNum():
    assert arb2rom(2) == 'II'

def test_highNum():
    assert arb2rom(3000) == 'MMM'

def test_avgNum():
    assert arb2rom(50) == 'L'

def test_decimal():
    assert arb2rom(7.9) == ''

def test_string():
    assert arb2rom('hello') == ''

def test_orange():
    assert arb2rom(400000) == ''
