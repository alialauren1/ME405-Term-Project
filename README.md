# ME405-Term-Project

Our term project this quarter entails constructing a submersible tank capable of reaching
specified depths. The system will operate in a closed loop, maintaining control until it 
reaches the desired pressure depth.

This project was intended for our senior project where. Dr. Ghalamchi wants to improve previous tests on waterproof drones that can take off from underwater to allow for a drone that can float on top of the water surface as well as have added support to be pushed up from underwater. The new design needs to be detachable from the built waterproof drone to compare its new features in tests. The propellers must also be above the water surface when the drone is idling on the water so that the efficiency of takeoff can be compared to the drone without the chamber in which the whole drone is submerged underwater upon takeoff.

Our project for ME 405 will be the system attached to this drone, enabling the drone to submerge underwater with a maximum depth of 5ft. While allowing for the system to resurface and position the propellers above the water's surface. 

In order to simulate this system for our ME 405 Term Project. The system will allow the user to input a desired "depth". The system will run to achieve this setpoint and stay at this position for 5 seconds. Then the system will reset to its original position. The system will also have a maximum depth of 5ft. 

## Hardwear design
In Figure 1, we can see the internal system of the system. We have integrated Ametck Pittman's PG6712A077-R3 motor to a 50 CC syringe. Utilizing this motor, we've have attached a worm gear and gears to ensure sufficient torque to be generated. These gears are attached to a pinion
and aligned with a rack that allows for the syringe to be moved back and forth. This allows
for the system to achieve the desired weight to submerge the whole system.

While sizing and choosing the number of teeth we would need for our system. We calculated the following results.

$F_r = T_A / R_A$

$T_A = F_R * R_A$

$T_B = T_A$

$T_C = (N_C / N_B ) * T_B$

$    = (N_C / N_B ) * (F_R * R_A)$

   = (1/30) * (18) * (5x10^-3)

   = 0.003 N*m
   = 3 N*m$

Doing these calculations led us to select appropriate gears for our system, ensuring that they can withstand the pressure encountered during operation while maintaining an ideal speed.

![pic 3](https://github.com/alialauren1/ME405-Term-Project/assets/157066050/dabea663-33ab-48a3-91b7-2d57c6a7cb01)
Figure 1. Internal system of our terms project with labels indicating parts of the system.



![PIC 4](https://github.com/alialauren1/ME405-Term-Project/assets/157066050/eb48edbe-51e1-428f-be92-7078a6765a94)

Figure 2. Secondary view of the internal system of our terms project with labels indicating parts of the system.


## Software design
To measure pressure, we used a Honeywell Board Mount Pressure Sensor, which uses I^2C communication. The sensor transmits data in byte arrays. The first byte being status, next two being pressure, and following two being temperature. 

To calculate the pressure from the digital output, the pressure sensor transfer function shown below was used, provided from the manual, "I^2C Communications with Honeywell Digital Output Pressure". The equation was rearranged to solve for Pressure. 

<img width="326" alt="Screenshot 2024-03-17 at 9 38 54 PM" src="https://github.com/alialauren1/ME405-Term-Project/assets/157066441/e8322335-e550-4d0f-b144-daa90d571818">

Where,

<img width="349" alt="Screenshot 2024-03-17 at 9 40 21 PM" src="https://github.com/alialauren1/ME405-Term-Project/assets/157066441/437d8267-a8c5-4346-8fe1-e501ef4dec2b">


You can read more about our pressure sensor and its I^2C communication using the links included at the bottom of the readme. 

Attaching the sensor and the Ametck motor to our Nucleo, we were able to program both components to get a functioning product. 

## Test and Results
In order to test our project sensors and motor control. We ran multiple test in order to find our optimal Kp value. The results are presented in the plot down below.

![pic1_405](https://github.com/alialauren1/ME405-Term-Project/assets/157066050/a46d59bb-a24d-4553-81b0-75914381d4f0)

Figure 3. Is a funtion of atmosphefic pressure vs the duration of time. Each line represents data collected while altering the Kp value.

During our testing, we initially set Kp to 5 (shown in blue) and then increased it to 10 (shown in orange). Observing the graph, it's evident that increasing the Kp value led to faster attainment of the target atmospheric pressure of 16.5 atm.

While testing to achieve for efficiency in reaching the desired pressure. It's essential to consider what our system will be attached to. Which includes our sensor project drone. Where rapid pressure changes might introduce a moment within the drone body causing the drone to be uncontrollable. Therefore, we must weigh the trade-offs between achieving rapid pressure targets and maintaining system stability.

As we continue to test our project, further tests will be necessary to determine the optimal balance between speed, the system stability and accuracy. This process may involve fine-tuning parameters beyond just changing the Kp. This may incude making the chamber of the system bigger and other factors.

## What we have learned
While 3D printing gears and housing system for our project we learned that tolerances while creating parts is harder to achieve. When 3D printing the gears it was harder to align the gears causing the small gears to slip and not allowing for our system to be as efficient as it can be.

When reading the values off of our pressure sensor, we never knew that the data given to us wouldn't be read in atmospheric pressure and instead had its own reading. We then had to incorporate this into our code. So that when the user sends a depth that they would like the system to achieve it will then convert that input (in atm) and then convert it to a value that can be read off of the pressure sensor.

While designing this system we learned how important it is to design and test early. Although most of the system was done with a reasonable amount of time. We keep running into issues causing the system to take longer to complete.

## Safety
Our project prioritizes user safety through thoughtful design considerations. By utilizing small gears, we have effectively reduced the risk of injuries to the user. Once the system has been fully assembled, all moving components and electrical elements will be enclosed and inaccessible to the user. This design ensures that users are protected from potential hazards during the system's operation.

## Additional files

Pressure sensor datasheet:
[SSCMANV030PA2A3 Honeywell.pdf](https://github.com/alialauren1/ME405-Term-Project/files/14630972/SSCMANV030PA2A3.Honeywell.pdf)

I2C Communications with Honeywell Pressure Sensors:
[sps-siot-i2c-comms-digital-output-pressure-sensors-tn-008201-3-en-ciid-45841.pdf](https://github.com/alialauren1/ME405-Term-Project/files/14630975/sps-siot-i2c-comms-digital-output-pressure-sensors-tn-008201-3-en-ciid-45841.pdf)

Below shows a table of parameters.  

|          **Parameters**          |   Variable   |    Value   |   Units   |
|:--------------------------------:|:------------:|:----------:|:---------:|
| **----Rack+Piston Parameters--** |  **-------** |  **----**  |  **----** |
|Force to overcome friction in tube|      bl      |     10     |     N     |
|  **-----Motor Parameters------** | **--------** |  **-----** |  **----** |
|       Radius of Motor Gear       |      rm      |   0.00662  |     m     |
| Motor Nominal Voltage            |     V_DC     | 12         |     V     |

