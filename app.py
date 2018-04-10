def cool_func(x):
    if x > 3:
        return "that's more than a few."
    elif x == 3:
        return "that's exactly a few."
    else:
        return "that's no more than a couple."


def func2(x):
    if x > 0:
        print('that thing is greater than zero')
    return 'yay!'


def div(x, y):
    try:
        return x / y
    except ZeroDivisionError as zde:
        print('Are you sure you want to paradox?')
        print('What do you even want from me?')
        print('Because you asked for nonsense, you get nonsense')
        if x == 0:
            print("I literally can't even")
            return x
        else:
            return y / x
