import pyttsx3

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    
    print(voices)
    engine.setProperty('voice', voices[0].id)  #yha pr voices jo bhi hogi hmaare paas usme
                                            # jo 1 no. pr hogi vo in use aajegi
    engine.setProperty('rate', 174)
    
    engine.say(text)
    engine.runAndWait()
    
speak("I love Coding")