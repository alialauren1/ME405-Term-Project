# ME405-Term-Project

![Screenshot 2024-02-27 at 12 06 52 AM](https://github.com/alialauren1/ME405-Term-Project/assets/157066441/c3292629-7c7a-42ef-b7bf-8b73d2cc03e6)

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

### Open-Loop Response from Simulation

![Screenshot 2024-02-27 at 12 14 27 AM](https://github.com/alialauren1/ME405-Term-Project/assets/157066441/fb641230-9615-4e07-a996-a2f8f92ce283)

### Closed-Loop Response from Simulation 
Kp = 1000, Kd = 100
Desired Setpoint = 0.1 m [= approx. 4 inches]

![Screenshot 2024-02-27 at 12 15 31 AM](https://github.com/alialauren1/ME405-Term-Project/assets/157066441/470a8a85-c9bd-4e56-983b-ea06feaf428f)

