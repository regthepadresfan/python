import pathlib
import os, time
import pygame

inputdirectory = r"c:/Users/Reggie/Music/Downloads"

initial_count = 0
for path in pathlib.Path("c:/Users/Reggie/Music/Downloads").iterdir():
    if path.is_file():
        initial_count += 1
print (f"There are {initial_count} audio files ")

list = os.listdir('c:/Users/Reggie/Music/Downloads')
print(list)


song = input("Enter the song you wish to play ")
file = os.path.join(inputdirectory, song)

pygame.init()
pygame.mixer.music.load(file)


while True:
    time.sleep(1)
    print("Enter 1 to play ")
    time.sleep(1)
    print("Enter 2 to pause ")
    time.sleep(1)
    print("Enter anything else to exit ")
    userInput = int(input())
    if userInput == 1:
        print("Playing some tunes ")
        pygame.mixer.music.play()
    elif userInput == 2:
        pygame.mixer.music.pause()
    else:
        exit()
