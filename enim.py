import serial

# Configure serial port
serial_port = serial.Serial('COM1', 9600, timeout=1)  # COM1, baudrate 9600, timeout 1s

# Check if the port is open
if serial_port.is_open:
    print(f"Serial port {serial_port.name} is open.")
else:
    print(f"Failed to open {serial_port.name}.")
    exit()

# Now you can read/write to serial_port
# Example: Read data
data = serial_port.readline()
print(f"Received: {data.decode()}")

# Example: Write data
serial_port.write(b'Hello serial port!\n')

# Close the serial port when done
serial_port.close()
