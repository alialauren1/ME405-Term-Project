"""!
@file basic_tasks.py
    This file contains a demonstration program that runs some tasks, an
    inter-task shared variable, and a queue. The tasks don't really @b do
    anything; the example just shows how these elements are created and run.

@author JR Ridgely
@date   2021-Dec-15 JRR Created from the remains of previous example
@copyright (c) 2015-2021 by JR Ridgely and released under the GNU
    Public License, Version 2.
    
@Modifications Made By: Alia Wolken, Eduardo Santos, Andrew Jwaided
"""

import gc
import utime
import pyb
import cotask
import task_share
import Closed_Loop_Controller


from motor_driver import motordriver
from encoder_reader import Encoder
from Closed_Loop_Controller import Controller
from pressure_sensor import PressureSensor

def task1_print(shares):
# convert, and print data
    """!
    Task which takes things out of a queue and share and displays them.
    @param shares A tuple of a share and queue from which this task gets data
    """
    # Get references to the share and queue which have been passed to this task
    qTime, qPos, share_init_p = shares
        
    sensor_obj = PressureSensor(0,0,0)
    
    state = 1
    S1_print = 1

    while True:
        
        if (state == S1_print): # Done with Controller, Print Vals
            
            time = qTime.get()
            pos = qPos.get()
 
            #print('TIME')
            #print('RAW P')
            pos_raw = (pos)
            #print(f'{pos_raw=}')
            pressure, pressure_diff, depth, init_p  = sensor_obj.RawtoData_P(pos_raw)
            share_init_p.put(init_p)
            print(f'{time=},{pressure=}{init_p=}')
            
        else:
            pass
            
        yield 0
            
        
def task2_get(shares):
    # get data
    qTime, qPos, share_init_p = shares[0], shares[1], shares[2]
    
    enc2 = Encoder("enc2", pyb.Pin.board.PB6, pyb.Pin.board.PB7, 4)
    moe2 = motordriver (pyb.Pin.board.PA10, pyb.Pin.board.PB4, pyb.Pin.board.PB5, 3)
    
    setpoint_p = 15
    sensor_obj = PressureSensor(setpoint_p,0,0)
    setpoint_raw = sensor_obj.PtoRawP(setpoint_p)

    enc2.zero()
    
    # Paramters for the contoller
    Kp = 100 
    controller_obj2 = Controller(Kp, setpoint_raw)
    
    state = 1
    S1_data = 1
    S2_off = 2
    S3_goback = 3
    counter = 0
    key = 0

    
    while True:
        
        if (state == S1_data): # Closed Loop Controller
            initialP = share_init_p.get()
            reader_p_value, temp_val = sensor_obj.readP_Raw() # Reads Raw P & T values
            PWM, time_passed, measured_output = controller_obj2.run(reader_p_value)
            moe2.set_duty_cycle(-PWM) #Ajust motor 2 postion
            # + makes vacuum, - makes ^ pressure
            counter += 1

            print(f"{reader_p_value=} {PWM=} {time_passed=} {measured_output=}")
            qTime.put(time_passed)
            qPos.put(measured_output)
            
            if setpoint_raw-6 <= reader_p_value <= setpoint_raw+6:
                print('REACHED SETPOINTT!!')
    
                state = 2
                
        elif (state == S2_off):
            moe2.set_duty_cycle(0)
            #controller_obj2.set_setpoint(initialP)
#             controller_obj2 = Controller(Kp, initialP)
#             utime.sleep(5)
#             reader_p_value, temp_val = sensor_obj.readP_Raw() # Reads Raw P & T values
#             PWM, time_passed, measured_output = controller_obj2.run(reader_p_value)
#             moe2.set_duty_cycle(-PWM) #Ajust motor 2 postion
#             # + makes vacuum, - makes ^ pressure
#             counter += 1
# 
#             #print(f"{reader_p_value=} {PWM=} {time_passed=} {measured_output=}")
#             qTime.put(time_passed)
#             qPos.put(measured_output)
#             
#             if (initialP-10 <= reader_p_value <= initialP+10):
#                 print('ORIGINAL PRESSURE REACHED !!')
#                 moe2.set_duty_cycle(0)

                
      
        else:
            pass  
        yield 0

# This code creates a share, a queue, and two tasks, then starts the tasks. The
# tasks run until somebody presses ENTER, at which time the scheduler stops and
# printouts show diagnostic information about the tasks, share, and queue.
if __name__ == "__main__":
    print("Testing ME405 stuff in cotask.py and task_share.py\r\n"
          "Press Ctrl-C to stop and show diagnostics.")
    
    qTime = task_share.Queue('L', 100, thread_protect=False, overwrite=False,
                          name="Queue Time")
    qPos = task_share.Queue('L', 100, thread_protect=False, overwrite=False,
                          name="Queue Pos")
    init_p = task_share.Share('h', thread_protect=False, name="inititial pressure")
    
    # Create a share and a queue to test function and diagnostic printouts
    #share0 = task_share.Share('h', thread_protect=False, name="Share 0")
    #q0 = task_share.Queue('L', 16, thread_protect=False, overwrite=False,
    #                      name="Queue 0")

    # Create the tasks. If trace is enabled for any task, memory will be
    # allocated for state transition tracing, and the application will run out
    # of memory after a while and quit. Therefore, use tracing only for 
    # debugging and set trace to False when it's not needed
    task1 = cotask.Task(task1_print, name="Task_1", priority=1, period=50,
                        profile=True, trace=False, shares=(qTime, qPos, init_p))
    task2 = cotask.Task(task2_get, name="Task_2", priority=2, period=49,
                        profile=True, trace=False, shares=(qTime, qPos, init_p))
    
    # bug report in readme, only works when data task is running faster than printing task
    
    # Ex: motor controller, time constant half second => run 10 times faster
    
    cotask.task_list.append(task1)
    cotask.task_list.append(task2)
    
    # Run the memory garbage collector to ensure memory is as defragmented as
    # possible before the real-time scheduler is started
    gc.collect()

    # Run the scheduler with the chosen scheduling algorithm. Quit if ^C pressed
    while True:
        try:
            cotask.task_list.pri_sched()
        except KeyboardInterrupt:
            break

    # Print a table of task data and a table of shared information data
    print('\n' + str (cotask.task_list))
    print(task_share.show_all())
    #print(task1.get_trace())
    print('') 
