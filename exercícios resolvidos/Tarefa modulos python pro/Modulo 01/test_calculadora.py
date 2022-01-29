import pytest
from calculadora import adicao, subtr, multi, div

class TestCalc:
    def setup(self):
        pass
    
    def test_adicao(self):
        resultado = adicao(2, 3)
       
        assert resultado == 5
    
    def test_subtr(self):
        resultado = subtr(10, 2)

        assert resultado == 8
    
    def test_multi(self):
        resultado = multi(10,20)

        assert resultado == 200
    
    def test_div(self):
        resultado = div(1200, 20)

        assert resultado == 60
        with pytest.raises(ZeroDivisionError):
            div(1200,0)
        