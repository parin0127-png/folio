import threading, os
from gtts import gTTS
import playsound

def reminders(message: str, seconds: int):
    """set a reminder or alert that will notify after a specified number of seconds"""
    try:
        def remind():
            print(f"> Reminder: {message}")
            tts = gTTS(text = message, lang = "en", tld = "com.au")
            tts.save("reminder.mp3")
            playsound.playsound("reminder.mp3")
            os.remove("reminder.mp3")
            
        timer = threading.Timer(seconds, remind)
        timer.start()
        return f"> Reminder set for {seconds} seconds: {message}"
    except Exception as e:
        return f"> Reminder failed: {str(e)}"

