import app


def test_cool_func():
    #assert app.cool_func(3) == "that's exactly a few."
    assert app.cool_func(2) == "that's no more than a couple."
    assert app.cool_func(10) == "that's more than a few."


def test_func2():
    assert app.func2(1) == 'yay!'
    #assert app.func2(0) == 'yay!'


def test_div():
    assert app.div(4, 2) == 2
    #assert app.div(1, 0) == 0
    #assert app.div(6, -2) == -3
    #assert app.div(0, 0) == 0
