from thesaurus import delay


def nextspeedsetting(speedrange):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Before we start, can you please tell us the speed from the range of {speedrange}?')


nextspeedsetting('1-10')

speednumrange = input()

while speednumrange not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
    print("Invalid speed, please use the correct speed, as listed in the question. Thanks!")
    nextspeedsetting('1-10')
    speednumrange = input()
    pass

def nextspeed1():
    if speednumrange in ['1']:
        speed1var = 2
        while speed1var > 0:
            speed1var = speed1var - 1
            if speed1var == 0:
                break
            print('Speed:', speed1var)
            delay(10)


def nextspeed2():
    if speednumrange in ['2']:
        speed2var = 3
        while speed2var > 0:
            speed2var = speed2var - 1
            if speed2var == 1:
                break
            print('Speed:', speed2var)
            delay(9)


def nextspeed3():
    if speednumrange in ['3']:
        speed3var = 4
        while speed3var > 0:
            speed3var = speed3var - 1
            if speed3var == 2:
                break
            print('Speed:', speed3var)
            delay(8)


def nextspeed4():
    if speednumrange in ['4']:
        speed4var = 5
        while speed4var > 0:
            speed4var = speed4var - 1
            if speed4var == 3:
                break
            print('Speed:', speed4var)
            delay(7)


def nextspeed5():
    if speednumrange in ['5']:
        speed5var = 6
        while speed5var > 0:
            speed5var = speed5var - 1
            if speed5var == 4:
                break
            print('Speed:', speed5var)
            delay(6)


def nextspeed6():
    if speednumrange in ['6']:
        speed6var = 7
        while speed6var > 0:
            speed6var = speed6var - 1
            if speed6var == 5:
                break
            print('Speed:', speed6var)
            delay(5)


def nextspeed7():
    if speednumrange in ['7']:
        speed7var = 8
        while speed7var > 0:
            speed7var = speed7var - 1
            if speed7var == 6:
                break
            print('Speed:', speed7var)
            delay(4)


def nextspeed8():
    if speednumrange in ['8']:
        speed2var = 9
        while speed2var > 0:
            speed2var = speed2var - 1
            if speed2var == 7:
                break
            print('Speed:', speed2var)
            delay(3)


def nextspeed9():
    if speednumrange in ['9']:
        speed2var = 10
        while speed2var > 0:
            speed2var = speed2var - 1
            if speed2var == 8:
                break
            print('Speed:', speed2var)
            delay(2)


def nextspeed10():
    if speednumrange in ['10']:
        speed10var = 11
        while speed10var > 0:
            speed10var = speed10var - 1
            if speed10var == 9:
                break
            print('Speed:', speed10var)
            delay(1)


class speed1notifier:
    if speednumrange == '1':
        nextspeed1()
        pass


class speed2notifier:
    if speednumrange == '2':
        nextspeed2()
        pass


class speed3notifier:
    if speednumrange == '3':
        nextspeed3()
        pass


class speed4notifier:
    if speednumrange == '4':
        nextspeed4()
        pass


class speed5notifier:
    if speednumrange == '5':
        nextspeed5()
        pass


class speed6notifier:
    if speednumrange == '6':
        nextspeed6()
        pass


class speed7notifier:
    if speednumrange == '7':
        nextspeed7()
        pass


class speed8notifier:
    if speednumrange == '8':
        nextspeed8()
        pass


class speed9notifier:
    if speednumrange == '9':
        nextspeed9()
        pass


class speed10notifier:
    if speednumrange == '10':
        nextspeed10()
        pass



