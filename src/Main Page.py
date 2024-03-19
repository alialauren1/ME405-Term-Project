"""! \mainpage Software

 * \section intro_sec Introduction
 * Below are the following three classes used to implement our main program.
 
 * \section p_sensor_sec Pressure Sensor Class
 * def __init__:
         Initialize the PressureSensor Object.
         Collect initial data values for status and initial pressure. 
 * def readP_Raw:
         Reads Raw Status, Pressure, and Temperature Data from Sensor
 * def PtoRawP:
         Converts setpoint pressure from units of psi to counts.
 * def RawtoData_P:
         Converts raw pressure data in units of counts to [psi].
         Then pressure difference from initial pressure and thus displacement depth
 * def RawtoData_T:
         Converts raw pressure data in units of counts to [Fahrenheit].
         
 * \section motor_driv_sec Motor Driver Class
 * def __init__:
         Creates a motor driver by initializing GPIO pins and turning off the motor for safety. 
 * def set_duty_cycle:
         This method sets the duty cycle to be sent to the motor to the given level.
         Positive values cause torque in one direction, negative values
         in the opposite direction.
         
 * \section CL_controller_sec Closed-Loop Controller Class
 * def __init__: Inits the Controller object with the provided proportional gain and set points.
 * def run: Runs the controller and calculation for the actual values based by the measured output.
 * def set_setpoint:
        Takes in a desired set point. 
        Sets new setpoint for class
 * def set_Kp:
        Takes in a desired Kp value.
        Sets new Kp for class
"""

 