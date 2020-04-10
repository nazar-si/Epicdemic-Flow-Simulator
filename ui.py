####### This is just hard and messy code which isn't connected with main theme of this projet #######
########################## Here i just draw different stuff on the screen ###########################
##################################### And define ui elements ########################################
#####################################################################################################
#===================================================================================================#
#####################################################################################################
import numpy as np
import pygame as pg
from pygame import gfxdraw as gfx

# Cool colors
blue = np.array([0, 132, 255])
yellow = np.array([255, 225, 0])
orange = np.array([250, 100, 0])
red = np.array([255, 50, 35])
green = np.array([50, 250, 100])
violet = np.array([96, 32, 250])

gray = np.array([96, 96, 96])
white = np.array([204, 204, 204])
flat = np.array([33, 35, 37])
dkflat = np.array([23, 25, 27])
ltflat = np.array([40, 42, 44])
ltgray = np.array([132, 135, 140])
wflat = np.array([200, 205, 210])

elements = []
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
        global run_application, mouse, press, release

        press = False; release = False             # Different
        for event in pg.event.get():               #
            if event.type == pg.QUIT:              #
                run_application = False            #
            elif event.type == pg.MOUSEBUTTONDOWN: # events
                if event.button == 1:              #
                    press = True                   #
            elif event.type == pg.MOUSEBUTTONUP:   #
                if event.button == 1:              #
                    release = True                 # processing

        mouse = np.array(pg.mouse.get_pos()) # get mouse coords

        for element in elements: # Update
            if element.enable:   # UI
                element.update() # elements

        pg.display.update() # Update all drawings
        clock.tick(FPS) # Make frame step by frame rate
        root.fill(flat) # Clear all drawings for future ones
        pg.draw.rect(root, ltflat, panel) # Draw ui panel background


        z = clock.get_fps()               # Return relative
        return FPS / z if z != 0 else 1.0 # frame time

color = white # Set drawings color
font_ref = pg.font.match_font('Robodo', 12)


######################### Draw functions ############################
def circle(x, y, r):
    x, y, r = int(x), int(y), int(r)
    gfx.filled_ellipse(root, x, y, r, r, np.array(color, dtype = "int32"))
    gfx.aacircle(root, x, y, r, np.array(color, dtype = "int32"))


def line(x1, y1, x2, y2):
    x1, y1, x2, y2 = np.array([x1, y1, x2, y2], dtype = "int32")
    gfx.line(root, x1, y1, x2, y2, np.array(color, dtype = "int32"))

def linew(x1, y1, x2, y2):
    x1, y1, x2, y2 = np.array([x1, y1, x2, y2], dtype = "int32")
    gfx.line(root, x1 + 1, y1, x2 + 1, y2, np.array(color, dtype = "int32"))
    gfx.line(root, x1, y1 - 1, x2, y2 - 1, np.array(color, dtype = "int32"))

def rect(x, y, w, h):
    pg.draw.rect(root, np.array(color, dtype = "int32"), np.array([x, y, w, h], dtype = "int32"))

def draw_text(text, x, y, size):
    global color
    font = pg.font.Font(font_ref, size)
    text_surf = font.render(text, True, color)
    text_frame = text_surf.get_rect()
    text_frame.center = (x, y)
    root.blit(text_surf, text_frame)

def draw_text_angle(text, x, y, size):
    global color
    font = pg.font.Font(font_ref, size)
    text_surf = font.render(text, True, color)
    text_frame = text_surf.get_rect()
    text_frame.topleft = (x, y)
    root.blit(text_surf, text_frame)

def draw_text_oangle(text, x, y, size):
    global color
    font = pg.font.Font(font_ref, size)
    text_surf = font.render(text, True, color)
    text_frame = text_surf.get_rect()
    text_frame.topright = (x, y)
    root.blit(text_surf, text_frame)
###### P.S. these functions definetly better than original ones ######

####### UI elements #######
class element:
    locked = False
    main_color = blue
    enable = True
    def __init__(self):
        self.enbled = True
        self.locked = False
        elements.append(self)

