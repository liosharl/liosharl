import speech_recognition as sr
import pyttsx3

def listen_for_command():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Listening for a command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

def respond(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()

def main():
    respond("Hello, I am your basic MARY How can I assist you?")

    while True:
        command = listen_for_command()

        if command is not None:
            if "hello" in command:
                respond("Hello! How can I help you?")
            elif "goodbye" in command:
                respond("Goodbye!")
                break
            else:
                respond("I'm sorry, I cannot perform that task.")

if __name__ == "__main__":
    main()
