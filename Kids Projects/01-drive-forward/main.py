basic.show_icon(IconNames.HAPPY)

def on_forever():
    Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Run, 100)
    basic.pause(1000)

    Tinybit.CarCtrl(Tinybit.CarState.Car_Stop)
    basic.pause(1000)

basic.forever(on_forever)
