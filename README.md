# ME405-Term-Project

Our term project this quarter entails constructing a submersible tank capable of reaching
specified depths. The system will operate in a closed loop, maintaining control until it 
reaches the desired pressure depth.

This project was intended for our senior project where. Dr. Ghalamchi wants to improve previous tests on waterproof drones that can take off from underwater to allow for a drone that can float on top of the water surface as well as have added support to be pushed up from underwater. The new design needs to be detachable from the built waterproof drone to compare its new features in tests. The propellers must also be above the water surface when the drone is idling on the water so that the efficiency of takeoff can be compared to the drone without the chamber in which the whole drone is submerged underwater upon takeoff.

Our project for ME 405 will be the system attached to this drone, enabling the drone to submerge 
underwater and resurface to position the propellers above the water's surface.


## Hardwear design
In Figure 1, we can see the internal system of the system. We have integrated Ametck Pittman's PG6712A077-R3 motor to a 150 CC syringe. Utilizing this motor, we've have attached a worm gear and gears to ensure sufficient torque to be generated. These gears are attached to a pinion
and aligned with a rack that allows for the syringe to be moved back and forth. This allows
for the system to achieve the desired weight to submerge the whole system.

![pic 3](https://github.com/alialauren1/ME405-Term-Project/assets/157066050/dabea663-33ab-48a3-91b7-2d57c6a7cb01)
Figure 1. Internal system of our terms project with labels indicating parts of the system.


## Software design
To measure pressed we have used a Leadless SMT AN from Honeywell, which can output
I^2C. Attaching this sensor and the Ametck motor to our Nucleo, we were able to program both components to get a functioning product. You can read more about our software design by clicking the link down below:

## Test and Results

Below shows a table of the parameters. These are mostly approximations and will be adjusted accordingly as more accurate values are determined. 

|          **Parameters**          |   Variable   |    Value   |   Units   |
|:--------------------------------:|:------------:|:----------:|:---------:|
| **----Rack+Piston Parameters--** |  **-------** |  **----**  |  **----** |
|        Mass of Rack+Piston       |      mr      |     0.1    |     kg    |
|   Damping between Piston & Tube  |      bl      |     10     |   N-s/m   |
|  **-----Motor Parameters------** | **--------** |  **-----** |  **----** |
|       Radius of Motor Gear       |      rm      |   0.00662  |     m     |
|     Viscous Damping of Motor     |      bm      | 0.00000134 | N-m-s/rad |
|          Torque Constant         |      Kt      |    0.022   |   N-m/A   |
|         Back-emf Constant        |    Kv = Kt   |    0.022   |  V-s/rad  |
|        Terminal Resistance       |       R      |     4.3    |    ohm    |
| Terminal Inductance              | L            | 4.72e-3    | H         |
| Motor Nominal Voltage            | V_DC         | 12         | V         |

## What we have learned

## Additional files

Pressure sensor datasheet:
https://prod-edam.honeywell.com/content/dam/honeywell-edam/sps/siot/en-us/products/sensors/pressure-sensors/board-mount-pressure-sensors/basic-abp2-series/documents/sps-siot-abp2-series-datasheet-32350268-en.pdf?download=false


