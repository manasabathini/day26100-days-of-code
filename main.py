from replit import audio
import os, time

def play():
  source = audio.play_file('audio.wav')
  source.paused = False # unpause the playback
  while True:
    # Start taking user input and doing something with it
    stop_playback = int(input("Press 2 anytime to stop playback and go back to the menu : "))
    if stop_playback == 2:
      source.paused = True
      return
    else:
      continue

while True:
  # clear the screen 
  os.system("clear")
  print(" MyPOD Musix player")
  time.sleep(1)
  print("Press 1 to Play")
  time.sleep(1)
  print("Press 2 to Exit")
  time.sleep(1)
  print("Press anything else to see the menu again")
  # Show the menu
  userInput = int(input())
  # take user's input
  if userInput == 1:
    print("Playing som eproer tunes!")
    play()
  elif userInput == 2:
    exit()
  else:
    continue

