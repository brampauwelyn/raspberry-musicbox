from gpiozero import Button
from signal import pause
import pygame

bass = pygame.mixer.Sound("/samples/bass.wav")

btn_red = Button(17)
btn_blue = Button(27)
btn_yellow = Button(22)

btn_red.when_pressed = bass.play