class dot(element):
    def __init__(self, x, y, add_to_update = True):
        self.x = x
        self.y = y
        self.state = 0
        self.enable = True
        self.color = np.array(ltgray, dtype = "float64")
        if add_to_update:
            elements.append(self)

    def update(self, separate_draw = False):

        if not self.locked:
            if np.sum(np.power(mouse - np.array([self.x, self.y]), 2)) <= 36:
                if press:
                    self.state = 2
                elif self.state != 2 or release:
                    self.state = 1
            else:
                if self.state != 2 or release:
                    self.state = 0

            if self.state == 2:
                dif = (mouse - np.array([self.x, self.y])) * 0.1
                if abs(dif[0]) >= 0.01:
                    self.x += dif[0]
                else:
                    self.x = mouse[0]

                if abs(dif[1]) >= 0.01:
                    self.y += dif[1]
                else:
                    self.y = mouse[1]

        if not separate_draw:
            self.draw()

    def draw(self):
        global color
        r = 4
        if not self.locked:
            if self.state == 0:
                self.color += (ltgray - self.color) * 0.1

            elif self.state == 1:
                self.color += (wflat - self.color) * 0.1
                color = self.color
                r = 5

            elif self.state == 2:
                self.color += (white - self.color) * 0.1
                color = self.main_color
                circle(self.x, self.y, 7)

        else:
            self.state = 0
            self.color += (gray - self.color) * 0.1
            color = ltgray
            circle(self.x, self.y, 7)

        color = self.color
        circle(self.x, self.y, r)

class slider(element):
    def __init__(self, x, y, width):
        self.x = x
        self.y = y
        self.width = width
        self.dot = dot(x, y, False)
        self.enable = True
        elements.append(self)

    def update(self):
        global color

        self.dot.main_color = self.main_color
        pg.draw.line(root, dkflat, [self.x, self.y], [self.x + self.width, self.y], 5)
        pg.draw.line(root, self.main_color, [self.x, self.y], [self.dot.x, self.y], 5)

        color = self.main_color
        circle(self.x, self.y, 2)
        color = dkflat
        circle(self.x + self.width, self.y, 2)

        self.dot.update(True)

        dot.locked = self.locked

        self.dot.y = self.y
        self.dot.x = min(max(self.dot.x, self.x), self.x + self.width)

        self.dot.draw()

    def get(self):
        return (self.dot.x - self.x) / self.width

    def set(self, x):
        self.dot.x = self.width * x + self.x


class sliderint(element):
    def __init__(self, x, y, width, n):
        self.x = x
        self.y = y
        self.n = n
        self.width = width
        self.dot = dot(x, y, False)
        self.enable = True
        elements.append(self)

    def update(self):
        global color

        self.dot.main_color = self.main_color
        pg.draw.line(root, dkflat, [self.x, self.y], [self.x + self.width, self.y], 5)
        pg.draw.line(root, self.main_color, [self.x, self.y], [self.dot.x, self.y], 5)
        # color = dkflat
        # circle(self.x, self.y, 2)
        # circle(self.x + self.width, self.y, 2)
        color = wflat
        s = 3
        for i in range(self.n + 1):
            x = self.x + i * self.width / self.n
            if x >= self.dot.x:
                color = gray
                s = 2
            circle(x, self.y, s)

        self.dot.update(True)

        dot.locked = self.locked

        self.dot.y = self.y
        self.dot.x = min(max(self.dot.x, self.x), self.x + self.width)
        self.dot.x += (self.x + self.width * self.get() / self.n - self.dot.x) * 0.09

        self.dot.draw()

    def get(self):
        return round(self.n * (self.dot.x - self.x) / self.width)

    def set(self, x):
        self.dot.x = self.width * int(x) / self.n + self.x

    def nset(self, x):
        self.dot.x = self.x + (self.dot.x - self.x) * n / x
        self.n = x

