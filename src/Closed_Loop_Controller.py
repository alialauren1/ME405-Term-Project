import utime
import cqueue

class Controller:
    """!
    This class represents a closed-loop contoller for the system. 
    @author Alia Wolken, Eduardo Santos, Andrew Jwaideh
    """
    
    def __init__(self, kp, set_point):
    """!
    Inits the Controller object with the provided proportional gain and set points.
    
    Kp (float): The proportinal gain of the controller.
    set_point (float): Is the desired setpoint of the system.
    start (int): The initial time of when the controller starts.
    """
         self.kp = float(kp)
         self.set_point = float(set_point)
         self.start = utime.ticks_ms()
         
    def run(self, measured_output):
    """!
    Runs the controller and calculation for the actual values based by the measured output.
    
    measured_output (float): The measured output of the system.
    
    Returns:
        tuple: A tuple containing the actual value and time that has passed.
    """
        err = self.set_point - measured_output # Calculates error 
        actuation = self.kp*err 
        current_time = utime.ticks_ms()
        self.time_passed = utime.ticks_diff(current_time, self.start)
        return actuation, self.time_passed, measured_output
        
    def set_setpoint(self, desired_set_point):
    """!
    Takes in a desired set point. 
    Sets new setpoint for class
    
    self.setpoint (float): The new setpoint
    """
        self.set_point = float(desired_set_point) # To set a new setpoint for class
        
    def set_Kp(self, desired_Kp):
    """!
    Takes in a desired Kp value. 
    Sets new Kp for class
    
    self.kp: The new kp value
    """
        self.kp = desired_Kp # To set a new kp for class
        