from components.mymodule import add, mul

class TestMyModule():
    
    def test_add(self):
        assert add(2,1) == 3 , "not good"

    def test_mul(self):
        assert mul(5,4) == 20 , "not good"    
