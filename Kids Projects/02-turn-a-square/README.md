# 02 Turn A Square

## Goal

Make Tiny:bit drive in a square.

## What You Learn

- how to repeat code
- how to turn right
- how to tune robot movement

## Code

Copy this into MakeCode Python:

```python
basic.show_icon(IconNames.SQUARE)

def on_forever():
    for i in range(4):
        Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Run, 100)
        basic.pause(1000)

        Tinybit.CarCtrl(Tinybit.CarState.Car_Stop)
        basic.pause(200)

        Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_SpinRight, 100)
        basic.pause(450)

        Tinybit.CarCtrl(Tinybit.CarState.Car_Stop)
        basic.pause(200)

basic.forever(on_forever)
```

## Try Changing This

- If the turn is too small, make `450` bigger.
- If the turn is too big, make `450` smaller.

## Challenge

Can you make a triangle by changing the number of repeats and turn time?
