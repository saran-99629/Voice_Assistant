import speech_recognition as sr
import pyttsx3 
import pywhatkit
import datetime
import wikipedia
import pyjokes 


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
  engine.say(text)
  engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'darling' in command:
                command = command.replace('darling', '')
                print(command)
    except:
        pass
        return command

def run_darling():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing..' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is...' +time)
    elif 'who is ' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry,Go with your girl friend')
    elif ' single' in command:
        talk('sorry, I have a Boy friend')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'saran' in command:
        talk('he is an brillant , smart person')
    elif 'create' in command:
        talk('Saran created me , he is such an nice person and i always love him ')
    elif 'sister' in command:
        talk('saran sister is monika sree')
    else:
        talk('please say the command again')



while True:
   run_darling()
