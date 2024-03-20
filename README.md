# ME405-Term-Project

Our term project this quarter entails constructing a submersible chamber capable of reaching
specified depths. The system will operate in a closed loop, maintaining control until it 
reaches a desired pressure depth.

This project was intended for our senior project where. Dr. Ghalamchi wants to improve previous tests on waterproof drones that can take off from underwater to allow for a drone that can float on top of the water surface as well as have added support to be pushed up from underwater. The new design needs to be detachable from the built waterproof drone to compare its new features in tests. The propellers must also be above the water surface when the drone is idling on the water so that the efficiency of takeoff can be compared to the drone without the chamber in which the whole drone is submerged underwater upon takeoff.

Our project for ME 405 will be the system attached to this drone, enabling the drone to submerge underwater with a minimum depth of 5ft. While allowing for the system to resurface and position the propellers above the water's surface. 

Pressure can be directly correlated to depth, given a liquid's density.
   In order to simulate this system for our ME 405 Term Project, this system takes a desired pressure setpoint and controls a motor-driven syringe system to
   pressurize a chamber to the setpoint. It waits a period of time, as if it were underwater collecting data,
   and then returns to the initial pressure, as if it were returning to the water surface. 

## Hardware design
In Figure 1, we can see the internal system of the system. We have integrated Ametck Pittman's PG6712A077-R3 motor to a 50 CC syringe. Utilizing this motor, we've have attached a worm gear and gears to ensure sufficient torque to be generated. These gears are attached to a pinion
and aligned with a rack that allows for the syringe to be moved back and forth. This allows
for the system to achieve the desired weight to submerge the whole system.

While sizing and choosing the number of teeth we would need for our system. We calculated the following results.

$F_r = T_A / R_A$

$T_A = F_R * R_A$

$T_B = T_A$

$T_C = (N_C / N_B ) * T_B$

$T_C = (N_C / N_B ) * (F_R * R_A)$

$T_C = (1/15) * (6 N) * (.0152 m)$

$T_C = (0.006 Nm) = (6 mNm)$ 

Doing these calculations led us to select appropriate gears for our system, ensuring that they can withstand the pressure encountered during operation while maintaining an ideal speed.

