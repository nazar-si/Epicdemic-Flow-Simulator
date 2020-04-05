##################################
#  ______   ______   _   ______  #
# |        |         _  |      | #
# |______  |___      |  |_____/  #
# |        |         |  |        #
# |______  |         |  |        #
##################################
#.by TDXStudios

from opensimplex import OpenSimplex #basic lib for creatin simplex noise
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


########### Main loop #############
while ui.run_application:

    ####### Math #######
    pass



    ####### Draw #######
    pass



    ##### Main UI ######
    pass


    
    ###### Debug ######
    if debug_enabled:
        pass #some debug code here



    ###### Update ######
    delta = ui.update() #this function updates screen and returns relative delta time





## exit ##
## |  | ##
##\|/\|/##
pg.quit()#
##########
