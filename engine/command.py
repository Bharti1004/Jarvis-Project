import pyttsx3
import speech_recognition as sr

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    
    print(voices)
    engine.setProperty('voice', voices[0].id)  #yha pr voices jo bhi hogi hmaare paas usme
                                            # jo 1 no. pr hogi vo in use aajegi
    engine.setProperty('rate', 174)
    
    engine.say(text)
    engine.runAndWait()
    
def takecommand():
    
    r=sr.Recognizer()
    
    with sr.Microphone() as source:
        print('listening....')
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source)
        
        audio=r.listen(source,10,6)
        
    try:
        print('recognizing')
        query=r.recognize_google(audio,language='en-in')
        print(f"user said:{query}")
    except Exception as e:
        return ""
    
    return query.lower()

text=takecommand()
    
speak(text)
