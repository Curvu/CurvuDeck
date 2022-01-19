#! @author Curvu
#! The things that are commented out (that are code) I'll try to use them in the future
import subprocess
import serial
'''
from PIL import Image
from pystray import Icon as icon, Menu as menu, MenuItem as item

def start_App():
    image = Image.open(".\Scripts\icon-tray.ico")
    icon('CurvuDeck', image, menu=menu(item('Quit', stop_App), item('Show', doSomething))).run_detached()

def doSomething():
    pass

def stop_App(systray, item):
    systray.stop()
    exit()
'''
#$ Find the correct port
def findPort():
    global serialPort ## global variable so i can use in the other functions
    i = 1 ## Interval of ports: [1,6]
    limit = 6 ## But you can change the the variable 'limit' and put 7, 8, etc.
    while i <= limit:
        port = 'COM' + str(i) ## just switchig the port
        try:
            serialPort = serial.Serial(port, baudrate = 9600, timeout=0) ## connect to serial
            print('Serial Port Using: "%s".' % port)
            break ## if find the correct port, then break the loop
        except OSError:
            i += 1

#$ Read from serial port
##
def deck(red, white):
    line = serialPort.readline().strip() ## read line from serialPort
    if(line == b'R'): ## in arduino program if i click in button red it 'Serial.println('R')
        try:
            subprocess.call(red)
            print('Opening the red button program...')
        except OSError:
            print('Could not open program in the RED button')
    if(line == b'W'): ## in arduino program if i click in button white it 'Serial.println('W')
        try:
            subprocess.call(white)
            print('Opening the white button program...')
        except OSError:
            print('Could not open program in the WHITE button')
      
#! You may change the value on 'red' and 'white' variables
red = 'C:\\Users\\Utilizador\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe'
white = ''

#! Might have some problems but i'll try to fix them later
findPort() ## call function to find the correct port
while True: ## forever loop
    deck(red, white) ## call function to start reading from port
serialPort.close() ## disconnect from serial port
