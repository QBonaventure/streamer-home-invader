#!/usr/bin/python3

from rgb import RGB
from time import sleep

class StreamAnimation:

    def __init__(self, rgb):
        self.rgb = rgb

    def stopAll(self):
        self.rgb.stop(self.rgb.r)
        self.rgb.stop(self.rgb.g)
        self.rgb.stop(self.rgb.b)


    def followEvent(self):
        self.rgb.g.toRun(self.rgb.blink, 5, (3/4,1/4,))
        self.rgb.b.toRun(self.rgb.sleep, 1, (2/4,))
        self.rgb.b.toRun(self.rgb.blink, 4, (3/4,1/4,))
        self.rgb.b.toRun(self.rgb.blink, 5, (2/4,2/4,))
        self.rgb.b.toRun(self.rgb.sleep, 1, (2/4,))
        self.rgb.g.toRun(self.rgb.blink, 5, (2/4,2/4,))
        self.rgb.wait()
        self.rgb.b.toRun(self.rgb.blink, 10, (1/10,1/10,))
        self.rgb.g.toRun(self.rgb.blink, 10, (1/10,1/10,))


    def subEvent(self):
        self.rgb.g.toRun(self.rgb.blink, 7, (1/20,1/10,))
        self.rgb.r.toRun(self.rgb.blink, 7, (1/20,1/10,))
        self.rgb.wait()
        for r in range(4):
            self.rgb.g.toRun(self.rgb.fadeOut, 2, (1/30, 1<<8,))
            self.rgb.r.toRun(self.rgb.fadeOut, 2, (1/30, 1<<8,))
            self.rgb.b.toRun(self.rgb.fadeOut, 1, (1/30, 1<<8,))
            self.rgb.wait()
        self.rgb.g.toRun(self.rgb.blink, 1, (5, .1,))
        self.rgb.r.toRun(self.rgb.blink, 1, (5, .1,))
        self.rgb.b.toRun(self.rgb.breath, 7, (1/20, 1<<18,))
        self.rgb.wait()

    def banEvent(self):
        self.rgb.r.toRun(self.rgb.breath, 12, (1/20, 1<<18, 1<<24,))
        self.rgb.b.toRun(self.rgb.sleep, 1, (1/8,))
        self.rgb.b.toRun(self.rgb.breath, 12, (1/20, 1<<18, 1<<24,))
        self.rgb.wait()

    def baseLoop(self):
        self.rgb.r.toRun(self.rgb.breath, 1, (1/15,1<<15,1<<24))
        self.rgb.wait()
