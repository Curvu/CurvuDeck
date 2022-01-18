# Made by Curvu
import subprocess
import serial
# from PIL import Image
# from pystray import Icon as icon, Menu as menu, MenuItem as item

'''
def start_App():
    image = Image.open(".\Scripts\icon-tray.ico")
    icon('CurvuDeck', image, menu=menu(item('Quit', stop_App), item('Show', doSomething))).run_detached()
'''

def doSomething():
    pass

'''
def stop_App(systray, item):
    systray.stop()
    exit()
'''

def findPort():
    global serialPort
    i = 1
    while i <= 6:
        port = 'COM' + str(i) # just switchig the port
        try:
            serialPort = serial.Serial(port, baudrate = 9600, timeout=0) # connect to serial
            print('Serial Port Using: "%s".' % port)
            break # if find the correct port, then break the loop
        except OSError:
            i += 1

def deck(red, white):
    line = serialPort.readline().strip() # read line from serialPort
    if(line == b'R'): # in arduino program if i click in button red it 'Serial.println('R')
        try:
            subprocess.call(red) # open the program
            print('Opening the red button program...')
        except OSError: # if cant open
            print('Could not open program in the RED button')
    if(line == b'W'): # in arduino program if i click in button white it 'Serial.println('W')
        try:
            subprocess.call(white) # open the program
            print('Opening the white button program...')
        except OSError: # if cant open
            print('Could not open program in the WHITE button')

red = 'C:\\Users\\Utilizador\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe'
white = ''

findPort() # call function to find the correct port
while True: # forever loop
    deck(red, white)
serialPort.close() # close the program
