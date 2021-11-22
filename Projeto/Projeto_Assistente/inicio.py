from tkinter import font
from typing_extensions import runtime

import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime
import keyboard
import os
from pygame import mixer
import subprocess as sub
# import para criar interface
import requests
from tkinter import *         #
from PIL import Image,ImageTk # interagir com imagens

#
from microfone import recog
# import interface 
sites={
    'google':'google.com',
    'youtube':'youtube.com',
    'facebook':'facebook.com',
    'faculdade':'impacta.edu.br'
}
programas={
    'steam':r"C:\Program Files\steam\Steam.exe"


}
name='L'
microfone=sr.Recognizer()
engine=pyttsx3.init()

voices=engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',180)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def run():
    while True:
        rec=recog()
        print(rec)        
        if "exibir" in rec:#falar "falar"  depois o que voce precisa
            music=rec.replace("exibir",'')
            talk("exibir"+ music)# a voz da assistente
            pywhatkit.playonyt(music)#conexão com you_tube
        
        elif "pesquisa" in rec:
            buscar=rec.replace("pesquisa", "")
            wikipedia.set_lang('pt')
            wiki=wikipedia.summary(buscar,2)
            talk (wiki)
            # interface.write_text(buscar+": " + wiki)
        
        elif "alarme " in rec:
            num =rec.replace('alarme','')
            num=num.strip()
            talk("alarme ativara as " + num + "horas")
            while True:
                if datetime.datetime.now().strftime('%H:%M')==num:
                    print("Acorda!!!")
                    mixer.init()
                    mixer.music.load("DiE4u - Bring Me The Horizon Rain Paris Cover_160k.mp3")
                    mixer.music.play()
                    if keyboard.read_key()=="s":
                        mixer.music.stop()
                        break
        elif 'abrir' in rec:
            for site in sites:
                if site in rec:
                    sub.call(f"start opera.exe {sites[site]}",shell=True)
                    talk(f"abrindo {site}")
            for app in programas:
                if app in rec:
                    talk(f"abrir{app}")
                    os.startfile(programas[app])
        elif 'escrever' in rec:
            try:
                with open("anotações.txt","r") as f:
                    write(f)
            except FileNotFoundError as e :
                file=open("anotações.txt","w")
                write(file)
        elif "terminar" in rec:
            talk ("ATE A PROXIMA!!!")
            break
        
def write(f):
    talk("O que voce deseja escrever?")
    rec_write=recog()
    f.write(rec_write+ os.linesep)
    f.close()
    talk("tudo pronto, você pode revisar")
    sub.Popen("anotações.txt",shell=True)

        
