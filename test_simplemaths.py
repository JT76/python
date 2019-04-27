import pytest
from pytest import raises
from simplemaths.simplemaths import SimpleMaths as sm
    
class TestSimpleMaths():
    def test_constructor_1(self):
        with raises(TypeError):
            sm(3.2)
        with raises(TypeError):
            sm(-123.2)
        with raises(TypeError):
            sm(3/2.5)
    def test_constructor_2(self):
        with raises(Exception):
            sm("just a string")
    def test_constructor_3(self):
        with raises(Exception):
            sm(3.0)
    def test_constructor_4(self):
        with raises(Exception):
            sm(sm(3))
    def test_constructor_5(self):
        with raises(Exception):
            sm([3,2,1])
    def test_constructor_6(self):
        with raises(Exception):
            sm([3,2,1])
    def test_constructor_7(self):
        with raises(Exception):
            sm(3,2,1)
    def test_constructor_8(self):
        with raises(TypeError):
            sm()
    def test_constructor_9(self):
        assert sm(3)
    def test_square_1(self): 
        assert sm(3).square() == 9
    def test_square_2(self): 
        with raises(AssertionError):
            assert sm(3).square() == 12
    def test_factorial_1(self): 
        with raises(Exception):
            assert sm(0).factorial() == 0
    def test_factorial_2(self): 
        assert sm(0).factorial() == 1
    def test_factorial_3(self): 
        assert sm(10).factorial() == 3628800
    def test_power_1(self): 
        assert sm(2).power() == 8
    def test_power_2(self): 
        assert sm(2).power(4) == 16
    def test_oddoreven_1(self): 
        assert sm(2187235).odd_or_even() == 'Odd'
    def test_oddoreven_2(self): 
        assert sm(2187236).odd_or_even() == 'Even'
    def test_oddoreven_3(self): 
        with raises(AssertionError):
            assert sm(0).odd_or_even() == 'Odd'
    def test_square_root_1(self): 
        assert type(sm(-3).square_root())==complex
            