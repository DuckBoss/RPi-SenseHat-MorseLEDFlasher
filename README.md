# RPi-SenseHat-MorseLEDFlasher
Flashes a message through the RPi SenseHat LEDs in Morse.

### This project requires Python 3, and it can only be run on raspberry pi devices with an attached sensehat.

  
## Dependencies:
- sense-hat (can be installed with pip)

## Usage:
- Format: 'python3 morse_transcriber.py \<message> \<color>'
  
  Example: Runs the morse_transcriber script with the message "Test Message" with Blue (RGB) LED colours.
  ```
  python3 morse_transcriber.py "Test Message" 0,0,255
  ```
  
  ![Morse GIF](https://user-images.githubusercontent.com/20238115/39659594-b68a7eb2-4ff9-11e8-9c28-b5388f6547ea.gif)

