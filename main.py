##################################
#  ______   ______   _   ______  #
# |        |         _  |      | #
# |______  |___      |  |_____/  #
# |        |         |  |        #
# |______  |         |  |        #
##################################
#.by TDXStudios

from opensimplex import OpenSimplex #basic lib for creatin simplex noise
from scipy.spatial import KDTree #data structure for agent position anlys
import pygame as pg #pygame module for basic visuals and controls
import numpy as np #library of improved array system
import random
import math
import ui
from agent import * #agent class
from area import * #area class

### We want to create different scenario ###
import scenario.distancing as s_d #adds new behaviour of social distancing
import scenario.quarantine as s_q #adds quarantine
import scenario.transport as s_t #adds transport scenarios and transport ways
import scenario.goverment as s_p #adds goverment behaviour(police, solders)
import scenario.isolation as s_i #adds behaviour of self-isolation
import scenario.mutation as s_m #adds virus strains and changes it's propeties
import scenario.society as s_s #adds other social behaviour
import scenario.remedy as s_r #adds ability to heal and create medecine
import scenario.zombe as s_z #adds functions for dead agents

### We want create different tools ###
import tools.graph #adds aditional graph informaiton and analisys
import tools.save #helps saving your simulation data
import tools.seed #adds infecting functions
import tools.dnd#adds ability to move agents and areas in real time

########## Actual Code ############
#=================================#
###################################
#--
########## Start setup ############

### Window initialisation ###
ui.init(60) #60 frames per second
### Noise  initialisation ###
noise = OpenSimplex() #we using noise but in future we might use random baiser curve path generation instead
debug_enabled = False

####### Some preparations #########


for i in range(100):
    dot = ui.dot(random.randint(396, 1180), random.randint(100, 800))
    dot.main_color = [ui.violet, ui.green, ui.blue, ui.yellow, ui.red, ui.orange][random.randint(0, 5)]
for i in range(35):
    dot = ui.dot(random.randint(100, 396), random.randint(374, 800))
    dot.main_color = [ui.violet, ui.green, ui.blue, ui.yellow, ui.red, ui.orange][random.randint(0, 5)]
for i in range(10):
    for j in range(10):
        ui.box(1300 + 25 * i, 100 + 25 * j)
for j in range(3):
    slider = ui.slider(1300, 32 + j * 16, 256)
    slider.set(random.random())
    if j == 1:
        slider.main_color = ui.white
for i in range(10):
    slider = ui.sliderint(1300, 384 + 16 * i, 256, i + 1)
    slider.set(random.randint(0, i + 1))

dots = []
for i in range(5):
    dot = ui.connect(1300, 596 + 32 * i, i == 2)
    dot.exclude_arr(dots)
    dots.append(dot)

dots1 = []
for i in range(7):
    dot = ui.connect(1556, 564 + 32 * i, i == 3 or i == 1 or i == 5)
    dot.exclude_arr(dots1)
    dots1.append(dot)

for i in range(5):
    j = random.randint(0, len(dots1) - 1)
    dots[i].connect(dots1[j])

ui.button(1440, 868, 256, "update")
ui.text_const(1296, 16, 16, "Parametrs")
ui.text_const(1296, 76, 16, "Boolean matrix")

f = lambda x, a, s, r: r * math.pow(math.e, - math.pi * math.pow(abs(2 * x) / s, a))
graph = ui.graph((100, 100, 256, 192), (-3, -0.1, 6, 1.2), f, 1, 1, 1)
graph.border = ui.dkflat
graph.step = 1
slider1 = ui.slider(100, 320, 256)
slider2 = ui.slider(100, 336, 256)
slider3 = ui.slider(100, 352, 256)
slider3.set(0.3)
slider1.set(0.5)
slider2.set(0.3)
########### Main loop #############
while ui.run_application:

    ###### Update ######
    delta = ui.update() #this function updates screen and returns relative delta time

    ###### Logic #######
    graph.args = [slider1.get() * 4.5 + 0.5, slider2.get() * 3 + 0.5, slider3.get()]

    ####### Draw #######
    pass



    ##### Main UI ######
    pass



    ###### Debug ######
    if debug_enabled:
        pass #some debug code here







## exit ##
## |  | ##
##\|/\|/##
pg.quit()#
##########
