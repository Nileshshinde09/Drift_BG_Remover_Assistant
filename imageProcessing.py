
#--------------------------------------------------------------------------------------------------
# All global Import's
import string
from PIL import Image
import easygui
from rembg import remove

# All local Import's
from speak import speak
from constant import *
from constants.ano_names import *
from utils.listoutfile import *
from random import randint
from commands import *
from commands import *
from Database_utilities import *
#--------------------------------------------------------------------------------------------------

def imageProcessing(inputfilepath,savefilepath,index):
    print(inputfilepath)
    print(savefilepath)
    print(index)

    try:
        iNG=ImageNameGenerator()
        # inputfilepath = easygui.fileopenbox(title="Select folder ")
        inp = Image.open(inputfilepath)
        output = remove(inp)
        ANO_NAME_RESULT=iNG.get_random_unique_name()
        out_img = savefilepath+"\\"+ ANO_NAME_RESULT
        print(out_img)
        if out_img:
            output.save(out_img)
            speak(IMAGE_PROCESSING_COMPLITION(index,ANO_NAME_RESULT))
    except Exception as e:
        print(f"An error occurred: {e}")
        speak(ERROR_COMMAND)

