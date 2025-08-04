from openai import OpenAI
import speech_recognition as sr
import pyttsx3
import os
from dotenv import load_dotenv

load_dotenv()  # Loads variables from .env into os.environ

# Initialize OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Reading Microphone as source
# listening the speech and store in audio_text variable
with sr.Microphone() as source:
    print("Talk")
    audio_text = r.listen(source)
    print("Time over, thanks")
    # recoginze_() method will throw a request
    # error if the API is unreachable,
    # hence using exception handling
    
    try:
        # using google speech recognition
        usrText = r.recognize_google(audio_text)
        print("Text: "+usrText)
        # Make a chat completion request
        response = client.chat.completions.create(
            model="gemini-1.5-flash",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": usrText}
            ]
        )
        # Print the response
        print(response.choices[0].message)
        result = response.choices[0].message.content
        print(result)
        pyttsx3.speak(result)


    except:
         pyttsx3.speak("Sorry, I did not get that")