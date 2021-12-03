# Gaming With Gestures:<br>Gesture Recognition Using Machine Learning <img src="https://drive.google.com/uc?export=view&id=10pEPAWtMe4R3jUYgyDQsqDI5LmS81gAT" width="25" height="25">
***
## Table of Contents
1. [Project Overview](#project-overview)
    * [Our Vision](#our-vision)
    * [Personas and Key Features](#personas-features)
2. [Hello World](#hello-world)
3. [Technologies](#technologies)
4. [New Releases](#new-releases)
    * [How to Download and Install New Release](#download-install-release)
    * [How to Run New Release](#run-release)
5. [Team Contributions](#team-contributions)
    * [Meet Our Team](#team)
    * [Contributions](#contributions)
6. [UML Diagrams](#uml-dia)
    * [Class Diagram](#class-dia)
    * [Sequence Diagram](#seq-dia)
7. [Resources](#resources)
    


***
<a name = "project-overview"></a>
## Project Overview 
Gestures are a natural way of communicating or clarifying ideas or intentions. This especially makes gestures a more user-friendly approach to gaming. Often when utilizing a controller, novice players are tasked with the initial learning curves of using buttons and joystick movements to perform successfully in a game. Furthermore, a controller can confine a player to more rigid and unnatural movements, resulting in the lack of immersion or gaming interaction. Considering this, the goal of this project is to enhance the gaming experience by detecting and recognizing gestures as the controls for gaming interaction. This is intended to be done using machine learning. Whether it is driving, dribbling, or performing a complex combination of hand seals, gestures can be an efficient and immersive way to interact with our favorite video games.

<a name = "our-vision"></a>
### Our Vision
FOR members of the gamming community WHO desires a more intuititive and immersive gaming experience without extra hardware and cost. THE Gaming with Gestures Project is a application THAT provides hand tracking, static gesture-based game controls, and dynamic gesture-based game controls. UNLIKE other hardware-based games or immersive gaming software, OUR product provides immersive gamming without the use of unique hardware, making it a more cost efficient and user friendly option.

<a name = "personas-features"></a>
### Personas and Key Features
#### [Shakirah Cooper](https://github.com/ArchaePi) | Rebecca Black, A high school student at Villa Park High School
Rebecca, age 15, is a high school student studying at Villa Park High School in Villa Park, California. She has recently been accepted to the dance team at her school. During her first few practices, she has had a hard time keeping up with the moves. In fear of being kicked off the team for not showing improvement, Rebecca wants to make more time at home to practice so that she can perform the moves correctly and in time. She is aware of different gaming options she can explore to practice dancing, however she has an especially tight budget, and little time to learn new devices as she is not particularly tech savvy.

Rebecca, has taken interest in the Gaming with Gestures application because she understands that it is going to allow her the ability to still play popular dancing games, but without the high price or the hardware learning curve. Because of the Gaming with Gestures functionality to recognize dynamic gestures, Rebecca will be able to play her favorite dancing games and have her physical movements picked up and registered as game controls.

#### [Phi Truong](https://github.com/PT141) | Jerry Dinkleburg, A father in New York City, New York
Jerry used to play video games when he was younger. However, life circumstances led to him dropping off of videogames. Now that his life is stable, he now wishes to go back into the gaming sphere. He used to play on the Xbox 360, and one thing he remembers loving about it was the Xbox Kinect. He would love to find a way to recreate that experience in any sort of way. 

Jerry is rather average with technology. He has a laptop to do his work and spend his leisure time on. He is aware of setting up software and hardware to suit his needs from his gaming time earlier in his life. He would love if there was a software program that could imitate the full-body interactions of the Kinect, allowing the user to utilize their full body as a controller.

#### [Hasnat Hasib](https://github.com/HHasib) | James Conor, high school student
James is a 16 year old high school student. He is a science student and is currently studying for
his SAT. He hopes to join his local community college in Computer Science. He plans to become a
game developer in the future.

He is a great student and in his free time he
likes to play video games with his friends. He has a gaming pc that he uses to play his games with.
He does not only have a keyboard and a mouse to play his games with but also other controllers
such as a joystick, steering wheel and pedals, etc.

#### [Brandon Bolden](https://github.com/tui84176) | Emily, A mother of two in San Fransico, California
Emily is a 27 year old mother of one who lives in San Francisco, California. She was born in Oakland to parents who were partially deaf at a young age. While Emily isn’t deaf, individuals in her family are, including her son. She moved to San Francisco due to her husband’s job and currently works as an IoT Specialist from home while she takes care of her son. She obtained a degree in computer science, at the California Institute of Technology, to help achieve her dream job of working in the field of technology. With a husband and son, she looks forward to a life of happiness in her family.

As an IoT Specialist, Emily has already done work in the coding field. She has used multiple languages and ultimately prefers to use python. In relation to this project, Emily believes that she could use the hand recognition features to help her son and other deaf individuals learn sign language from home. She has an interest in this project because her son can try to practice signing out letters and maybe some words while she has her own job to attend to.

#### [Leomar Duran](https://github.com/lduran2) | Gustav, A doctoral student

Gustav is 22 years old. He is a doctoral student at Temple University, and currently mostly uss his computer to do resarch for his thesis. Gustav has always had a type of neurofibromatosis that results in limited mobility. Because of his motor accuracy issues, he would have difficulty using the mouse and keyboard.

However, Gustav can adapt Gaming with Gestures to work with the web browser to do thesis research, and he can even control a word processor using Gaming with Gestures. This takes advantage of the feature “Universal Compatibility and Flexibility”. Although the Gaming with Gestures project is marketed towards and tested on games, it is a universal control, and it can easily be adapted to any application.

***
<a name = "hello-world"></a>
## Finger Identifier [FID]
Finger Identifier (FID) is an application designed to identify which of the user's fingers are currently up. It is limited to identify either one finger at a time, or all fingers. Interest in developing FID arose from the larger project currently in development, Gaming with Gestures (GwG). GwG can ultilize FID's functionality to craft static gestures which can then be mapped to hardware controls for compatible video game software.

### Limitations
* Programmed exclusively for right hand use
* Only one finger or all fingers can be identified at a time. Therefore, if the user attempts to identify the both the index finger and the middle finger at the same time, there will be no single finger identified and displayed.

***
<a name = "technologies"></a>
## Technologies
* Anaconda Individual Edition

### Libraries
* Google's MediaPipe
* Keras
* Keyboard
* NumPy
* OpenCV on Wheels
* PyautoGUI
* Time
* Virtual Gamepad

***
<a name = "new-releases"></a>
## New Releases

<a name = "download-install-release"></a>
### How to Download and Install New Release
In order to download ScreenController, click on the latest ScreenController release on the side. From there, download ScreenController.exe and wait until it finishes downloading.

<a name = "run-release"></a>
### How to Run New Release
In order to run the executable, click on the file to run it. It should take a while to execute, but when it finishes there should be an indicator that the camera on your machine is turned on (such as a light next to the camera). When this appears, the program is finally running! For a quick tutorial, click <a href="https://drive.google.com/file/d/1tjsxGIvNLwNwHDA8qbJEQHZ0p0oB-F3X/view?usp=sharing">here</a>.

***
<a name = "team-contributions"></a>
## Team Contributions

<a name = "team"></a>
### Meet Our Team
#### Shakirah D. Cooper - Product Owner / Developer
#### Phi D. Truong - Scrum Master / Developer
#### Hasnat Hasib - Developer
#### Brandon Bolden - Developer
#### Leomar Duran - Developer

<a name = "contributions"></a>
### Contributions
Shakirah's contributions include...

Phi's contributions include...

Hasnat's contributions include...

Brandon's contributions include...

Leomar's contributions include...

1. [Week 1](./Week1.md)
2. [Week 2](./Week2.md)
3. [Week 3](./Week3.md)
4. [Week 4](./Week4.md) 

<a name = "uml-dia"></a>
## UML Diagrams

<a name = "class-dia"></a>
### Class Diagram v1
[![Version 1 of UML](https://github.com/CIS3296SoftwareDesignF21/prj-03-gaming-with-gestures/blob/ReadMe/Gestures.drawio.png)](https://github.com/CIS3296SoftwareDesignF21/prj-03-gaming-with-gestures/blob/ReadMe/Gestures.drawio.png)

### Class Diagram v2
[![Version 2 of UML](https://github.com/CIS3296SoftwareDesignF21/prj-03-gaming-with-gestures/blob/ReadMe/Gestures.UML.png)](https://github.com/CIS3296SoftwareDesignF21/prj-03-gaming-with-gestures/blob/ReadMe/Gestures.UML.pdf)

<a name = "seq-dia"></a>
### Sequence Diagram
The user (Gamer) presented within this diagram interacts soley with the Graphical User Interface (GUI). On the GUI, there will be options to start gesture control mode, change gesture, change controller, and stop gesture control mode. If the user selects to start gesture control mode, the camera will then be opened, and the loop of tracking will begin. If during tracking, a gesture is recognized, it will result in its corresponding control on the current controller. For example, if the current controller is a screen controller and the peace sign maps to a mouse click, then once a peace sign is recognized, a mouse click will be performed. Tracking simply continues until another gesture is recognized. The user also can change the gestures that map to specific controls via the GUI as well as change the controls provided by changing the controller also via the GUI. Finally, if the user selects to stop gesture control mode, then the camera will be turned off which will cease tracking and gesture recognition.

![GWG UML Sequence Diagram](https://raw.githubusercontent.com/CIS3296SoftwareDesignF21/prj-03-gaming-with-gestures/ReadMe/GWG_Sequence2.svg)

***

<a name = "resources"></a>
## Resources
https://google.github.io/mediapipe/solutions/hands.html </br>
https://github.com/google/mediapipe/   </br>
https://trello.com/b/ABXoxfJg/gaming-with-gestures-gesture-recognition-using-machine-learning   </br>
https://github.com/CIS3296SoftwareDesignF21/prj-03-gaming-with-gestures
***


