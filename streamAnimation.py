from rgb import RGB
from time import sleep

class StreamAnimation:

    def __init__(self, rgb):
        self.rgb = rgb

    def defaultLoop(self):
        self.rgb.r.toRun(self.rgb.breath, 10, (1/15, 1<<1, 1<<24,))
        sleep(1)
        self.rgb.wait((self.rgb.r,))

    def banEvent(self):
        self.rgb.r.toRun(self.rgb.breath, 10, (1/40, 1<<18, 1<<24,))
        self.rgb.b.toRun(self.rgb.sleep, 1, (1/8,))
        self.rgb.b.toRun(self.rgb.breath, 12, (1/40, 1<<22, 1<<24,))
        self.rgb.wait()

    def baseLoop(self):
        self.rgb.r.toRun(self.rgb.breath, 1, (1/15,1<<15,1<<24))
        self.rgb.wait()
