def transposition(number):
    hundreds = int(number / 100)
    units = number % 10
    dozens = int((number - hundreds * 100 - units) / 10)
    return hundreds, dozens, units


def magic_1089():

    x = 100
    key = True

    while x < 1000:
        h, d, u = transposition(x)
        if h > d > u:
            new_x = u*100 + d*10 + h
            y = x - new_x
            h, d, u = transposition(y)
            new_y = u*100 + d*10 + h
            result = new_y + y
            if result != 1089:
                print('I found ' + str(x), 'result: ' + str(result))
                key = False
        x += 1

    if key:
        print('There are no such numbers :(')


if __name__ == "__main__":
    magic_1089()
