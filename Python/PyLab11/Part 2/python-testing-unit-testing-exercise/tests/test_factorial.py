from programs import factorial

def test_factorial():
    assert factorial.fact(5) == 120
    assert factorial.fact(0) == 1
