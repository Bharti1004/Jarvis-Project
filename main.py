import os

import eel

<<<<<<< HEAD
eel.init("www")

=======
from engine.features import *

eel.init("www")

playAssistantSound()

>>>>>>> 8c8b51f (Jarvis)
os.system('start msedge.exe --app="http://localhost:8000/index.html"')
eel.start('index.html', mode=None, host='localhost', block=True)