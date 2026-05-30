# 05 Avoid A Wall

## Goal

Make Tiny:bit stop and turn when something is close.

## What You Learn

- how to use the ultrasonic distance sensor
- how to compare numbers
- how to make a simple robot decision

## Code

Copy this into MakeCode Python:

```python
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
```

## Try Changing This

- Change `10` to `15` so Tiny:bit stops earlier.
- Change turn pause `500` to make a bigger or smaller turn.

## Challenge

Make Tiny:bit turn left sometimes and right sometimes.
