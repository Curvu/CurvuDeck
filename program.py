import subprocess
import serial

port = 'COM4'
serialPort = serial.Serial(port, baudrate=9600, timeout=0)
line = serialPort.readline().strip()

red = 'C:\\Users\\Utilizador\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe' # this is an example
white = '"C:\\Riot Games\\Riot Client\\RiotClientServices.exe" --launch-product=league_of_legends --launch-patchline=live' # Another example

while True:
    line = serialPort.readline().strip()
    if(line == b'R'):
        try:
            subprocess.call(red)
            print('Opening program of red button...')
        except OSError:
            print('Could not open program in the RED button')
    if(line == b'W'):
        try:
            subprocess.call(white)
            print('Opening program of white button...')
        except OSError:
            print('Could not open program in the WHITE button')
