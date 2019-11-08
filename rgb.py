#!/usr/bin/python3

from gpiozero import PWMLED
from time import sleep
from threading import Thread
from ledThread import LedThread

class RGB:


  def __init__(self):
    self.r = PWMLED("GPIO6")
    self.g = PWMLED("GPIO16")
    self.b = PWMLED("GPIO20")


  def setAll(self, value):
    self.r.value = value
    self.g.value = value
    self.b.value = value


  def black(self):
    self.setAll(0)


  def white(self):
    self.setAll(1)


  def defaultEventLoop(self):
      i = 0
      st = .2
      self.black()

      while(i < 20):
        self.r.value = 1
        sleep(st)
        self.g.value = 1
        sleep(st)
        self.b.value = 1
        sleep(st*5)
        i = i+1


  def streamChangeLoop(self):
      n = 0
      st = .2

      while(n < 5):
          self.black()
          self.r.value = 1
          self.g.value = 1
          self.b.value = 1
          i = 0
          while(i < 19):
            self.r.value = self.r.value - 0.05
            self.g.value = self.g.value - 0.05
            self.b.value = self.b.value - 0.05
            sleep(0.1)
            i = i+1
          self.black()
          n = n+1


  def subscriptionLoop(self):
      i = 0
      st = .1

      self.black()

      while(i < 60):
        self.g.value = .6
        self.r.value = 1
        sleep(st)
        self.g.value = 0.1
        self.r.value = 0.5
        sleep(st)
        i = i+1


  def followLoop(self):
      i = 0
      st = .2

      self.black()

      while(i < 5):
        self.g.value = 1
        sleep(st)
        self.g.value = 0
        sleep(0.8)
        i = i+1


  def modSwitchLoop(self):
      i = 0
      st = .2

      self.black()

      while(i < 4):
        self.b.value = 1
        sleep(st)
        self.b.value = 0.4
        sleep(st)
        i = i+1

  def banLoop(self):
      i = 0
      st = .2

      self.black()

      while(i < 20):
        self.r.value = 1
        sleep(st)
        self.r.value = 0.4
        sleep(st)
        i = i+1


  def breath(self, led, sleepTime, minValue, maxValue = 1<<8):
    lvalue = minValue

    while(lvalue < maxValue):
      led.value = (lvalue-1)/maxValue
      lvalue = lvalue << 1
      sleep(sleepTime)

    sleep(sleepTime)

    while(lvalue >= minValue):
      led.value = (lvalue-1)/maxValue
      lvalue = lvalue >> 1
      sleep(sleepTime)


  def blink(self, led, onTime, offTime):
      led.value = 1
      sleep(onTime)
      led.value=0
      sleep(offTime)
