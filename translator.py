import speech_recognition as sr
from googletrans import Translator
import pyttsx3

# Initialize the translator and text-to-speech engine
translator = Translator()
engine = pyttsx3.init()

# Set voice properties for pyttsx3 (Optional, for better experience)
voices = engine.getProperty('voices')
for voice in voices:
    if "english" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def translate_voice():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Use the microphone as the audio source
    with sr.Microphone() as source:
        print("Listening for Hindi input... Speak now.")
        try:
            # Capture audio
            audio = recognizer.listen(source)
            print("Processing your speech...")

            # Recognize speech (in Hindi)
            hindi_text = recognizer.recognize_google(audio, language='hi-IN')
            print(f"Detected Hindi: {hindi_text}")

            # Translate to English
            translated_text = translator.translate(hindi_text, src='hi', dest='en').text
            print(f"Translated to English: {translated_text}")

            # Speak the translated text
            speak(translated_text)

        except sr.UnknownValueError:
            print("Sorry, could not understand your speech.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    translate_voice()
