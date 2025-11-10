import random
import pyttsx3

# Initialize text-to-speech engine
try:
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
except Exception:
    engine = None

def speak(text: str) -> None:
    """Speak text if TTS engine is available. Silent no-op on failure."""
    try:
        if engine:
            engine.say(text)
            engine.runAndWait()
    except Exception:
        # If speaking fails for any reason, ignore so game still works.
        pass

# Snake, Water, Gun game
choices = {"s": "Snake", "w": "Water", "g": "Gun"}
youdict = {"s": 0, "w": 1, "g": 2}
reversedict = {0: "s", 1: "w", 2: "g"}

# Computer makes a random choice
computer = random.randint(0, 2)

# User input
youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()
if youstr not in youdict:
    print("Invalid input!")
    speak("Invalid input")
    exit()

you = youdict[youstr]

print(f"Computer choice: {choices[reversedict[computer]]}")
print(f"Your choice: {choices[youstr]}")
speak(f"Computer chose {choices[reversedict[computer]]}. You chose {choices[youstr]}.")

# Game logic
if computer == you:
    print("It's a tie!")
    speak("It's a tie")
elif (computer == 0 and you == 1) or (computer == 1 and you == 2) or (computer == 2 and you == 0):
    print("You win!")
    speak("You win")
else:
    print("You lose!")
    speak("You lose")