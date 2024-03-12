import pyb
import utime
import struct

class PressureSensor:
    
    def __init__(self,Setpoint,Data):
        
        
        self.I2C_obj = pyb.I2C(1,pyb.I2C.CONTROLLER,baudrate=100000)
        
         # scan I2C bus to make sure 1 device talking
        sensor_addr = self.I2C_obj.scan() # Check for devices on bus, output is I2C Device Address
        #Sensor_Addr = 0x28 # I2C Addr From Data Sheet
        
        self.byte_array = bytearray(7)
        
        # COLLECT FIRST P VALUE
        data = self.I2C_obj.recv(self.byte_array,0x28) # receive data from I2C, store in bytearray
        status = (data[0] & 0xC0) >> 6 # extract first byte, shift 6 positions and store
        print(f'{status=}') 
        self.init_p = data[1] | ((data[0] & 0x3F) << 8) # 16bit pressure val
        #pressure conversion
        P_MAX = 2  #[bar]
        P_MIN = 0  #[bar]
        O_MAX = 0.9 * pow(2,14) # Max output val from sensor 
        O_MIN = 0.1 * pow(2,14) # Max input val from sensor 
        self.init_pressure = ((self.init_p - O_MIN) * (P_MAX - P_MIN) / (O_MAX - O_MIN) + P_MIN)*14.5038 #[psi]

        
    def readP_Raw(self):
        
        # need to keep pressure values in raw counts to have max precision
        
        data = self.I2C_obj.recv(self.byte_array,0x28) # receive data from I2C, store in bytearray

        status1 = '{0:08b}'.format(data[0]) # extract first byte 
        status2 = (data[0] & 0xC0) >> 6 # extract first byte, shift 6 positions and store
        #print(f'{status1=},{status2=}')
        
        #print('first p val',self.init_pressure)

        self.pressCounts = data[1] | ((data[0] & 0x3F) << 8) # 16bit pressure val
        self.tempCounts = ((data[3] & 0xE0) >> 5) | (data[2] << 3) # 12bit temp val
        
        return self.pressCounts
    
    def PtoRawP(self,Setpoint):
        
        #pressure conversion from pressure [psi] to raw counts
        
        P_MAX = 2  #[bar]
        P_MIN = 0  #[bar]
        O_MAX = 0.9 * pow(2,14) # Max output val from sensor 
        O_MIN = 0.1 * pow(2,14) # Max input val from sensor
        setpoint_raw = ((Setpoint/14.5038)-P_MIN)*(O_MAX - O_MIN)/(P_MAX - P_MIN)+O_MIN
        return setpoint_raw
    
    def RawtoData(self):
        #pressure conversion from raw counts to pressure [psi]
        
        P_MAX = 2  #[bar]
        P_MIN = 0  #[bar]
        O_MAX = 0.9 * pow(2,14) # Max output val from sensor 
        O_MIN = 0.1 * pow(2,14) # Max input val from sensor 
        pressure = ((self.pressCounts - O_MIN) * (P_MAX - P_MIN) / (O_MAX - O_MIN) + P_MIN)*14.5038 #[psi]
        self.p_diff = pressure - self.init_pressure # pressure relative to atmosphere [psig]
        
        #temperature conversion
        T_MAX = 150  #[Celsius]
        T_MIN = -50  #[Celsius]
        T_COUNTS = pow(2,11) - 1
        self.temperature = (self.tempCounts * (T_MAX - T_MIN) / T_COUNTS + T_MIN)*(9/5)+32  #[Farenheight]

        return pressure, self.p_diff, self.temperature
        
    def ConvtoDepth(self):
        
        gravity = 32.17405 # [ft/s^2]
        density = 62.3 # [lb/ft^3]
        
        depth = self.p_diff*144*32.174/(gravity*density) # [ft]
        return depth
#
#         
#         #pressure conversion
#         P_MAX = 2  #[bar]
#         P_MIN = 0  #[bar]
#         O_MAX = 0.9 * pow(2,14) # Max output val from sensor 
#         O_MIN = 0.1 * pow(2,14) # Max input val from sensor 
#         pressure = ((self.pressCounts - O_MIN) * (P_MAX - P_MIN) / (O_MAX - O_MIN) + P_MIN)*14.5038 #[psi]
#         p_gauge = pressure - self.init_pressure # pressure relative to atmosphere [psig]
# 
#         #temperature conversion
#         T_MAX = 150  #[Celsius]
#         T_MIN = -50  #[Celsius]
#         T_COUNTS = pow(2,11) - 1
#         self.temperature = (self.tempCounts * (T_MAX - T_MIN) / T_COUNTS + T_MIN)*(9/5)+32  #[Farenheight]
#         
#         #return self.pressure,self.p_gauge,self.temperature
#         
#         gravity = 32.17405 # [ft/s^2]
#         density = 62.3 # [lb/ft^3]
#         
#         depth = p_gauge*144*32.174/(gravity*density) # [ft]
#         return depth
#         
#         
if __name__ == "__main__":
        
    # init
    setpoint = 15
    sensor_obj = PressureSensor(0,0)

    while True:
        try:
            utime.sleep (0.5) # sleep 1 second
          
            rawP_val = sensor_obj.readP_Raw()
            pressure, pressure_diff, temp = sensor_obj.RawtoData()
            
            print('--------------------')
            print(f'{setpoint=}')
            print('Raw Setpoint =',sensor_obj.PtoRawP(setpoint))
            print('---')
            print('Raw P Val = ',rawP_val)
            print(f'{pressure=} ')
            print(f'{pressure_diff=} ')
            #print(f'{temp=} ')
            print('Depth =',sensor_obj.ConvtoDepth())
           
           
        except KeyboardInterrupt:
            break
    