class box(element):
    def __init__(self, x, y, state = False):
        self.x = x
        self.y = y
        self.state = state
        self.enable = True
        self.main_color = gray
        self.color = np.array(ltgray, dtype = "float64")
        elements.append(self)

    def update(self):
        global color
        color = ltgray
        x = self.x
        y = self.y
        circle(x - 5, y - 5, 3)
        circle(x - 5, y + 5, 3)
        circle(x + 5, y - 5, 3)
        circle(x + 5, y + 5, 3)
        rect(x - 5, y - 8, 10, 17)
        rect(x - 8, y - 5, 17, 10)

        focus = np.sum(np.power(mouse - np.array([self.x, self.y]), 2)) <= 81

        if self.locked:
            if self.state:
                self.color += (self.main_color * 0.4 + ltgray * 0.6 - self.color) * 0.2
            else:
                self.color += (ltgray - self.color) * 0.2
        else:
            # if focus and not self.state:
            #     self.color += (self.main_color * 0.3 + ltgray * 0.7 - self.color) * 0.2
            # elif focus and self.state:
            #     self.color += (self.main_color * 0.6 + ltgray * 0.4 - self.color) * 0.2
            # else:
            if self.state:
                self.color += (self.main_color - self.color) * 0.2
            else:
                self.color += (ltgray - self.color) * 0.2

            if focus and press:
                self.state = not self.state

        if (np.array(self.color, dtype = "int32") != ltgray).all():
            color = self.color
            circle(x - 3, y - 3, 2)
            circle(x - 3, y + 3, 2)
            circle(x + 3, y - 3, 2)
            circle(x + 3, y + 3, 2)
            rect(x - 3, y - 5, 5, 11)
            rect(x - 5, y - 3, 11, 5)

class radio_dot(element):
    def __init__(self, x, y, radio = None, name = ""):
        self.x = x
        self.y = y
        self.state = False
        self.enable = True
        self.name = name
        self.radio = radio
        self.color = np.array(ltgray, dtype = "float64")
        if not radio:
            elements.append(self)

    def update(self):
        global color
        color = ltgray
        circle(self.x, self.y, 8)

        focus = np.sum(np.power(mouse - np.array([self.x, self.y]), 2)) <= 121

        if self.locked:
            if self.state:
                self.color += (ltflat * 0.4 + ltgray * 0.6 - self.color) * 0.1
            else:
                self.color += (ltgray - self.color) * 0.1
        else:
            if focus and not self.state:
                self.color += (ltflat * 0.3 + ltgray * 0.7 - self.color) * 0.1
            elif focus and self.state:
                self.color += (ltflat * 0.6 + ltgray * 0.4 - self.color) * 0.1
            else:
                if self.state:
                    self.color += (ltflat - self.color) * 0.1
                else:
                    self.color += (ltgray - self.color) * 0.1

            if focus and press:
                if not self.radio:
                    self.state = not self.state
                else:
                    self.radio.set(self.name)

        if (np.array(self.color, dtype = "int32") != ltgray).all():
            color = self.color
            circle(self.x, self.y, 5)

class radio(element):
    def __init__(self):
        self.enable = True
        self.dots = []
        self.dic = {}
        elements.append(self)

    def add(self, name, x, y):
        self.dic[name] = len(self.dots)
        self.dots.append(radio_dot(x, y, self, name))
        if len(self.dots) == 1:
            self.dots[0].state = True

    def get(self, name):
        return self.dots[self.dic[name]].state

    def set(self, name):
        for rdot in self.dots:
            rdot.state = False
        self.dots[self.dic[name]].state = True

    def update(self):
        for rdot in self.dots:
            rdot.locked = self.locked
            rdot.update()

