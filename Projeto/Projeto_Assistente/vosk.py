import vosk
import pyaudio

model= Model(r"C:\Users\JoseL\Desktop\Franck\Projeto\Projeto_Assistente\vosk-model-small-pt-0.3")
recognizer=KaldiRecognizer(model,16000)

cap=pyaudio.PyAudio()
stream=cap.open(format=pyaudio.paInt16,channels=1,rate=16000,input=True, frames_per_buffer=8192)
stream.start_stream()

while True:
    data=stream.read(4096)
    if recognizer.AcceptWaveform(data):
        print(recognizer.Result())