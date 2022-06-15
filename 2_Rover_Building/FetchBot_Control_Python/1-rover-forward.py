# Robot forward
import time  # Import the Time library
import gpiozero # Import the GPIO Zero Library

right_motor = gpiozero.Motor(9, 10)
left_motor = gpiozero.Motor(7, 8)

# Forward: Turn both motors on with a speed of 0.5
left_motor.forward(0.5)
right_motor.forward(0.5)

# Wait for 1 seconds
time.sleep(1)

# Turn the motors off
left_motor.stop()
right_motor.stop()
