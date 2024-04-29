import os
from datetime import datetime
from speak import speak
from commands import ERROR_COMMAND
import random
import string

def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

def create_directory(directory_path):
    try:
        if os.path.exists(directory_path) != True:
            os.makedirs(directory_path+"-processed")
            speak_directory_path = directory_path.split("\\")[-1]
            print(f"Directory '{speak_directory_path}' created successfully.")
            speak(f"Directory '{speak_directory_path}' created successfully.")
            return directory_path+"-processed"
        else:
            speak_directory_path = directory_path.split("\\")[-1]
            print(f"Directory '{speak_directory_path}' already exists.")
            speak(f"Directory '{speak_directory_path}' already exists.")
            random_string = generate_random_string(10)
            DIR= directory_path+'-'+str(random_string)
            speak_DIR = speak_directory_path+'-'+str(random_string)
            os.makedirs(DIR)
            print(f"Directory '{speak_DIR}' created successfully.")
            speak(f"Directory '{speak_DIR}' created successfully.")
            return DIR
    except Exception as e:
        print(f"An error occurred: {e}")
        speak(ERROR_COMMAND)
        return -1