import sys
from time import sleep
from sense_hat import SenseHat

class Morse:
    senseHat = None
    sentence = None
    multiplierSpeed = 1
    transcriber = None

    flashColor = [255,255,255]
    loop = False

    def __init__(self):
        if len(sys.argv) < 2:
            print("ERROR: This script requires a string argument to convert to morse.")
            sys.exit(1)

        if len(sys.argv) == 3:
            self.flashColor = list(map(int, sys.argv[2].split(',')))
            print("Custom Flash Color Added!")

        if len(sys.argv) == 4:
            if sys.argv[3] == "True":
                self.loop = True

        self.senseHat = SenseHat()
        self.senseHat.low_light = False

        self.sentence = sys.argv[1]
        self.multiplierSpeed = 1
        self.transcriber = MorseTranscriber()
        self.transcriber.set_color(self.flashColor)

        print("RPI Sense Hat Morse Code Flasher Initialized!")
        self.flash_sentence()

    def flash_sentence(self):
        morseSentence = self.transcriber.sentence_to_morse(self.sentence, self.senseHat, self.flashColor, self.loop)
        print(morseSentence)

class MorseTranscriber:
    morseDefinitions = {
        'a':'.-',
        'b':'-...',
        'c':'-.-.',
        'd': '-..',
        'e': '.',
        'f': '..-.',
        'g': '--.',
        'h': '....',
        'i': '..',
        'j': '.---',
        'k': '	-.-',
        'l': '.-..',
        'm': '--',
        'n': '-.',
        'o': '---',
        'p': '.--.',
        'q': '--.-',
        'r': '.-.',
        's': '...',
        't': '-',
        'u': '..-',
        'v': '...-',
        'w': '.--',
        'x': '-..-',
        'y': '-.--',
        'z': '--..',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        '0': '-----',
        '.': '.-.-.-',
        ',': '--..--',
        ':': '---...',
        '?': '..--..',
        '\'': '.----.',
        '/': '-..-.',
        '(': '-.--.-',
        ')': '-.--.-',
        '@': '.--.-.',
        '=': '-...-',
        '-': '-....-',
        '\"': '.-..-.',
        ' ': ' '
    }

    standardDur = 500 # ms
    multiplierDur = 3
    frequency = 550

    def set_color(self, color):
        self.X = color

    def sentence_to_morse(self, sentence, senseHat, morseFlash, loop):
        morseSentence = ""
        senseHat.clear()
        print(sentence)

        morseFlasher = [morseFlash] * 64
        print(morseFlasher)

        while True:
            for letter in sentence.lower():
                morseChar = str(self.morseDefinitions.get(letter))
                morseSentence += morseChar

                senseHat.clear()
                print(morseChar)
                for char in morseChar:
                    senseHat.clear()

                    if char == ".":
                        senseHat.set_pixels(morseFlasher)
                        sleep(self.dot() / (1000))

                        print(self.dot()/1000)
                        senseHat.clear()
                    elif char == "-":
                        senseHat.set_pixels(morseFlasher)
                        sleep(self.dash() / (1000))
                        print(self.dash() / 1000)
                        senseHat.clear()
                    elif char == " ":
                        senseHat.clear()
                        sleep(self.spaceWords()/(1000))
                        print(self.spaceWords() / 1000)
                        continue
                    sleep(self.dot()/1000)

                sleep(self.spaceLetters()/(5000))

            sleep(2)
            if not loop:
                break

        return morseSentence



    def dot(self):
        return int(self.standardDur / self.multiplierDur)
    def dash(self):
        return int(3 * (self.standardDur / self.multiplierDur))
    def spaceChar(self):
        return self.dot()
    def spaceLetters(self):
        return self.dash()
    def spaceWords(self):
        return int(7 * (self.standardDur / self.multiplierDur))

if __name__ == '__main__':
    newInstance = Morse()






