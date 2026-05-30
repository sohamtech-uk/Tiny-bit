# Troubleshooting

## The Car Does Not Move

- Check the batteries.
- Check the micro:bit is pushed in properly.
- Try a slower speed like `80`.
- Make sure your code uses a move block before a stop block.

## The Car Spins Instead Of Driving Straight

- Check both wheels can turn freely.
- Try a lower speed.
- Use `CarCtrlSpeed2` if one motor is stronger than the other.

## The Car Turns Too Much

- Make the turn pause smaller.
- Example: change `450` to `350`.

## The Car Does Not Turn Enough

- Make the turn pause bigger.
- Example: change `450` to `550`.

## Lights Do Not Turn On

- Check you are using `RGB_Car_Big` or `RGB_Car_Big2`.
- Try `Tinybit.enColor.Red` first.

## The Distance Sensor Gives Strange Numbers

- Point the sensor at a flat wall.
- Keep your hand at least a few centimeters away.
- Try again in a place with less clutter.

## MakeCode Shows Red Lines

- Check if you are in Python mode or JavaScript mode.
- Python uses `for i in range(4):`.
- JavaScript uses `for (let i = 0; i < 4; i++)`.
