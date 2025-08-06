from openai import OpenAI
import speech_recognition as sr
import pyttsx3
import os
from dotenv import load_dotenv

load_dotenv()  


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)


r = sr.Recognizer()

\
with sr.Microphone() as source:
    print("speak....")
    audio_text = r.listen(source)
    print("Time over, thanks")
   
    
    try:
        
        usrText = r.recognize_google(audio_text)
        print("Text: "+usrText)
      
        response = client.chat.completions.create(
            model="gemini-1.5-flash",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": usrText}
            ]
        )
        
        print(response.choices[0].message)
        result = response.choices[0].message.content
        print(result)
        pyttsx3.speak(result)


    except:
         pyttsx3.speak("Sorry, I did not get that")