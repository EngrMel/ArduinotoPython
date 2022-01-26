import serial

arduino = serial.Serial('COM6', 9600) # connecting to port and defining baudrate

def readArduino():
    try:
        value = arduino.readline() #getting the incoming data
        val = str(value, 'utf') #used for converting the arduino data
        print(val) #print the incoming data

    except:
        print("failed to connect") #error message if we can't connect to Arduino
        exit()

while True: #loop to continuously execute the function
    readArduino() # calling the function



