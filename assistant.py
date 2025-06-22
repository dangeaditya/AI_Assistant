import speech_recognition as sr
import os
import time
from playsound import playsound

# PATH TO YOUR VOICE FILES
VOICE_FOLDER = "voices"

# Keywords and their corresponding audio replies
voice_responses = {
    "hey jarvis":"hi_reply.mp3",
    "how are you": "how_are_you.mp3",
    "open youtube": "youtube_open.mp3",
    "shutdown": "shutdown.mp3"
}

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Speak now...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            command = recognizer.recognize_google(audio).lower()
            print("✅ Heard:", command)
            return command
        except Exception as e:
            print("❌ Error:", str(e))
            return ""

def handle_command(command):
    for key in voice_responses:
        if key in command:
            filepath = os.path.join(VOICE_FOLDER, voice_responses[key])
            if os.path.exists(filepath):
                print(f"▶️ Playing voice reply for: {key}")
                playsound(filepath)
                return
            else:
                print(f"⚠️ File not found: {filepath}")
                return

    print("🤷‍♂️ No matching voice response.")

# MAIN LOOP
if __name__ == "__main__":
    print("🎧 Jarvis (Voice Playback Edition) Ready.")
    while True:
        command = listen_command()
        if command:
            handle_command(command)
        time.sleep(1)
