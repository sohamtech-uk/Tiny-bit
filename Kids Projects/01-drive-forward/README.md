# 01 Drive Forward

## Goal

Make Tiny:bit drive forward, stop, and wait.

## What You Learn

- how to start the motors
- how to stop the car
- how speed and time change movement

## Code

Copy this into MakeCode Python:

```python
basic.show_icon(IconNames.HAPPY)

def on_forever():
    Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Run, 100)
    basic.pause(1000)

    Tinybit.CarCtrl(Tinybit.CarState.Car_Stop)
    basic.pause(1000)

basic.forever(on_forever)
```

## Try Changing This

- Change speed `100` to `150`.
- Change pause `1000` to `500`.

## Challenge

Can you make Tiny:bit drive forward for exactly one tile or one sheet of paper?
