#!/usr/bin/python3

from gpiozero import PWMLED
from time import sleep
from threading import Thread
from ledThread import LedThread


class RGB:


  def __init__(self, baseClock):
    self.baseClock = baseClock
    self.r = LedThread(PWMLED("GPIO5"), baseClock)
    self.g = LedThread(PWMLED("GPIO12"), baseClock)
    self.b = LedThread(PWMLED("GPIO16"), baseClock)
    self.r2 = LedThread(PWMLED("GPIO20", False), baseClock)
    self.g2 = LedThread(PWMLED("GPIO18", False), baseClock)
    self.b2 = LedThread(PWMLED("GPIO22", False), baseClock)


  def wait(self):
    ledThreads = (self.r, self.g, self.b, self.r2,)
    while sum([t.taskCount for t in ledThreads]) > 0:
        sleep(.1)

    [t.toRun(self.off, 1) for t in ledThreads]


  def stop(self, led):
      led.queue.clear()
      led.done()


  def sleep(self, led, sleepTime):
      sleep(sleepTime)
      led.done()


  def off(self, led, sleepTime=0):
      led.value = 0
      sleep(sleepTime)
      led.done()


  def fadeIn(self, led, sleepTime, minValue = 1<<1, maxValue = 1<<24, isSubElement = False):
    lvalue = minValue
    while(lvalue < maxValue):
      led.value = lvalue/maxValue
      lvalue = lvalue << 1
      sleep(sleepTime)
    if isSubElement == False:
        led.done()


  def fadeOut(self, led, sleepTime, minValue = 1<<1, maxValue = 1<<24, isSubElement = False):
    lvalue = maxValue
    while(lvalue >= minValue):
      led.value = lvalue/maxValue
      lvalue = lvalue >> 1
      sleep(sleepTime)
    if isSubElement == False:
        led.done()


  def breath(self, led, sleepTime, minValue, maxValue = 1<<24):
    lvalue = minValue
    self.fadeIn(led, sleepTime, minValue, maxValue, True)
    sleep(sleepTime)
    self.fadeOut(led, sleepTime, minValue, maxValue, True)
    led.done()


  def blink(self, led, onTime, offTime):
      led.value = 1
      sleep(onTime)
      led.value = 0
      sleep(offTime)
      led.done()
