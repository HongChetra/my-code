import pyttsx3
import speech_recognition as sr 
import datetime

engine = pyttsx3.init("sapi5")

voices = engine.getProperty("voices")
print(voices)

engine.setProperty("voice", voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def Mytalk():
    time = int(datetime.datetime.now().hour)

    if time >= 0 and time <12:
        speak("Good Morning Sir!")
    
    elif time >=12 and time<18:
        speak("Good afternoon Sir!")

    else:
        speak("It's night time Sir, it's time to go to bed. Have a good dream sir!")

    speak("I am Jezz. What Can I help you?")

def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1 
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-uk')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Please say again!")

        return 'home'
    return query

if __name__ == "__main__":
    Mytalk()
    speak("Happy")
    takeCommand()