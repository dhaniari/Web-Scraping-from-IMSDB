import re

def extract_dialogue(script):
    # Screenplays often follow a pattern where character names are in uppercase
    # and followed by lines of dialogue.
    lines = script.split("\n")
    dialogue = []
    
    character = None
    for line in lines:
        # If the line is uppercase, it's usually a character name
        if line.isupper():
            character = line.strip()
        # If it's not empty and it's under a character name, it's dialogue
        elif character and line.strip():
            dialogue.append(f"{character}: {line.strip()}")
            character = None  # Reset after the dialogue ends
    
    return dialogue

# Example usage
with open("some_movie_script.txt", "r") as f:
    script_text = f.read()

dialogue_lines = extract_dialogue(script_text)

# Output the first few dialogues
for line in dialogue_lines[:10]:
    print(line)
