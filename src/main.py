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


def task1_fun(shares):
    """!
    Task which puts things into a share and a queue.
    @param shares A list holding the share and queue used by this task
    """
    # Get references to the share and queue which have been passed to this task
    my_share, my_queue = shares

    counter = 0
    while True:
        my_share.put(counter)
        my_queue.put(counter)
        counter += 1

        yield 0

def task2_fun(shares):
    """!
    Task which takes things out of a queue and share and displays them.
    @param shares A tuple of a share and queue from which this task gets data
    """
    # Get references to the share and queue which have been passed to this task
    the_share, shareTime, sharePos, the_queue = shares
    
    #reader_p_value = sharep.get()
    #PWM = sharePWM.get()
    #controller_obj2 = shareContObj.get()
    time = qTime.get()
    pos = qPos.get()
    
    sensor_obj = PressureSensor(0,0,0)
    
    state = 1
    S1_print = 1

    while True:
#         # Show everything currently in the queue and the value in the share
#         print(f"Share: {the_share.get ()}, Queue: ", end='')
#         while q0.any():
#             print(f"{the_queue.get ()} ", end='')
#         print('')

        
        if (state == S1_print): # Done with Controller, Print Vals
             
            print('TIME')
            #while time.any():
            print(time)
            print('RAW P')
            #while pos.any():
            pos_raw = (pos)
            pressure, pressure_diff, depth, init_p  = sensor_obj.RawtoData_P(pos_raw)
            print(pressure)
            #state = 2
        else:
            pass
            
            yield 0
            
        
def task3_fun(shares):
    qTime, qPos = shares[1], shares[2]
    
    enc2 = Encoder("enc2", pyb.Pin.board.PB6, pyb.Pin.board.PB7, 4)
    moe2 = motordriver (pyb.Pin.board.PA10, pyb.Pin.board.PB4, pyb.Pin.board.PB5, 3)
    
    setpoint_p = 15.5
    sensor_obj = PressureSensor(setpoint_p,0,0)
    setpoint_raw = sensor_obj.PtoRawP(setpoint_p)

    enc2.zero()
    queue_size = 100
    # Paramters for the contoller
    Kp = 100 #float(input("Enter the proportional gain (Kp) =  "))
    controller_obj2 = Controller(Kp, setpoint_raw, queue_size)
    #shareContObj.put(controller_obj2)
     
    state = 1
    S1_data = 1
    S2_done = 2
    S3_goback = 3 # close loop controller with init pressure as setpoint
    S4_print = 4
    #queue_size1 = 100
    counter = 0
    
    # Loop over a set number of iterations
    #for i in range(queue_size):
    while True:
        
        if (state == S1_data): # Closed Loop Controller   

            reader_p_value, temp_val = sensor_obj.readP_Raw() #Reads Raw P value
            # sharep.put(reader_p_value)
            
            PWM, time_passed, measured_output = controller_obj2.run(reader_p_value)
            # sharePWM.put(int(PWM))
            moe2.set_duty_cycle(-PWM) #Ajust motor 2 postion
            # + makes vacuum, - makes ^ pressure
            counter += 1
            
            #print('Motor 2, Pin A1 & A0')
            print(f"{reader_p_value} {PWM}")
            #tup = controller_obj2.data()
            #time = tup[0] # THIS IS A QUEUE
            qTime.put(time_passed)
            #print(time)
            #pos = tup[1] # THIS IS A QUEUE
            qPos.put(measured_output)
            
            if counter == queue_size:
                state = 2        
#             
        elif (state == S2_done): # Turn Off Motor Once Printed Data
            moe2.set_duty_cycle(0)
#             utime.sleep(5) # [5 seconds]
#             state = 3
#         
#         if (state == S3_goback): # Closed Loop Controller   
#             controller_obj2.set_setpoint(init_p)
#             reader_p_value_back, temp_val_back = sensor_obj.readP_Raw() #Reads Raw P value
#             PWM = controller_obj2.run(reader_p_value_back) 
#             moe2.set_duty_cycle(-PWM) #Ajust motor 2 postion
#             # + makes vacuum, - makes ^ pressure
#             counter += 1
#             
#             if counter == queue_size:
#                 #state = 3
#                 pass
#                 
       # if (state == S4_print):
          #  moe2.set_duty_cycle(0)
        else:
            pass  
        
        yield 0

# This code creates a share, a queue, and two tasks, then starts the tasks. The
# tasks run until somebody presses ENTER, at which time the scheduler stops and
# printouts show diagnostic information about the tasks, share, and queue.
if __name__ == "__main__":
    print("Testing ME405 stuff in cotask.py and task_share.py\r\n"
          "Press Ctrl-C to stop and show diagnostics.")
    
    #sharep = task_share.Share('h', thread_protect=False, name="Share p")
    #sharePWM = task_share.Share('h', thread_protect=False, name="Share PWM")
    #shareContObj = task_share.Share('h', thread_protect=False, name="Controller Object")
    #shareTime = task_share.Share('h', thread_protect=False, name="Time")
    #sharePos = task_share.Share('h', thread_protect=False, name="Pos")
    
    qTime = task_share.Queue('L', 16, thread_protect=False, overwrite=False,
                          name="Queue Time")
    qPos = task_share.Queue('L', 16, thread_protect=False, overwrite=False,
                          name="Queue Pos")
    
    # Create a share and a queue to test function and diagnostic printouts
    share0 = task_share.Share('h', thread_protect=False, name="Share 0")
    q0 = task_share.Queue('L', 16, thread_protect=False, overwrite=False,
                          name="Queue 0")

    # Create the tasks. If trace is enabled for any task, memory will be
    # allocated for state transition tracing, and the application will run out
    # of memory after a while and quit. Therefore, use tracing only for 
    # debugging and set trace to False when it's not needed
#    task1 = cotask.Task(task1_fun, name="Task_1", priority=1, period=400,
#                        profile=True, trace=False, shares=(share0, q0))
    task2 = cotask.Task(task2_fun, name="Task_2", priority=2, period=1500,
                        profile=True, trace=False, shares=(share0, qTime, qPos, q0))
    task3 = cotask.Task(task3_fun, name="Task_3", priority=3, period=60,
                        profile=True, trace=False, shares=(share0, qTime, qPos, q0))
    
    #cotask.task_list.append(task1)
    cotask.task_list.append(task2)
    cotask.task_list.append(task3)
    
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
