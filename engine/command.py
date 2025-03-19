import pyttsx3
import eel
import speech_recognition as sr
import time

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    
 
    engine.setProperty('voice', voices[0].id)  #yha pr voices jo bhi hogi hmaare paas usme
                                            # jo 1 no. pr hogi vo in use aajegi
    engine.setProperty('rate', 174)
    eel.DisplayMessage(text)
    # eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()
    

def takecommand():
    
    r=sr.Recognizer()
    
    with sr.Microphone() as source:
        print('listening....')
        eel.DisplayMessage('listening....')
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source)
        
        audio=r.listen(source,10,6)
        
    try:
        print('recognizing')
        eel.DisplayMessage('recognizing....')
        query=r.recognize_google(audio,language='en-in')
        print(f"user said:{query}")
        eel.DisplayMessage(query)
        time.sleep(2)
        eel.ShowHood()
    except Exception as e:
        return ""
    
    return query.lower()

# text=takecommand()
    
# speak(text)

@eel.expose
def allCommands():
    query=takecommand()
    print(query)
    
    if "open" in query:
        from engine.features import openCommand
        openCommand(query)
    elif "on youtube" in query:
        from engine.features import PlayYoutube
        PlayYoutube(query)
    else:
        print("not run")   
        
    eel.ShowHood() 
    