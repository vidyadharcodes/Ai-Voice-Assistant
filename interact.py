import os
import pyttsx3
import speech_recognition as sr
import google.generativeai as genai
from dotenv import load_dotenv

# Load API Key from environment
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Configure the API key for Gemini API
genai.configure(api_key=API_KEY)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        speak("Say that again please...")
        return "None"
    return query


if __name__ == '__main__':
    # Initialize the chat model
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Start the chat with an initial message (if any)
    chat = model.start_chat(
        history=[
            {"role": "user", "parts": "Hello"},
            {"role": "model", "parts": "Great to meet you. What would you like to know?"},
        ]
    )

    speak("Chat initialized. You can start talking to the AI. Say 'exit' to end the conversation.")
    print("Chat initialized. You can start talking to the AI. Say 'exit' to end the conversation.")

    while True:
        # Take user input
        user_input = takecommand().lower()

        # Check if the user wants to exit
        if user_input in ["exit", "quit"]:
            speak("Goodbye!")
            print("Goodbye!")
            break

        # Send the user input to the chat model and get a response
        response = chat.send_message(user_input)
        model_response = response.text

        # Output the model's response
        print(f" {model_response}")
        speak(model_response)

        #results = wikipedia.summary(query, sentences=2)
