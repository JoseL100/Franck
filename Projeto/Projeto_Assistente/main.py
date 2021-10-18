
import speech_recognition as sr
import pyttsx3, pywhatkit, wikipedia, datetime, keyboard , os 
from pygame import mixer
import subprocess as sub
name='lee'
listener=sr.Recognizer()
engine=pyttsx3.init()

voices=engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)

sites={
    'google':'google.com',
    'youtube':'youtube.com',
    'facebook':'facebook.com',
    'faculdade':'impacta.edu.br'
}

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    
    try:
        with sr.Microphone() as source:
            print("escutando...")
            pc=listener.listen(source)
            rec=listener.recognize_google(pc,language='pt-br')
            rec=rec.lower()
            if name in rec:
                rec=rec.replace(name,"")
        
    except:
        pass
    return rec

def run():
    while True:
        rec=listen()
        if "video" in rec:#falar "ok"  depois o que voce precisa
            music=rec.replace("video",'')
            print('Reprodurindo'+ music)
            talk("Reproduzindo "+ music)# a voz da assistente
            pywhatkit.playonyt(music)#conexão com you_tube

        elif "buscar" in rec:
            buscar=rec.replace("buscar ", "")
            wikipedia.set_lang('es')
            wiki=wikipedia.summary(buscar,2)
            print(buscar+": " + wiki)
            talk (wiki)
        
        elif "alarme " in rec:
            num =rec.replace('alarme', '')
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
        
        # falta melhor a busca no sistema 
        # elif 'archivo' in rec:
        #     for file in files:
        #         if file in rec:
        #             sub.Popen([files[file]], shell=True)
        #             talk(f'abrindo {file}')
        
        #codigo para escrever no bloco de notas 
        elif 'escrever' in rec:
            try:
                with open("anotações.txt","r") as f:
                    write(f)
            except FileNotFoundError as e :
                file=open("anotações.txt","w")
                write(file)
        elif "termina" in rec:
            talk ("adios!")
            break
def write(f):
    talk("O que voce deseja escrever?")
    rec_write=listen()
    f.write(rec_write+ os.linesep)
    f.close()
    talk("tudo pronto, você pode revisar")
    sub.Popen("anotações.txt",shell=True)

    
if __name__=='__main__':
    run()
