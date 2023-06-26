from gtts import gTTS

import playsound as ps

def text_to_speech():
    
    tts = gTTS(text='hello world',lang='en')

    tts.save('sound.mp3')
    
    ps.playsound('sound.mp3')

text_to_speech()