#!/usr/bin/python3

from gpiozero import PWMLED
from time import sleep
from threading import Thread

class LedThread(Thread):

  def __init__(self, led):
    super(LedThread, self).__init__()
    self.queue = []
    self.is_stopped = False
    self.led = led
    self.start()

  def toRun(self, fun, args):
      self.queue.append((fun,args[1:]))

  def run(self):
    while True:
      print(len(self.queue))
      if len(self.queue) > 0:
        (fun, args) = self.queue.pop(0)
        fun(self.led, *args)
      sleep(0.5)


  def stop(self):
    self.is_stopped = True

  def stopped(self):
    return self._stop_event.is_set()
