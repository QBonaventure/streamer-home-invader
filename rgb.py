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
    self.r2 = LedThread(PWMLED("GPIO20"), baseClock)
    self.scale = [x/255 for x in (0, 2, 3, 4, 6, 8, 11, 16, 23, 32, 45, 64, 90, 128, 181, 255)]

  def base(self):
      self.r.toRun(self.breath, 10, (1/30, 1<<20, 1<<24,))
      self.b.toRun(self.sleep, 1, (1/8,))
      self.b.toRun(self.breath, 10, (1/30, 1<<20, 1<<24,))
      self.wait((self.r, self.b,))

  def wait(self):
    ledThreads = (self.r, self.g, self.b,)
    while all(v.is_active == 0 for v in ledThreads) == False:
        sleep(self.baseClock)

  def sleep(self, led, sleepTime):
      sleep(sleepTime)


  def breath(self, led, sleepTime, minValue, maxValue = 1<<8):
    lvalue = 1<<1

    while(lvalue < maxValue):
      led.value = (lvalue>>1)/maxValue
      lvalue = lvalue << 1
      sleep(sleepTime)

    sleep(sleepTime)

    while(lvalue >= minValue):
      led.value = lvalue/maxValue
      lvalue = lvalue >> 1
      sleep(sleepTime)


  def blink(self, led, onTime, offTime):
      led.value = 1
      sleep(onTime)
      led.value=0
      sleep(offTime)
