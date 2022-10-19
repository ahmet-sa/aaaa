
# coding=utf-8
from .ButtonService import ButtonService
from .MotorService import MotorService,MotorState
from .SwitchService import SwitchService
from threading import Timer
from signal import pause

class SheildControl:  
   
    onStateChange = None 
  
    def __initControl(self):
        if self._pin1 and self._pin2:
            print('-----------------------------CONTROL ----------------------------------------')

    def __init__(self,pin1,pin2,pin3,pin4,pin5,pin6,pin7,pin8):
      self._pin1 = pin1
      self._pin2 = pin2
      self._pin3 = pin3
      self._pin4 = pin4
      self._pin5 = pin5
      self._pin6 = pin6
      self._pin7 = pin7 
      self._pin8 = pin8
      self.timerOut=None
      self.connectionSheild="Idle"
      self.currIndex=0
      self.isInSequence=False
      self.Control=False
      self.sequenceFinish=True
      self.ejectFail=False
      self.motorState='disconnet'
      self.printBedState='Middle'
      self.sequence = ['W','F','W','B','W','C','S']
      self.actions ={"W":self.wait,"F":self.forward,"B":self.backward,"C":self.correct}
      self.__initControl()
      self.buttonService=ButtonService(self._pin1,self._pin2,self._pin3)
      self.motorService=MotorService(self._pin4,self._pin5)
      self.switchService=SwitchService(self._pin6,self._pin7)
      self.ejectFailTime=self._pin8  

      self.connection()
   
   
      
    def connection(self):
        self.connectionSheild=MotorState.getConnection()

    
    def forward(self):
        self.motorState='Forward'
        self.sendStates()
        
        self.motorService.goForward()

    def backward(self):
        self.motorState='Backward'
        self.sendStates()
        
        self.motorService.goBackward()
        
    def stop(self):
        self.motorState='Stop'
        self.sendStates()
        
        self.motorService.stop()    
  
    def callStop(self):
        self.motorState='Stop'
        self.sendStates()
        
        if self.Control==False:
            self.stop()
            self.currIndex=0
            self.isInSequence=False
        else:
            self.Control=False
            
    def sendActions(self,a):
        if a=="backward":
            self.backward()
        if a=="stop":
            self.stop()
        if a=="forward":
            self.forward()
        if a=="eject":
            self.startSequence()        
            
    def startSequence(self):
        self.ejectFail=False
        self.sequenceFinish=False
        if self.isInSequence==False and self.currIndex==0:
            self.triggerNextJob()
        else :
            self.currIndex=0
            self.isInSequence=False
            self.stop()
            
    def triggerNextJob(self):
        print("next")
        if self.timerOut!=None:
            self.timerOut.cancel()
            self.timerOut=None
        if self.isInSequence==True:
            self.currIndex=self.currIndex+1
            if self.currIndex %2 == 1:
                self.startTimer()
            self.runJob()
        else:
            self.isInSequence=True
            self.runJob()        
    
    
    def startTimer(self):
        if self.timerOut==None:
            self.timerOut = Timer(self.ejectFailTime,self.killTimeOut)
            self.timerOut.start()        
         


    def killTimeOut(self):
        self.timerOut=None
        self.ejectFail=True
        self.callStop()

        

    def runJob(self):
        
        self.currentSeq = self.sequence[self.currIndex]
        self.action = self.actions.get(self.currentSeq,self.jobFinish)
        if self.action :
            self.action()

        
    def jobFinish(self):
        if self.currIndex==6:
            self.callStop()
            self.Control=False
            self.currIndex=0
            self.isInSequence=False
        else :
            self.triggerNextJob()
    
    

        
    def wait(self):
        self.stop()
        waitTimer = Timer(2,self.jobFinish,args=None,kwargs=None)
        waitTimer.start()
 
    def correct(self):
        self.stop()
        waitTimer = Timer(2,self.jobFinish,args=None,kwargs=None)
        waitTimer.start()
        self.motorService.goForward()
        self.sendStates()
        waitTimer = Timer(1,self.stop,args=None,kwargs=None)
        waitTimer.start()
        self.tablaState="Idle"
        self.sequenceFinish=True
        
        
        
 

        
        
    def sendStates(self):
        if self.onStateChange:
            self.onStateChange(self.printBedState,self.motorState,self.ejectFail)
 
 
    def switch1Press(self):
        print("press")
        self.motorService.stop()
        self.printBedState="Forward"
        self.sendStates()
        if self.isInSequence==True and self.sequence[self.currIndex]=='B':
            self.jobFinish()
        if self.isInSequence==True and self.sequence[self.currIndex]=='F':
            self.jobFinish()

        
    def switch2Press(self):
        self.motorService.stop()
        self.printBedState="Backward"
        self.sendStates()
        if self.isInSequence==True and self.sequence[self.currIndex]=='B':
            self.jobFinish()

            
    def switch1Released(self):
        self.printBedState="Middle"
        self.sendStates()
    
    def switch2Released(self):
        self.printBedState="Middle"
        self.sendStates()


   


    def buttonInit(self):
        self.buttonService.onShortPressed = self.startSequence
        self.buttonService.onForwardPressed=self.forward
        self.buttonService.onBackwardPressed=self.backward
        self.switchService.onswitch1Pressed=self.switch1Press
        self.switchService.onSwitch2Pressed=self.switch2Press
        self.switchService.onswitch1Released=self.switch1Released
        self.switchService.onswitch2Realesed=self.switch1Released
        
        
        pause()


            
        
         

  

  
