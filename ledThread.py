#!/usr/bin/python3

from gpiozero import PWMLED
from time import sleep
from threading import Thread

class LedThread(Thread):


  def __init__(self, led, baseClock):
    super(LedThread, self).__init__()
    self.queue = []
    self.led = led
    self.baseClock = baseClock
    self.taskCount = 0
    self.start()

  def toRun(self, fun, loopNb=1, args=()):
      for _ in range(loopNb):
        self.queue.append((fun, args))
        self.taskCount += 1

  def run(self):
    while True:
      if len(self.queue) > 0:
        self.is_active = True
        (fun, args) = self.queue.pop(0)
        fun(self, *args)
      sleep(self.baseClock)

  def done(self):
    self.taskCount = self.taskCount - 1

  def getValue(self, value):
      return self.led.value

  def setValue(self, value):
      self.led.value = value

  value = property(getValue, setValue)
