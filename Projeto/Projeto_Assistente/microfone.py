from typing import Text
from vosk import Model, KaldiRecognizer
import pyaudio
import pyttsx3

engine=pyttsx3.init()

voices=engine.getProperty('voices')
engine.setProperty('voice',voices[-2].id)
engine.setProperty('rate',180)

def talk(text):
    engine.say(text)
    engine.runAndWait()
def recog():
    talk('Escutando...')
    model=Model(r'vosk-model-small-pt-0.3')
    recognizer= KaldiRecognizer(model,16000)

    cap=pyaudio.PyAudio()
    stream = cap.open (format=pyaudio.paInt16,channels=1,rate=16000,input=True,frames_per_buffer=8192)
    stream.start_stream()

    while True:
        t=''
        data=stream.read(4096)
        if recognizer.AcceptWaveform(data):
            
            resul=recognizer.FinalResult()
            print(recognizer.FinalResult()) 
            for i in resul:
                t+=i
        
        t_news=t.replace('text','')
        t_news=t_news.replace(':','')
        t_news=t_news.replace('{','')
        t_news=t_news.replace('}','')
        t_news=t_news.replace('"','')
        # t_news=t_news.replace(' ','')
        if "buscar"  in t_news:
            return t_news
        elif "alarme" in t_news:
            return t_news
        elif "reproduzir" in t_news:
            return t_news
        elif "escrever" in t_news:
            return t_news
        elif "terminar" in t_news:
            return t_news
            



# t=recog()
# print(t+' finalmente porra')


# s = "Naze{{{{{{{}}}}}+++"
# new_s = s[:0]+s[:4]
# print(new_s)

# # r='foda se o mundo '
# l=['jose','luis','merma','pinedo',]
# x=True

# for i in l:
#     if i in r:
#         print('foi essa merda')
#     else:
#         print('merda de sistema')