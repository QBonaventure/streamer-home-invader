#!/usr/bin/python3

from gpiozero import PWMLED
from time import sleep
from threading import Thread
from ledThread import LedThread

class RGB:

  def __init__(self):
    self.r = LedThread(PWMLED("GPIO6"))
    self.g = LedThread(PWMLED("GPIO16"))
    self.b = LedThread(PWMLED("GPIO20"))
    self.queue = []


  def queue(self, *args):
      self.queue.append(args)
      print(self.queue)
      led = getattr(self, args[0])
      print(fun)
      led.toRun(getattr(self, fun), args)


  def run(self, fun, *args):
    led = getattr(self, args[0])
    print(fun)
    led.toRun(getattr(self, fun), args)


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
      i = 0
      st = .2

      self.black()

      while(i < 20):
        self.r.value = 1
        self.g.value = 1
        self.b.value = 1
        sleep(st*3)
        self.black()
        sleep(st)
        i = i+1


  def subscriptionLoop(self):
      i = 0
      st = .1

      self.black()

      while(i < 20):
        print('zzzzz')
        self.g.value = .7
        self.r.value = 1
        sleep(st)
        self.g.value = 0.4
        self.r.value = 0.7
        sleep(st)
        i = i+1


  def followLoop(self):
      i = 0
      st = .2

      self.black()

      while(i < 20):
        self.g.value = 1
        sleep(st)
        self.g.value = 0.4
        sleep(st)
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


  def breath(self, led):
    sleepTime = 1/10

    minValue = 1
    maxValue = 1 << 12
    lvalue = minValue
    print(led)
    while(lvalue < maxValue):
      led.value = lvalue/maxValue
      lvalue = lvalue << 1
      sleep(sleepTime)
    sleep(sleepTime)
    while(lvalue >= minValue):
      led.value = lvalue/maxValue
      lvalue = lvalue >> 1
      sleep(sleepTime)
    led.value = 0

  def blink(self, led, onTime, offTime):
      led.value = 1
      sleep(onTime)
      led.value=0
      sleep(offTime)


  def baseLoop(self):
    inc = 0.04
    lvalue = inc
    sleepTime = 1/10

    self.black()

    while(lvalue <= 1):
      self.r.value = round(lvalue, 2)
      lvalue = lvalue+inc
      sleep(sleepTime)

    while(lvalue >= 0):
      self.r.value = round(lvalue, 2)
      lvalue = lvalue-inc
      sleep(sleepTime)


  def testLoop(self):
      self.redd(.5)
      sleep(.5)

      self.redd(1)
      sleep(.5)

      self.redd(.5)
      sleep(.5)

      self.redd(0)
      sleep(.5)
