import serial
import threading

# Define the serial port and baud rate
SERIAL_PORT = '/dev/ttyACM0'  # Change this to your Arduino's serial port
BAUD_RATE = 9600

# Function to read from serial and print
def read_from_serial(ser):
    while True:
        if ser.in_waiting > 0:
            serial_data = ser.readline().decode().strip()
            print("Received from Arduino:", serial_data)

# Open serial port
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=0.1)

# Start a thread to read from serial
read_thread = threading.Thread(target=read_from_serial, args=(ser,))
read_thread.daemon = True
read_thread.start()

# Continuously send user input to Arduino
while True:
    user_input = input()
    if user_input.lower() == 'exit':
        break
    ser.write(user_input.encode())
    ser.write(b'\n')

# Close serial port
ser.close()
