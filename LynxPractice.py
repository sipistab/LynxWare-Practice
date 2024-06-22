import sys
import random
import time
import math

# List of characters to practice
characters = [
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "k", "m", "n", "o", "p", "q", "r", "s", "j", "l", "t", "u", "v", "w", "x", "y", "z"
]

if sys.platform == 'win32':
    import msvcrt
    def get_input():
        return msvcrt.getch().decode()

def practice_keyboard(characters):
    random.shuffle(characters) 
    tested_characters = set()
    faults = 0
    start_time = time.time()
    
    while not tested_characters >= set(characters):
        for char in characters:
            if char not in tested_characters:
                print("Press :  ", char)
                while True:
                    input_char = get_input()
                    if input_char == char:
                        print("GOOD!")
                        tested_characters.add(char)
                        break
                    else:
                        faults += 1
                        print(f"{input_char} - BAD! TRY: {char}")
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    score = elapsed_time + math.ceil(faults)
    print("Session time:", elapsed_time, "seconds")
    print("Faults:", faults)
    print("Score:", math.ceil(score))

def main():
    print("TEST YOUR DEXTERITY.")
    input_text = input("ENTER to start the session ")
    if input_text.lower() == 'submit':
        return
    while True:
        practice_keyboard(characters)
        input_text = input("SUBMIT to end the session; ENTER to test again ")
        if input_text.lower() == 'submit':
            break

if __name__ == "__main__":
    main()