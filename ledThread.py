#!/usr/bin/python3

from gpiozero import PWMLED
from time import sleep
from threading import Thread

class LedThread(Thread):

  def __init__(self, led, baseClock):
    super(LedThread, self).__init__()
    self.queue = []
    self.is_stopped = False
    self.led = led
    self.baseClock = baseClock
    self.start()
    self.is_active

  def toRun(self, fun, loopNb=1, args=()):
      for _ in range(loopNb):
        self.queue.append((fun, args))

  def run(self):
    while True:
      if len(self.queue) > 0:
        self.is_active = True
        (fun, args) = self.queue.pop(0)
        fun(self.led, *args)
      self.is_active = False
      sleep(self.baseClock)


  def stop(self):
    self.is_stopped = True

  def stopped(self):
    return self._stop_event.is_set()
