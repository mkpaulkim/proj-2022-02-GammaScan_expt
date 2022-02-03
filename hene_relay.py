import pycube_hwlib.hardware as hw

uno = hw.Arduino()
LED = 3     # pin 11

while True:
    switch = input('on / off / quit: ')

    if switch[0].lower() == 'q':
        break

    if switch.lower() == 'on':
        uno.set_LED(LED)
    else:
        uno.set_LED(0)