class button(element):
    def __init__(self, x, y, width, text):
        self.x = x
        self.y = y
        self.width = width
        self.text = text.upper()
        self.state = 0
        self.enable = True
        self.color = np.array(ltgray, dtype = "float64")
        elements.append(self)

    def update(self, separate_draw = False):

        if not self.locked:
            if mouse[0] == min(max(mouse[0], self.x - self.width / 2 - 18), self.x + self.width / 2 + 18)\
                    and mouse[1] == min(max(mouse[1], self.y - 18), self.y + 18):
                if press:
                    self.state = 2
                elif self.state != 2 or release:
                    self.state = 1
            else:
                if self.state != 2 or release:
                    self.state = 0


        if not separate_draw:
            self.draw()

    def draw(self):
        global color
        r = 16

        if not self.locked:
            if self.state == 0:
                self.color += (ltgray - self.color) * 0.1

            elif self.state == 1:
                self.color += (wflat - self.color) * 0.1

            elif self.state == 2:
                self.color += (white - self.color) * 0.1
                color = self.main_color
                circle(self.x - self.width / 2, self.y, r + 4)
                circle(self.x + self.width / 2, self.y, r + 4)
                pg.draw.line(root, color, [self.x - self.width / 2, self.y],\
                        [self.x + self.width / 2, self.y], 2 * (r + 4) + 1)

        else:
            self.state = 0
            self.color += (gray - self.color) * 0.1
            color = ltgray
            circle(self.x - self.width / 2, self.y, r + 4)
            circle(self.x + self.width / 2, self.y, r + 4)
            pg.draw.line(root, color, [self.x - self.width / 2, self.y],\
                    [self.x + self.width / 2, self.y], 2 * (r + 4) + 1)

        color = self.color
        circle(self.x - self.width / 2, self.y, r)
        circle(self.x + self.width / 2, self.y, r)
        pg.draw.line(root, color, [self.x - self.width / 2, self.y], [self.x + self.width / 2, self.y], 2 * r + 1)
        color = ltflat
        if self.state == 2:
            color = self.main_color
        draw_text(self.text, self.x, self.y, 24)

class connect(element):
    def __init__(self, x, y, multy = False):
        self.x = x
        self.y = y
        self.multy = multy
        self.pair = None
        self.w = 3
        self.pairs = []
        self.closed = []
        self.state = 0
        self.color = np.array(ltflat, dtype = "float64")
        elements.append(self)

    def exclude(self, object):
        if not object in self.closed and object != self:
            self.closed.append(object)
            object.closed.append(self)

    def exclude_arr(self, obj_arr):
        for object in obj_arr:
            self.exclude(object)

    def connect(self, object):
        if self.multy:
            if object in self.pairs:
                self.pairs.remove(object)
                if object.multy:
                    object.pairs.remove(self)
                else:
                    object.pair = None
            else:
                self.pairs.append(object)
                if object.multy:
                    object.pairs.append(self)
                else:
                    if object.pair:
                        if object.pair.multy:
                            object.pair.pairs.remove(object)
                        else:
                            object.pair.pair = None
                    object.pair = self
        else:
            if object == self.pair:
                self.pair = None
                if object.multy:
                    object.pairs.remove(self)
                else:
                    object.pair = None
            else:
                if self.pair:
                    if self.pair.multy:
                        self.pair.pairs.remove(self)
                    else:
                        self.pair.pair = None
                self.pair = object
                if object.multy:
                    object.pairs.append(self)
                else:
                    if object.pair:
                        if object.pair.multy:
                            object.pair.pairs.remove(object)
                        else:
                            object.pair.pair = None
                    object.pair = self

    def update(self):
        global color

        if not self.locked:
            if release and self.state == 2:
                for e in elements:
                    if type(e) is connect:
                        if e.state == 1:
                            self.connect(e)
            if np.sum(np.power(mouse - np.array([self.x, self.y]), 2)) <= (121 if self.multy else 81):
                if press:
                    self.state = 2
                    for object in self.closed:
                        object.locked = True

                elif self.state != 2 or release:
                    self.state = 1
                    for object in self.closed:
                        object.locked = False

            else:
                if self.state != 2 or release:
                    self.state = 0
                    for object in self.closed:
                        object.locked = False

        ## draw ##
        color = ltgray
        circle(self.x, self.y, 10 if self.multy else 8)
        if not self.locked:
            if self.state == 0:
                if (not self.multy) and self.pair or self.multy and len(self.pairs) > 0:
                    self.color += (self.main_color - self.color) * 0.1
                else:
                    self.color += (ltflat - self.color) * 0.1

            elif self.state == 1:
                self.color += (self.main_color * 0.3 + gray * 0.7 - self.color) * 0.1

            elif self.state == 2:
                self.color += (wflat - self.color) * 0.1
                pg.draw.line(root, wflat, [self.x, self.y], mouse, self.w)

        else:
            self.state = 0
            self.color += (ltgray - self.color) * 0.1

        ## Draw lines ##
        if self.multy:
            for pair in self.pairs:
                pg.draw.line(root, self.main_color, [self.x, self.y], [pair.x, pair.y], self.w)
        elif self.pair:
            pg.draw.line(root, self.main_color, [self.x, self.y], [self.pair.x, self.pair.y], self.w)

        color = self.color
        if self.multy:
            circle(self.x, self.y, 7)
            color = ltgray
            circle(self.x, self.y, 4)
        else:
            circle(self.x, self.y, 5)

