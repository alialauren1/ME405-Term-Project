import pyb
import utime
import struct

def readPressureSensor():  
    # scan I2C bus to make sure 1 device talking
    sensor_addr = I2C_obj.scan() # Check for devices on bus, output is I2C Device Address
    return sensor_addr[0] #element num 0 to get out of list

if __name__ == '__main__':
    
    # init
    #Sensor_Addr = 0x28 # I2C Addr From Data Sheet
    
    I2C_obj = pyb.I2C(1,pyb.I2C.CONTROLLER,baudrate=100000)
    
    while True:
        utime.sleep (1) # sleep 1 second
        
        try:
            addr = readPressureSensor()

            byte_array = bytearray(7)
            # pull data
            data = I2C_obj.recv(byte_array,addr)
            
            # old 
            # pull status
            #data = I2C_obj.mem_read(7,addr,0x51)
            
            pass

        except KeyboardInterrupt:
            break


