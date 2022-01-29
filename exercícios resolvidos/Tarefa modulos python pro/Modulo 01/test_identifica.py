import pytest
from identifica import multi5, multi7, multi5e7, nao_multi

class TestMultiplos:
    def setup(self):
        pass

    def test_multi_5(self):
        result = multi5(14)

        assert result == False
   
    def test_multi_7(self):
        result = multi7(21)

        assert result == 'buzz'
    
    def test_multi5e7(self):
        result = multi5e7(210)

        assert result == 'fizzbuzz'

    def test_nao_multi(self):
        result = nao_multi(3)

        assert result == 'miss'
