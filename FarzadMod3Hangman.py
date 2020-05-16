# Mod 3 Hangman
# Author: Farzad Rahman
# Date Start: 29/04/20
# ICS3UI - 03, Ms. Harris

# Image from https://www.pinterest.ca/pin/52143308165138619/?nic_v1=1asA1I4s6KHdixSxLi6Evf0nnZe7fUHkozSMKxmWlJ%2F%2BdNKkfNCp3MsS%2FMlymxOdsG
"""
In
this option you will create a flowchart, and IPO
chart, and a trace table of one of your errors for
hangman. Weeks ago you were given a version 1 and
maybe a version 2 of hangman.  You are to complete this
task, use versioning and commit regularly as you add
each piece, nothing hardcoded. Your words will be input
from either a txt file or a csv file, your choice.  Your word
list should come from the week 5 up readings/quizzes OR
the Debates that have completed so far.

Complete Question 3 (b) on the Assignment 3, that has no due date - with the following changes;
- Use a txt, csv etc. file rather than a hard-coded word "secret".
- Add Error handing (catch the errors).
- Appropriate user messages so the user always knows their status (not gone off console screen)
-Hand into GitHub classroom - Module 3 new link below.

(optional - advanced) PyGame or Turtle graphics - nothing on the console.
"""

# Modifications:
# 30-04-20 - Added key-pressed acknowledgement


import pygame
import random

pygame.init() # Initializes all the modules
screen = pygame.display.set_mode((875, 673)) # Sets screen with given display size

# Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

words = []

# these lines read the lines in the file and adds to a list
file = open("Words_List.txt", "r")
while True:
    try:
        lines = file.readline()  # Reads in each line in the file.
    except:
        break
for parts in lines:
        words.append(parts.replace('\n', ''))

strikes = 0
answer = random.choice(words)
font_used = pygame.font.Font('CNN.ttf', 60) # Generates font
guessed = []

def background(image):
    #Displays background image
    picture = pygame.image.load(image)
    screen.blit(picture, (0, 0))
    pygame.display.flip()  # Puts the image on the screen
background('Background.png')

pygame.draw.rect(screen,WHITE,(50,577,875,20))  # Crosses out alphabet from image

def spaces(answer): # Generates spaces based on how many letters
    space = font_used.render("_", False, (BLACK))
    for i in range(len(answer)):
       screen.blit(space,(300+i*60,460))

def correct_letter(letter): # Displays letter when correctly chosen
    surface = font_used.render(letter, False, (BLACK))
    for i in range(len(answer)):
        if letter == answer[i]:
            screen.blit(surface, (300+i*60, 460))
    pygame.display.update()



def hang(): # Catches you if you choose wrong letter
    if strikes == 1:
        pygame.draw.circle(screen,BLACK,(272,180),30)
    elif strikes == 2:
        pygame.draw.line(screen,BLACK,(272,200),(272,320),5)
    elif strikes == 3:
        pygame.draw.line(screen,BLACK,(272,208),(360,270),5)
    elif strikes == 4:
        pygame.draw.line(screen,BLACK,(272,208),(184,270),5)
    elif strikes == 5:
        pygame.draw.line(screen,BLACK,(272,320),(184,382),5)
    elif strikes == 6:
        pygame.draw.line(screen,BLACK,(272,320),(360,382),5)
        game_over = font_used.render("Game Over", False, (BLACK))
        screen.blit(game_over,(300,300))
        pygame.display.update()
        pygame.time.delay(2000)
        raise EOFError




def word_bank(letter):  # Shows letters already guessed
    small_font = pygame.font.Font('CNN.ttf', 30)
    if len(letter) == 1: # Even if user pressed "," or "." they will get it wrong as they fail to comprehend what a letter is
        if letter not in guessed:
            guessed.append(letter)
            screen.blit(small_font.render(letter, False, (BLACK)), (20+30*len(guessed), 577))



run = True
while run:
    spaces(answer)
    pygame.display.update()
    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                KeyPressed = pygame.key.name(event.key)
                word_bank(KeyPressed)
                if KeyPressed in answer:
                    correct_letter(KeyPressed)
                else:
                    strikes += 1
                    hang()
    except:
        break
pygame.quit()