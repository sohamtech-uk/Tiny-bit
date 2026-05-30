# 03 Lights When Turning

## Goal

Make Tiny:bit change light color when it turns.

## What You Learn

- how lights can show robot actions
- how to combine movement and color

## Code

Copy this into MakeCode Python:

```python
def on_forever():
    Tinybit.RGB_Car_Big(Tinybit.enColor.Green)
    Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Run, 100)
    basic.pause(1000)

    Tinybit.RGB_Car_Big(Tinybit.enColor.Red)
    Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_SpinRight, 100)
    basic.pause(450)

    Tinybit.CarCtrl(Tinybit.CarState.Car_Stop)
    Tinybit.RGB_Car_Big(Tinybit.enColor.OFF)
    basic.pause(500)

basic.forever(on_forever)
```

## Try Changing This

- Change `Red` to `Blue`.
- Change `Green` to `Yellow`.

## Challenge

Use one color for left turns and another color for right turns.
