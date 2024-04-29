from easygui import *
from commands import *
import easygui
from utils.listoutfile import *
from utils.createDir import *
from imageProcessing import *
from tqdm import tqdm

	
def run():
    speak(INITIAL_COMMAND)
    while True:
        try:
            speak(CONFIRMATION_COMMAND)
            output = ynbox(CONFIRMATION_COMMAND)
            if(output):
                speak(FOLDER_SELECTION_COMMAND)
            else:
                continue
            inputdir=easygui.diropenbox(title="Select folder ")
            # INPUT_DIR_PATH = inputdir.replace(inputdir.split('\\')[-1],'')
            INPUT_DIR_NAME = inputdir.split('\\')[-1]
            speak(FOLDER_CONFIRMATION_COMMAND(INPUT_DIR_NAME))
            output = ynbox(FOLDER_CONFIRMATION_COMMAND(INPUT_DIR_NAME))
            if(output):
                speak(PROCESSING_TASK_COMMAND)
            else:
                speak(PROCESS_TERMINATION_COMMAND)
                continue

            RESULT_PATH = create_directory(inputdir)
            files = list_jpeg_files(inputdir)
            for i in tqdm (range(len(files)), desc="Processing…", ascii=False, ncols=100):
                print("\n")
                val=files[i]
                imageProcessing(inputdir+'\\'+val,RESULT_PATH,i+1)
            TASK_PROCESSING_COMPLITION(folder_name=inputdir.split('\\')[-1])
            speak(ASKING_OUT_COMMAND)
            output = ynbox(ASKING_OUT_COMMAND)
            if(output):
                continue
            else:
                speak(BYE_COMMAND())
                exit(1)
        except Exception as e:
            print(e)
            speak(PROCESS_TERMINATION_COMMAND)
            speak(e)

if __name__=="__main__":
    run()