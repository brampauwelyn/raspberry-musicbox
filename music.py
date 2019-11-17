from gpiozero import Button, LED
import os
import pygame
from time import sleep

pygame.init()

path = os.path.realpath(__file__)
directory = os.path.dirname(path) 

# Adding sounds
piano = pygame.mixer.Sound(directory + "/samples/piano.wav")
bass = pygame.mixer.Sound(directory + "/samples/bass.wav")
beat = pygame.mixer.Sound(directory + "/samples/ambi.wav")

# Configure the buttons with the GPIO pins
btn_red = Button(17)
btn_blue = Button(27)
btn_yellow = Button(22)

# Configure the LEDS
led_blue = LED(18)


def blue_pressed():
  piano.play()
  led_blue.on()

# Play sounds when buttons are presssed
while True:
  btn_red.when_pressed = bass.play
  btn_blue.when_pressed = blue_pressed
  btn_blue.when_released = led_blue.off
  btn_yellow.when_pressed = beat.play




