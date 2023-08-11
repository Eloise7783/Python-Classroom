from programs import vowels

def test_vowels():
    assert vowels.vowels("Eloise") == 4
    assert vowels.vowels("Cwtch") == 0