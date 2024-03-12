import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
import pyaudio

#escuchar nuestro microfono y devolver el audio como texto
def transformar_audio_en_texto():

    #almacenar el recognizer en una variable
    r = sr.Recognizer()

    #configurar el microfono
    with sr.Microphone() as origen:

        #tiempo de espera al microfono
        r.pause_threshold = 0.8

        #informar que comoenzo la grabacion
        print("Ya puedes hablar")

        #guardar audio en una variable
        audio = r.listen(origen)

        try:
            #buscar en google lo que escuche
            pedido = r.recognize_google_cloud(audio,language="es-mx")

            #imprimir en pantalla lo que se ha hablado
            print(f"Digiste: {pedido}")

            #devolver a pedido
            return pedido
        
        except sr.UnknownValueError:
            #prueba de que no comprendio el audio
            print("ups no entendi")

            #devolver error
            return "sigo esperando"
        except sr.RequestError:
            #prueba de que no comprendio el audio
            print("ups no entendi 2")

            #devolver error
            return "sigo esperando 2"
        except:
            #prueba de que no comprendio el audio
            print("ups no entendi 3")

            #devolver error
            return "sigo esperando 3"
        

#funcion para que el asistente pueda escuchar
def hablar(mensaje):
    #encender el motor de pytts3
    engine = pyttsx3.init()
    engine.setProperty('voice',id1)

    #pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()


#verifica las voces que tenemos instaladas en el ordenadro
'''
engine = pyttsx3.init()
for voz in engine.getProperty('voices'):
    print(voz)
'''
id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
hablar("HOla Javier no te durmas si ya tienes sueño vete a dormir.")
