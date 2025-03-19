# from playsound import playsound

# #playing assistant sound function
# def playAssistantSound():
#     music_dir="www\\assets\\audio\\start_sound.mp3"
#     playsound(music_dir)

import os
import re
import eel
from playsound import playsound
from engine.command import speak
from engine.config import ASSISTANT_NAME
import pywhatkit as kit

@eel.expose

# Define the function
def playAssistantSound():
    music_dir = "www\\assets\\audio\\start_sound.mp3"
    print("Playing:", music_dir)  # Debugging: Check if the path is correct
    playsound(music_dir)

# Call the function to test
if __name__ == "__main__":
    playAssistantSound()
    
    
def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    if query!="":
        speak("Opening"+query)
        print(f"Opening: {query}")
        os.system('start'+query)
    else:
        speak("not found")


def PlayYoutube(query):
    
    search_term = extract_yt_term(query)
    speak("Playing "+search_term+" on YouTube")
    kit.playonyt(search_term)
    
def extract_yt_term(command):
    pattern= r'play\s+(.*?)\s+on\s+youtube'
    
    match=re.search(pattern,command,re.IGNORECASE)
    return match.group(1) if match else None