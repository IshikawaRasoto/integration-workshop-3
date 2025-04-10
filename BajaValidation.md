# ECUT - ECU Tester 🚙

## Intro 🚜

![IMG_7520 CR2](https://github.com/user-attachments/assets/2d824bc4-d97e-435c-848b-64f49afb0f8a)

The university's Baja Team (Imperador) has a problem that the only way to test their eletronic system is with it installed in the vehicle. Therefore, it's necessary to develop an embedded system to test the hardware and firmware outside the car, in the most automatic way as possible.

## Proposal 📋

Following good practices from the automotive industry, we propose the development of an embedded system that will automatically do the tests of the different parameters acquired by the Baja team's ECU. It will generate all the measured parameters, let the user change it, and verify if the ECU is acquiring correctly all of the data.

![Imagem do WhatsApp de 2024-12-16 à(s) 11 26 18_944558cc](https://github.com/user-attachments/assets/0d2b4248-a0a9-4b65-997d-7421484309c5)

## Specifications ✔️

Imperador's ECU today acquires the following data of the vehicle:

- Battery Voltage

- Engine RPM

- CVT's Belt temperature

- Rear Axis's speed

- Front left semi-axis speed

- Front right semi-axis speed

With the collected parameters in mind, the proposal is to generate all of those parameters phiscally in a test bench in which the user will be able to install the ECU and test it.

![image](https://github.com/user-attachments/assets/84b8cfb3-95b7-4be6-99e5-4f0ed08d17df)


### Generating the parameters 📶

Each parameter will be generated by:

| Parameter | Generation |
| --- | --- |
| Battery Voltage | DAC |
| Rear Axis's speed | DC Motor and Phonic wheel |
| Engine RPM | DC Motor and Phonic wheel |
| Front left semi-axis speed | DC Motor and Phonic wheel |
| Front right semi-axis speed | DC Motor and Phonic wheel |
| CVT's Belt Temperature | Power resistor attatched to a piece of the CVT's belt|

### Paramters quality assurance 💯 

To assure the quality of the generated parameters, each one of the generations will have an retro feeding sensor. For example, the battery voltage simulated by a DAC will be coupled to an ADC of the tester which will measure the generated voltage. In the same way, we will couple a Thermocouple Type K to the Rubber belt to check the belt's temperature generated by the power resistor. And all of the speeds and RPM will be generated by motor, which we will measure their RPM with our own sensors.

### Automatic Test 📝

To verify the operation of the ECU, both systems will be connected through the troubleshooting USB port present on the ECU. All the data acquired by the ECU will be sent through this communication link, but also the tester will communicate with the ECU to notify about the start of a test.

#### Protocol 💬

The protocol will work as described below:

1. The Tester will notify the ECU about an upcoming test.
2. The ECU shall respond the Tester with an OK signal.
3. The ECU will send the measured data indefinetely.
4. The Tester will notificate the ECU with and END message.
5. The ECU will responde with OK.

The data packet will be sent as:

| TimeStamp | Battery Voltage | RPM | Rear axis' speed | Front left semi-axis' speed | Front right semi-axis' speed | CVT Temperature |

### User interface 📱

The tester will host a local Wi-Fi network that will serve as an interface to the user in their cellphone. In the web page a log will be generated with the messages received by the Tester, and in the end it will generate a report with the results of the test, comparing the generated signal with the ECU acquired data.

## Components 🔌

- 4x DC Motors

- 4x RPM sensors

- 2x DC Motor Drivers

- 1x ADC

- 1x Power resistor

- 1x Power PWM control unit

- 1x Thermocouple type K

- 1x ESP32

- 1x 12V Font

## BOM 💵

| Item | Quantity | Price (R$) |
| --- | --- | --- |
| DC Motor | 4 | 80,00 |
| RPM sensors | 4 | 100,00 |
| DC Motor Driver | 2 | 40.00 |
| ADC | 1 | 20,00 | 
| Power Resistor | 1 | 30,00 |
| Power PWM control unit | 1 | 35,00 |
| Thermocouple type K | 20,00 |
| ESP32 | 1 | 50,00 |
| 12V Font | 1 | 25,00 |
| Total | 400,00 |

