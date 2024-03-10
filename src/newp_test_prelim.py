import pyb
import utime
import struct

# init
I2C_obj = pyb.I2C(1,pyb.I2C.CONTROLLER,baudrate=100000)

# scan I2C bus to make sure 1 device talking
sensor_addr = I2C_obj.scan() # Check for devices on bus, output is I2C Device Address
#Sensor_Addr = 0x28 # I2C Addr From Data Sheet

while True:
    try: 
    
        utime.sleep (0.5) # sleep 1 second
        
        byte_array = bytearray(7)
        data = I2C_obj.recv(byte_array,0x28) # receive data from I2C, store in bytearray

        status1 = '{0:08b}'.format(data[0]) # extract first byte 
        status2 = (data[0] & 0xC0) >> 6 # extract first byte, shift 6 positions and store
        print(f'{status1=},{status2=}') 

        pressCounts = data[1] | ((data[0] & 0x3F) << 8) # 16bit pressure val
        tempCounts = ((data[3] & 0xE0) >> 5) | (data[2] << 3) # 12bit temp val
        
        #pressure conversion
        P_MAX = 2  #[bar]
        P_MIN = 0  #[bar]
        O_MAX = 0.9 * pow(2,14) # Max output val from sensor 
        O_MIN = 0.1 * pow(2,14) # Max input val from sensor 
        pressure = ((pressCounts - O_MIN) * (P_MAX - P_MIN) / (O_MAX - O_MIN) + P_MIN)*14.5 #[psi]

        #temperature conversion
        T_MAX = 150  #[Celsius]
        T_MIN = -50  #[Celsius]
        T_COUNTS = pow(2,11) - 1
        temperature = (tempCounts * (T_MAX - T_MIN) / T_COUNTS + T_MIN)*(9/5)+32  #[F]
        
        print(f'{pressure=},{temperature=}')
        
    except KeyboardInterrupt:
        break
        

# #calculate depth
# GRAVITY = 9.80665  #[m/s2]
# WATER_DENSITY = 998  #fresh water at 20 Celsius [kg/m3]
# pressurePa = pressure * 100000  #[Pa]
# depth = pressurePa / (GRAVITY * WATER_DENSITY)  #[m]

#print(f'{depth=}')