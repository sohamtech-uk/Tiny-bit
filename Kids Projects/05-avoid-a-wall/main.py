def on_forever():
    distance = Tinybit.Ultrasonic_CarV2()

    if distance < 10:
        Tinybit.RGB_Car_Big(Tinybit.enColor.Red)
        Tinybit.CarCtrl(Tinybit.CarState.Car_Stop)
        basic.pause(200)

        Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_SpinRight, 90)
        basic.pause(500)
    else:
        Tinybit.RGB_Car_Big(Tinybit.enColor.Green)
        Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Run, 80)

basic.forever(on_forever)
