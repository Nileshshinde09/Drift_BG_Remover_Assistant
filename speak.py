from constant import ASSISTANT,RATE,VOLUME
import pyttsx3
def speak(input):
    engine = pyttsx3.init()

    """ RATE"""
    rate = engine.getProperty('rate')                          
    engine.setProperty('rate', RATE)     


    """VOLUME"""
    volume = engine.getProperty('volume')                            
    engine.setProperty('volume',VOLUME)    

    """VOICE"""
    voices = engine.getProperty('voices')      
    if(ASSISTANT == "Male"): 
        engine.setProperty('voice', voices[0].id)  
    else:   
        engine.setProperty('voice', voices[1].id)   

    engine.say(input)

    engine.runAndWait()
    engine.stop()