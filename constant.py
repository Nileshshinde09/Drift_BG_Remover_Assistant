import socket
from datetime import datetime
HOST_NAME=socket.gethostname()
ASSISTANT = 'Female' #Male
RATE=175
VOLUME=1.0
DEVLOPER= "Nilesh Shinde"
TIME=datetime.now().hour
CONFIRMATION_KEY = "Yes"
if(ASSISTANT=='Female'):
    ASSISTANT_NAME='FREDY'
else:
    ASSISTANT_NAME="JARVIS"

