import utime
import cqueue

class Controller:
    """
    This class represents a contoller for the system.
    
    Kp (float): The proportinal gain of the controller.
    set_point (float): Is the desired setpoint of the system.
    start (int): The initial time of when the controller starts.
    """
    
    def __init__(self, kp, set_point):
    """
    Inits the Controller object with the provided proportional gain and set points.
    
    Kp (float): The proportinal gain of the controller.
    set_point (float): Is the desired setpoint of the system.    
    """
         self.kp = float(kp)
         self.set_point = float(set_point)
         self.start = utime.ticks_ms()
         

    def run(self, measured_output):
    """
    Runs the controller and calculation for the actual values based by the measured output.
    
    measure_poutput (float): The measured output of the system.
    
    Returns:
        tuple: A tuple containing the actual value and time that has passed.
    """
        err = self.set_point - measured_output
        actuation = self.kp*err
        current_time = utime.ticks_ms()
        self.time_passed = utime.ticks_diff(current_time, self.start)
        return actuation, self.time_passed, measured_output
        
    def set_setpoint(self, desired_set_point):
        self.set_point = float(desired_set_point)
        
    def set_Kp(self, desired_Kp):
        self.kp = desired_Kp
        