![pic 3](https://github.com/alialauren1/ME405-Term-Project/assets/157066050/dabea663-33ab-48a3-91b7-2d57c6a7cb01)

Figure 1. CAD: Internal system of our terms project with labels indicating parts of the system.

![PIC 4](https://github.com/alialauren1/ME405-Term-Project/assets/157066050/eb48edbe-51e1-428f-be92-7078a6765a94)

Figure 2. CAD: Secondary view of the internal system of our terms project with labels indicating parts of the system.

![IMG_6039](https://github.com/alialauren1/ME405-Term-Project/assets/157066441/fc4674fa-24fd-468d-8175-b390c374cd86)

![Screenshot 2024-03-19 at 6 15 07 PM](https://github.com/alialauren1/ME405-Term-Project/assets/157066441/7a1a9980-e30d-4ffa-95b8-1a75b6fceadd)


Figure 3. Gears, motor, and frame for the internal system.

![IMG_6037](https://github.com/alialauren1/ME405-Term-Project/assets/157066441/d11b0a8d-c261-4473-9286-de9a2c53cbf4)

Figure 4. Hardware all connected

## Software design
To measure pressure, we used a Honeywell Board Mount Pressure Sensor, which uses I^2C communication. 

Attaching the sensor and the Ametek motor to our Nucleo, we were able to program both components to get a functioning product.

## Testing and Results

### Preliminary
Our senior project requires our chamber to be able to acheive at minimum, 5 ft depth. Calculations were run to determine the pressure that coincides with a depth of 5 ft in water. Being a little under 16.5 psi, we decided to run initial tests at 16.5 psi. 

In order to test our project sensors and motor control, we ran multiple tests in order to find our optimal Kp value. The results are presented in the plot down below. This was preliminary testing. 

<img width="605" alt="Screenshot 2024-03-17 at 10 32 32 PM" src="https://github.com/alialauren1/ME405-Term-Project/assets/157066441/ac451cf5-9cc9-4dc5-884a-5c23263242ac">

Figure 5. Plot of Pressure vs Time inside the syringe. Each line represents a different run of data collected while altering the Kp value.

During our testing, we initially set Kp to 5 (shown in blue) and then increased it to 10 (shown in orange). Observing the graph, it's evident that increasing the Kp value led to faster attainment of the target pressure of 16.5 [psi].

While testing to achieve for efficiency in reaching the desired pressure, it's essential to consider what our system will be attached to. Our system with the syringe and pressure sensor will be attached to a drone. Rapid pressure and volume changes may introduce a moment within the drone body, causing the drone to loose control. Therefore, we must weigh the trade-offs between achieving rapid pressure targets and maintaining system stability.

As we continue to test our project, further tests will be necessary to determine the optimal balance between speed, the system stability and accuracy. This process may involve fine-tuning parameters beyond just changing the Kp. This may incude making the chamber of the system bigger and other factors.

### Lab Demo
The below plot shows the pressure inside the syringe. The autonomous journey is one in which the system reaches the desired setpoint, waits for a duration, and then returns to the initial pressure. This journey mimics future developement of our larger senior project in which this pressure chamber will be attached to a drone. We anticipate it will be beneficial for some remote or signal to send a desired depth as the setpoint to the system, in which the chamber will submerge with the drone, going to that depth. It will remain there, possible to collect data, and then autonomously return to the surface. 

<img width="360" alt="image" src="https://github.com/alialauren1/ME405-Term-Project/assets/157066441/75d0b395-c743-4855-a188-f06f3c17799e">

Figure 6. Plot of Pressure vs Time inside the syringe with a setpoint of 17 [psi]. 

## What we have learned
### 3D Printing
While 3D printing gears and housing system for our project we learned that tolerances while creating parts is harder to achieve. When 3D printing the gears it was harder to align the gears causing the small gears to slip and not allowing for our system to be as efficient as it can be.
Note: We are saving our used PLA parts to find a place to recycle them. 

![IMG_6034](https://github.com/alialauren1/ME405-Term-Project/assets/157066441/5b03ef0f-60c7-414f-b9d5-46a70c6df5b4)

![Screenshot 2024-03-19 at 6 14 47 PM](https://github.com/alialauren1/ME405-Term-Project/assets/157066441/54fc154a-4143-4713-95bc-231fa4f20410)

Figure 7. Collection of gears tested

### Software and Sensors
We learned that the data being output from our pressure sensor was in counts. This led to the creation of a definition in our PressureSensor class to interpret the counts into a unit of measurement that could be easily interpretted, that being [psi]. Since our Closed-Loop Controller class uses the pressure sensor output in counts to correct for a desired pressure, an additional definition was made to interpret user desired setpoint input from [psi] to counts. 

While designing this system we learned how important it is to design and test early. Although most of the system was done with a reasonable amount of time. We keep running into issues causing the system to take longer to complete.

## Safety
Our project prioritizes user safety through thoughtful design considerations. By utilizing small gears, we have effectively reduced the risk of injuries to the user. Once the system has been fully assembled, all moving components and electrical elements will be enclosed and inaccessible to the user. This design ensures that users are protected from potential hazards during the system's operation.

## Additional files

Pressure sensor datasheet:
[SSCMANV030PA2A3 Honeywell.pdf](https://github.com/alialauren1/ME405-Term-Project/files/14630972/SSCMANV030PA2A3.Honeywell.pdf)

I2C Communications with Honeywell Pressure Sensors:
[sps-siot-i2c-comms-digital-output-pressure-sensors-tn-008201-3-en-ciid-45841.pdf](https://github.com/alialauren1/ME405-Term-Project/files/14630975/sps-siot-i2c-comms-digital-output-pressure-sensors-tn-008201-3-en-ciid-45841.pdf)

Below shows a table of parameters.  

|           **Parameters**           |   Variable   |   Value   |   Units   |
|:----------------------------------:|:------------:|:---------:|:---------:|
|    **----Rack+Piston+Syringe--**   |  **-------** |  **----** |  **----** |
| Force to overcome friction in tube |      F_R     |     6     |     N     |
|           **----Gears--**          |  **-------** | **-----** | **-----** |
|            Radius Gear A           |      R_A     |   0.0152  |     m     |
|            Teeth Gear A            |      N_A     |     17    |           |
|     Outer Diameter Worm Gear B     |     OD_B     |     16    |     mm    |
|          Teeth Worm Gear B         |      N_B     |     15    |           |
|     Pressure Angle Worm Gear B     |     Phi_C    |     20    |  degrees  |
|        Outer Diameter Worm C       |     OD_C     |     12    |     mm    |
|        Pressure Angle Worm C       |     Phi_C    |     20    |  degrees  |
|            Teeth Worm C            |      N_C     |     1     |           |
|   **-----Motor Parameters------**  | **--------** | **-----** |  **----** |
|        Radius of Motor Gear        |      rm      |  0.00662  |     m     |
|        Motor Nominal Voltage       |     V_DC     |     12    |     V     |
