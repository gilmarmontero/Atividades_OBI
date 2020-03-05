from robo import lancamento

def test_lance1():
    assert lancamento(500) == 1

def test_lance2():
    assert lancamento(801) == 2

def test_lance3():
    assert lancamento(1402) == 3
    


