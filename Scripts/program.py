import subprocess
import serial
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

def findPort():
    global serialPort
    i = 1
    while i <= 6:
        port = 'COM' + str(i)
        try:
            serialPort = serial.Serial(port, baudrate = 9600, timeout=0)
            print('Serial Port Using: "%s".' % port)
            break
        except OSError:
            i += 1

def deck(red, white):
    line = serialPort.readline().strip()
    if(line == b'R'):
        try:
            subprocess.call(red)
            print('Opening the red button program...')
        except OSError:
            print('Could not open program in the RED button')
    if(line == b'W'):
        try:
            subprocess.call(white)
            print('Opening the white button program...')
        except OSError:
            print('Could not open program in the WHITE button')

red = 'C:\\Users\\Utilizador\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe'
white = ''

#start_App()
findPort()
while True:
    deck(red, white)