class text_const(element):
    def __init__(self, x, y, size, text):
        self.text = text
        self.x = x
        self.y = y
        self.color = white
        self.size = size
        elements.append(self)

    def update(self):
        global color
        color = self.color
        draw_text_angle(self.text, self.x, self.y, self.size)

class text_const_mid(text_const):
    def update(self):
        global color
        color = self.color
        draw_text(self.text, self.x, self.y, self.size)

class graph(element):
    def __init__(self, shape, graph_shape, f, *args):
        self.shape = np.array(shape)
        self.gshape = np.array(graph_shape)
        self.f = f
        self.w = 2
        self.border = white
        self.surf = pg.Surface(shape[2:])
        self.step = 2
        self.args = args
        self.pargs = 0
        self.pshape = 0
        self.pgshape = 0
        elements.append(self)
    def update(self):
        global color
        self.surf.fill(dkflat)
        if self.pargs != self.args or (self.pgshape != self.gshape).any() or (self.pshape != self.shape).any():
            self.gr = np.array([int(self.shape[3] * (1 - (self.f(self.gshape[0] + self.gshape[2] * i / self.shape[2], *self.args) - self.gshape[1]) / self.gshape[3])) for i in range(0, self.shape[2], self.step) ])
            self.pargs = self.args
            self.pgshape = self.gshape
            self.pshape = self.shape
                # y = self.gshape[0] + self.gshape[2] * i / self.shape[2]
                # y = self.f(y, *self.args)
                # y = self.shape[3] * (1 - (y - self.gshape[1]) / self.gshape[3])
        for i in range(0, self.shape[2] - self.step, self.step):
            pg.draw.line(self.surf, self.main_color, [i, self.gr[int(i / self.step)] ], [i + self.step, self.gr[int(i / self.step) + 1] ], self.w)

        y = self.shape[3] * (1 + self.gshape[1] / self.gshape[3])
        x = - self.shape[2] * self.gshape[0] / self.gshape[3]
        pg.draw.line(self.surf, white, [x, 0], [x, self.shape[3]], 2)
        pg.draw.line(self.surf, white, [0, y], [self.shape[2], y], 2)
        root.blit(self.surf, (self.shape[:2]))
        color = white
        draw_text_angle(str(round(self.gshape[1] + self.gshape[3], 5)), self.shape[0] + self.shape[2] + 4, self.shape[1], 16)
        draw_text_angle(str(round(self.gshape[1], 5)), self.shape[0] + self.shape[2] + 4, self.shape[1] + self.shape[3] - 12, 16)
        draw_text_oangle(str(round(self.gshape[0] + self.gshape[2], 5)), self.shape[0] + self.shape[2], self.shape[1] - 12, 16)
        draw_text_angle(str(round(self.gshape[0], 5)), self.shape[0], self.shape[1] - 12, 16)


        pg.draw.rect(root, self.border, self.shape + np.array([-1, -1, 2, 2]), 2)
