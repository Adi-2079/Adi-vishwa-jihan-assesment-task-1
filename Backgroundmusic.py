import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from pygame import mixer 

mixer.init()
audio_file = os.path.dirname(__file__) + "\\background.mp3"
mixer.music.load(audio_file)
mixer.music.play(loops=-1)