import pyttsx3
import speech_recognition as sr
import subprocess
import datetime
import requests

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Initialize speech recognizer
recognizer = sr.Recognizer()

# OpenWeatherMap API Key (sign up on openweathermap.org to get your API key)
api_key = "YOUR_API_KEY"
weather_api_url = "https://api.openweathermap.org/data/2.5/weather"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5)
        try:
            recognized_text = recognizer.recognize_google(audio)
            print("You said: " + recognized_text)
            return recognized_text.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't understand what you said.")
            return ""
        except sr.RequestError:
            print("Sorry, I encountered an error while processing your request.")
            return ""

def open_app(app_name):
    try:
        if "notepad" in app_name:
            subprocess.Popen(["notepad.exe"])
        elif "google" in app_name:
            subprocess.Popen(["google.exe"])
        elif "youtube" in app_name:
            subprocess.Popen(["youtube.exe"])        
        elif "facebook" in app_name:
            subprocess.Popen(["facebook.exe"])
        elif "appstore" in app_name:
            subprocess.Popen(["appstore.exe"]) 
        elif "safari" in app_name:
            subprocess.Popen(["safari.exe"])
        elif "instagram" in app_name:
            subprocess.Popen(["instagram.exe"]) 
        elif "play store" in app_name:
            subprocess.Popen(["playstore.exe"])
        elif "calculator" in app_name:
            subprocess.Popen(["calc.exe"])
        elif "spotify" in app_name:
            subprocess.Popen(["spotify.exe"])
        elif "wynk" in app_name:
            subprocess.Popen(["wynk.exe"])
        elif "calculator" in app_name:
            subprocess.Popen(["calc.exe"]) 
        elif "whatsapp" in app_name:
            subprocess.Popen(["C:\\Path\\to\\WhatsApp.exe"])  # Provide the correct path to WhatsApp.exe
        else:
            speak("Sorry, I don't know how to open that application.")
    except Exception as e:
        speak("An error occurred while opening the application.")

def get_current_time():
    current_time = datetime.datetime.now().strftime("%H:%M")
    speak("The current time is " + current_time)

def get_weather():
    city = "YOUR_CITY"
    params = {"q": city, "appid": api_key, "units": "metric"}
    response = requests.get(weather_api_url, params=params)
    weather_data = response.json()
    if weather_data.get("main") and weather_data.get("weather"):
        temperature = weather_data["main"]["temp"]
        weather = weather_data["weather"][0]["description"]
        speak(f"The weather in {city} is {weather} with a temperature of {temperature} degrees Celsius.")
    else:
        speak("Sorry, I couldn't retrieve the weather information.")

def main():
    speak("Hello! How can I assist you today?")
    
    while True:
        command = listen()
        
        if "hello" in command:
            speak("Hello! How can I assist you today?")
        elif "how are you" in command:
            speak("I'm just a computer program, but I'm doing well. How can I help you?")
        elif "open" in command:
            app_name = command.replace("open", "").strip()
            open_app(app_name)
        elif "what's the time" in command:
            get_current_time()
        elif "what's the weather" in command:
            get_weather()
        elif "goodbye" in command:
            speak("Goodbye! Have a great day.")
            break
        else:
            speak("I'm not sure how to respond to that.")

if __name__ == "__main__":
    main()
