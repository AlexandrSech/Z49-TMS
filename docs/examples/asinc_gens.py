from time import sleep


queue = []


def counter():
    counter = 0
    while True:
        print(counter)
        counter += 1
        if counter == 2:
            try:
                1 / 0
            except ZeroDivisionError:
                print('IDIOT')
        if counter == 4:
            break
        yield


def printer():
    co = 0
    while True:
        if co % 5 == 0:
            print(' '* 5 + 'OYWAY')
        co += 1
        yield


def main():
    while True:
        g = queue.pop(0)
        ended = False
        try:
            next(g)
        except StopIteration:
            print(str(g) + ' has stopped')
            ended = True

        if not ended:
            queue.append(g)
        sleep(0.5)


if __name__ == '__main__':
    g1 = counter()
    queue.append(g1)
    g2 = printer()
    queue.append(g2)
    main()
