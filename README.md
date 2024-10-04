# MinecraftEye
Voxel Engine (like Minecraft) in Python and OpenGL that takes data from AIRIS and shows where it has explored and what it is thinking.

You need to edit the first part of the strings in lines 63, 64, and 65 in scene.py with your file directory that '/experiential-minecraft/examples/output/' is in

Run main.py after starting Minecraft. Once the agent starts moving, the world will automatically update. Press F to instantly move to where the agent currently is. Press F again to regain camera control.

# Controls: 

Move: W A S D

Fly up: E

Fly down: Q

Fly fast: Hold shift

Toggle Auto-Camera: F

Switch View Filter: M

Toggle X-Ray mode: X

Toggle "View All States" (Can get very laggy after a lot of exploring): B

Release cursor: Esc

Capture cursor: Enter

# View Description

Small Blue Cube: The agents current location

Large Blue Cube: The blocks that the agent can currently see

Red Arrows: Where the agent predicts it will go when performing a particular action, but is not confident

Black Arrows: Where the agent predicts it will go when performing a particular action, and is confident

Green Arrows: The predicted outcome of the action it is going to perform. Can be a chain that represents a sequence of planned actions.

Small White Cube: Locations the agent has been that it searched to create the current plan

Small Green Cube: Locations the agent is expecting to go as part of its plan

Large Green Cube: The area of blocks the agent is expecting to discover at the end of its plan

Small Black Cube (Only visible if "View All States" is on): Every location the agent has been

![minecraft](/screenshot/0.jpg)