#! @author Curvu
#! If you will do your own arduino program, you should debounce the buttons. It will prevent from errors.
import subprocess
import serial

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
def deck(red, white):
    line = serialPort.readline().strip() ## read line from serialPort
    if(line == b'R'): ## in arduino program if i click in button red it will print "Serial.println('R')"
        try:
            subprocess.call(red)
            print('Opening the red button program...')
        except OSError:
            print('Could not open program in the RED button')
    if(line == b'W'): ## in arduino program if i click in button white it will "Serial.println('W')"
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
serialPort.close() ## disconnect from serial port if loop stops
