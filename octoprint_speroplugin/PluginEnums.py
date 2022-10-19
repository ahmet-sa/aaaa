

from enum import Enum



class ItemState(Enum):
    
    AWAIT="Await"
    PRINTING="Printing"
    EJECTING="Ejecting"
    EJECT_FAIL="eject fail"
    CANCELLED="Cancelled"
    CANCELLING="Cancelling"
    FAILLED="Failed"
    PAUSED="Paused"
    PAUSING="Pausing"
    FINISHED="Finished"

class QueueState(Enum):
    
    IDLE="IDLE"
    STARTED="STARTED"
    RUNNING="RUNNING"
    CANCELLED="CANCELLED"
    PAUSED="PAUSED"

    def __str__(self):
     return str(self.value)



class BedPosition(Enum):
    MIDDLE="Middle"
    FRONT="Front"
    BACK="Back"
    
    # def __str__(self):
    #     return str(self.value)



class MotorState(Enum):
    IDLE="Idle"
    FORWARD="Forward"
    BACKWORD="Backword"
    
class EjectState(Enum):
    IDLE="IDLE"
    WAIT_FOR_TEMP="WAIT_FOR_TEMP"
    EJECTING="EJECTING"
    EJECTING_FINISHED="EJECTING_FINISHED"
    EJECT_FAİL="eject fail"



