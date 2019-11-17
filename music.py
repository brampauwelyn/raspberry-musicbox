from gpiozero import Button
import pygame

pygame.init()

# Adding sounds
bass = pygame.mixer.Sound("/home/pi/projects/raspberry-musicbox/samples/bass.wav")
piano = pygame.mixer.Sound("/home/pi/projects/raspberry-musicbox/samples/piano.wav")
beat = pygame.mixer.Sound("/home/pi/projects/raspberry-musicbox/samples/beat.wav")

pygame.mixer.init()

def say_hello():
  print("hello")

# Configure the buttons with the GPIO pins
btn_red = Button(17)
btn_blue = Button(27)
btn_yellow = Button(22)

# Play sounds when buttons are presssed
btn_red.when_pressed = say_hello
btn_blue.when_pressed = piano.play
btn_yellow.when_pressed = beat.play




