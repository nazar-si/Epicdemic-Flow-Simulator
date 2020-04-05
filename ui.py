import numpy as np
import pygame as pg
from pygame import gfxdraw as gfx

# Cool colors
blue = np.array([0, 132, 255])
yellow = np.array([255, 255, 0])
gray = np.array([96, 96, 96])
red = np.array([245, 90, 75])
white = np.array([204, 204, 204])
flat = np.array([33, 35, 37])
ltflat = np.array([40, 42, 44])

# Initialisation
def init(fps):
    global root, run_application, clock, update, FPS, panel # Save all variables
    FPS = float(fps) # Save initial FPS
    pg.init() # Create window

    root = pg.display.set_mode((1600, 900)) # Setting up
    pg.display.set_caption("SIR-model")     # the window

    run_application = True # Is application is still running
    clock = pg.time.Clock() # Main clock

    panel = (1280, 0, 320, 900) # Position of UI panel
    def update():
        global run_application

        for event in pg.event.get():    # Exit
            if event.type == pg.QUIT:   # event
                run_application = False # processing

        pg.display.update() # Update all drawings
        clock.tick(FPS) # Make frame step by frame rate
        root.fill(flat) # Clear all drawings for future ones
        pg.draw.rect(root, ltflat, panel) # Draw ui panel background

        z = clock.get_fps()               # Return relative
        return FPS / z if z != 0 else 1.0 # frame time

color = white # Set drawings color

######################### Draw functions ############################
def circle(x, y, r):
    x, y, r = int(x), int(y), int(r)
    gfx.filled_ellipse(root, x, y, r, r, color)
    gfx.aacircle(root, x, y, r, color)


def line(x1, y1, x2, y2):
    x1, y1, x2, y2 = np.array([x1, y1, x2, y2], dtype = "int32")
    gfx.line(root, x1, y1, x2, y2, color)

def linew(x1, y1, x2, y2):
    x1, y1, x2, y2 = np.array([x1, y1, x2, y2], dtype = "int32")
    gfx.line(root, x1 + 1, y1, x2 + 1, y2, color)
    gfx.line(root, x1, y1 - 1, x2, y2 - 1, color)

def rect(x, y, w, h):
    pg.draw.rect(root, color, np.array([x, y, w, h], dtype = "int32"))
###### P.S. these functions definetly better than original ones ######
