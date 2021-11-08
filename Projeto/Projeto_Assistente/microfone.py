
#Nao mexer mais nesse codigo.

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
        elif "abrir" in t_news:
            return t_news
        else:
            talk("Não compriendo...")
            