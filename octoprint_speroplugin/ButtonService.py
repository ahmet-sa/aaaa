from time import time
import RPi.GPIO as GPIO 
from gpiozero import Button
from signal import pause
from .MotorService import MotorService, MotorState


class ButtonService():

    __buttonUtility = None
   
    __timerUtility = 0
    __thresholdUtility = 0

    onLongPressed = None
    onShortPressed = None
    onForwardPressed = None
    onBackwardPressed = None
    onButtonsReleased =None 

    a="a"
    a=MotorState.getState()
    
    def __onHeldUtility(self):
        if self.onLongPressed:
            self.onLongPressed()
    def __onPressedUtility(self):
        self.__timerUtility = time()

    def __onReleasedUtility(self):
        now = time()
        if now-self.__timerUtility < self.__thresholdUtility and self.onShortPressed:
            self.onShortPressed()
    
    def __onPressedForword(self):
        print("Pressed Forward")
        if self.onForwardPressed:
            a=MotorState.getState()
            if a=="MotorState.IDLE":
                self.onForwardPressed()

    def __onReleasedForword(self):
        print("Realesed Forward")
        if self.onButtonsReleased:
            a=MotorState.getState()
            print(a)
            if a=="MotorState.FORWARD":
             self.onButtonsReleased()

    def __onPressedBackword(self):
        
        if self.onBackwardPressed:
            a=MotorState.getState()
            print(a)
            if a=="MotorState.IDLE":
             self.onBackwardPressed()

    def __onReleasedBackword(self):
        if self.onButtonsReleased:
            a=MotorState.getState()
            print(a)
            if a=="MotorState.BACKWARD":
             self.onButtonsReleased()



    def __init__(self,_pin1,_pin2,_pin3,hold_time =3):
        print("Button Service init")
        self.__thresholdUtility = hold_time
        if _pin1:
            print(_pin1)
            self.pinUtility = _pin1
            self.__buttonUtility = Button(_pin1,pull_up=True, hold_time=hold_time)
            self.__buttonUtility.when_held = self.__onHeldUtility
            self.__buttonUtility.when_pressed = self.__onPressedUtility
            self.__buttonUtility.when_released = self.__onReleasedUtility

        if _pin2:
            print(_pin2)
            self.pinForword = _pin2
            self.__buttonForword = Button(_pin2,pull_up=True)
            self.__buttonForword.when_pressed = self.__onPressedForword
            self.__buttonForword.when_released = self.__onReleasedForword
        if _pin3:
            self.pinBackword = _pin3
            self.__buttonBackword = Button(_pin3,pull_up=True)
            self.__buttonBackword.when_pressed = self.__onPressedBackword
            self.__buttonBackword.when_released = self.__onReleasedBackword