# 04 Clap To Stop

## Goal

Make Tiny:bit stop when the sound sensor hears a loud noise.

## What You Learn

- how to read a sensor
- how to use an `if` condition
- how a robot can react to the world

## Code

Copy this into MakeCode Python:

```python
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
```

## Try Changing This

- If it stops too easily, change `600` to `700`.
- If it does not stop, change `600` to `500`.

## Challenge

Make Tiny:bit play a sound when it stops.
