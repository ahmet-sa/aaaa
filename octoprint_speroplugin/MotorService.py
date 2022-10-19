from multiprocessing import connection
from sqlite3 import connect
from time import time
import RPi.GPIO as GPIO 
from signal import pause
from datetime import datetime, timedelta
from timeit import default_timer
import time
from unicodedata import name
import RPi.GPIO as GPIO 
from enum import Enum


durum="MotorState.IDLE"
connectionn="disconnected"
GPIO.setmode(GPIO.BCM)


class MotorService():
   
   def __initMotor(self):
      global connectionn

      if self._pin1 and self._pin2:
         connectionn="connected"
         GPIO.setup(self._pin1,GPIO.OUT)
         GPIO.setup(self._pin2,GPIO.OUT)


   def __init__(self,pin1,pin2):
      self._pin1 = pin1
      self._pin2 = pin2
      self.__initMotor()
   
   

   def stop(self):
      print("motor_service stop")
      global durum
      if self._pin1 and self._pin2:
         GPIO.output(self._pin1,False)
         GPIO.output(self._pin2,False)
         durum = "MotorState.IDLE"

   def goForward(self):
      print("motor_service forward")
      global durum
      if self._pin1 and self._pin2:
         print("motor service pin 1 and  2")
         print(self._pin1)
         print(self._pin2)
         
         GPIO.output(self._pin1,True)
         GPIO.output(self._pin2,False)
         print(durum)
         durum = "MotorState.FORWARD"
    


   def goBackward(self):
      print("motor_service backword")
      global durum
      if self._pin1 and self._pin2:
         GPIO.output(self._pin1,False)
         GPIO.output(self._pin2,True)
         print(durum)
         durum = "MotorState.BACKWARD"
   


 


         
class MotorState(Enum):
  IDLE = 0
  FORWARD =1
  BACKWARD =2
  
  def getState():
     return durum
  def getConnection():
     return connectionn