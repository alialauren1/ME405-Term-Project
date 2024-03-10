import pyb
import utime
import struct

class PressureSensor:
    
    def __init__(self):
        self.byte_array = bytearray(7)
        
        # COLLECT FIRST P VALUE
        data = I2C_obj.recv(self.byte_array,0x28) # receive data from I2C, store in bytearray
        status = (data[0] & 0xC0) >> 6 # extract first byte, shift 6 positions and store
        print(f'{status=}') 
        self.init_p = data[1] | ((data[0] & 0x3F) << 8) # 16bit pressure val
        #pressure conversion
        P_MAX = 2  #[bar]
        P_MIN = 0  #[bar]
        O_MAX = 0.9 * pow(2,14) # Max output val from sensor 
        O_MIN = 0.1 * pow(2,14) # Max input val from sensor 
        self.init_pressure = ((self.init_p - O_MIN) * (P_MAX - P_MIN) / (O_MAX - O_MIN) + P_MIN)*14.5038 #[psi]

        
    def readPressure(self):
        
        data = I2C_obj.recv(self.byte_array,0x28) # receive data from I2C, store in bytearray

        status1 = '{0:08b}'.format(data[0]) # extract first byte 
        status2 = (data[0] & 0xC0) >> 6 # extract first byte, shift 6 positions and store
        #print(f'{status1=},{status2=}')
        
        #print('first p val',self.init_pressure)

        pressCounts = data[1] | ((data[0] & 0x3F) << 8) # 16bit pressure val
        tempCounts = ((data[3] & 0xE0) >> 5) | (data[2] << 3) # 12bit temp val
        
        #pressure conversion
        P_MAX = 2  #[bar]
        P_MIN = 0  #[bar]
        O_MAX = 0.9 * pow(2,14) # Max output val from sensor 
        O_MIN = 0.1 * pow(2,14) # Max input val from sensor 
        self.pressure = ((pressCounts - O_MIN) * (P_MAX - P_MIN) / (O_MAX - O_MIN) + P_MIN)*14.5038 #[psi]
        self.p_gauge = self.pressure - self.init_pressure # pressure relative to atmosphere [psig]

        #temperature conversion
        T_MAX = 150  #[Celsius]
        T_MIN = -50  #[Celsius]
        T_COUNTS = pow(2,11) - 1
        self.temperature = (tempCounts * (T_MAX - T_MIN) / T_COUNTS + T_MIN)*(9/5)+32  #[Farenheight]
        
        return self.pressure,self.p_gauge,self.temperature
    
    def readDepth(self):
        
        gravity = 32.17405 # [ft/s^2]
        density = 62.3 # [lb/ft^3]
        
        depth = self.p_gauge*144*32.174/(gravity*density) # [ft]
        return depth
        
        
if __name__ == "__main__":
        
    # init
    I2C_obj = pyb.I2C(1,pyb.I2C.CONTROLLER,baudrate=100000)
    sensor_obj = PressureSensor()

    # scan I2C bus to make sure 1 device talking
    sensor_addr = I2C_obj.scan() # Check for devices on bus, output is I2C Device Address
    #Sensor_Addr = 0x28 # I2C Addr From Data Sheet
    
    while True:
        try:
            utime.sleep (0.5) # sleep 1 second
            Pressure, GaugePressure, Temp = sensor_obj.readPressure()
            print('Pressure [psi]= ',Pressure)
            print('Depth in [ft]= ',sensor_obj.readDepth())
            
        except KeyboardInterrupt:
            break
    