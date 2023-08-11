from programs import list_of_squares

def test_ListOfSquares():
    assert list_of_squares.list_of_squares(11) == {1:1, 2:4, 3:9, 4:16, 5:25, 6:36, 7:49, 8:64, 9:81, 10:100, 11:121}
    assert list_of_squares.list_of_squares(1) == {1:1}
    assert list_of_squares.list_of_squares(0) == {}