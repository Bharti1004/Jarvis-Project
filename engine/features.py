# from playsound import playsound

# #playing assistant sound function
# def playAssistantSound():
#     music_dir="www\\assets\\audio\\start_sound.mp3"
#     playsound(music_dir)

import os
import eel
from playsound import playsound

@eel.expose

# Define the function
def playAssistantSound():
    music_dir = os.path.abspath("www/assets/audio/start_sound.mp3")
    print("Playing:", music_dir)  # Debugging: Check if the path is correct
    playsound(music_dir)

# Call the function to test
if __name__ == "__main__":
    playAssistantSound()

