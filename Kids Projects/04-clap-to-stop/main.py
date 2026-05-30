def on_forever():
    sound = Tinybit.Voice_Sensor()

    if sound > 600:
        Tinybit.RGB_Car_Big(Tinybit.enColor.Red)
        Tinybit.CarCtrl(Tinybit.CarState.Car_Stop)
        basic.pause(1000)
    else:
        Tinybit.RGB_Car_Big(Tinybit.enColor.Green)
        Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Run, 80)

basic.forever(on_forever)
