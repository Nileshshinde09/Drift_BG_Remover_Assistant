from greet import get_time_of_day,get_time_for_bye
from constant import HOST_NAME,DEVLOPER,CONFIRMATION_KEY,ASSISTANT_NAME

INITIAL_COMMAND = f'''
    Hello Good {get_time_of_day()} {HOST_NAME} . myself {ASSISTANT_NAME}. I am here to assist you for image generation task.
    '''
HELP_COMMAND =f"""
    Hey {HOST_NAME} . You need to cantact my devloper, { DEVLOPER } for any furthure assistance
"""

ERROR_COMMAND=f"""
    Sorry {HOST_NAME}, having trouble in processing your task ,{HELP_COMMAND}
"""
CONFIRMATION_COMMAND = f"""
    Press {CONFIRMATION_KEY} for confirmation.
"""

PROCESSING_TASK_COMMAND=f"""
    started to Processing Task!
"""
PROCESS_TERMINATION_COMMAND=f"""
    process terminated
"""
ASKING_OUT_COMMAND= """
           You can give me more task to get done!
"""
FOLDER_SELECTION_COMMAND= f"""
        You have to selecte folder for image processing task.
    """

def BYE_COMMAND():
    return f"""
     it's a fun to working with you ! , bye and {get_time_for_bye()} {HOST_NAME}
    """


def FOLDER_CONFIRMATION_COMMAND(folder_name):
    return f"""
        You have selected {folder_name} folder for image processing task. {CONFIRMATION_COMMAND}
    """
def IMAGE_PROCESSING_COMPLITION(imageIndex,newName):
   return f"""
        processing of Image {imageIndex} completed , new name assigned is {newName}. 
    """ 

def TASK_PROCESSING_COMPLITION(folder_name):
   return f"""
        Hey {HOST_NAME} ! Image Processing Task of folder name :{folder_name} is completed!  
    """
