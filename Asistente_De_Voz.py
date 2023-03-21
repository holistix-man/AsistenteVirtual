import speech_recognition as sr
import pyttsx3 as voz
import pywhatkit
import subprocess as sub
from datetime import datetime 
import wikipedia
import pyjokes

voice = voz.init()
voices = voice.getProperty('voices')
voice.setProperty('voice', voices[0].id)
voice.setProperty('rate', 140)


def say(text):
    voice.say(text)
    voice.runAndWait()

def search(query_google):
    pywhatkit.search(query_google)

def reproducir_musica(query_yt):
    pywhatkit.playonyt(query_yt)



while True:
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print('Escuchando...')
        audio=recognizer.listen(source, phrase_time_limit=3)

    try:
        comando = recognizer.recognize_google(audio, language='es-CL')
        print(f"Creo que dijiste '{comando}'")

        comando=comando.lower()
        comando = comando.split(' ')

        if 'asistente' in comando:
            if 'abre' in comando or 'abrir' in comando:

                sites={
                    'google': 'google.com',
                    'youtube': 'youtube.com',
                    'instagram': 'instagram.com',
                    'spotify' : 'open.spotify.com/',
                    'drive': 'drive.google.com/'
                }

                for i in list(sites.keys()):
                    if i in comando:
                        sub.call(f'start chrome.exe {sites[i]}', shell=True)
                        say(f"Abriendo {i}")

            elif 'hora' in comando:
                time = datetime.now().strftime('%H:%M')
                say(f"Son las {time}")

            elif 'buscar' in comando or 'busca' in comando or 'buscar en línea' in comando:
                query_google = ' '.join(comando[2:])
                search(query_google)
                say(f'Buscando {query_google} en google')

            elif 'reproduce' in comando:
                query_yt = ' '.join(comando[2:])
                reproducir_musica(query_yt)
                say(f'Reproduciendo {query_yt} en youtube')

        for i in ['termina', 'terminar','término']:
            if i in comando:
                say('Sesion finalizada')
                break

    except:
        print("No entendi, vuelve a decir")




