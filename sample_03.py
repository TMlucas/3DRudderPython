#####################################################################################
#
# Sample 03 - This sample presents the Event processing.
#
# Python 3.5.2
# 
# SDK 3dRudder
#
# Copyright (C) 2016-2017 3dRudder
#
#####################################################################################
import platform



# 32 or 64 bit
val_max=platform.architecture()

print(val_max[0])
if (val_max[0]=='32bit') : 
    from win32.Python363.ns3DRudder import * #import SDk 3dRudder
else:
    from x64.Python363.ns3DRudder import * #import SDk 3dRudder
import time


#-------------------------------------
#-------------------------------------
class CEvent(IEvent):
    
    def __init__(self) :
        IEvent.__init__(self)
        print("Create Event")

    def OnConnect(self,nDeviceNumber):
        print("-> 3dRudder is Connected") 
        
    def OnDisconnect(self,nDeviceNumber):
        print("-> 3dRudder is DisConnected") 
        


#-------------------------------------
# my code here
#-------------------------------------
def main():
    print("----------------------------")
    print("3dRudder")
    print("----------------------------")
    print("Start Sample 03")


    # 3dRudder settings
    nPortNumber=0
    myevent = CEvent()

    try:

        # Init SDk 3dRudder
        sdk=GetSDK()
        sdk.Init()

        sdk.SetEvent(myevent)
       
        while True:
            time.sleep(1)
        

    except KeyboardInterrupt as e:
        print ("->Stop by User")
   
    except ValueError as err:
        print ("Error : ",err )    
    finally:

        print("End Sample 03")
        print("----------------------------")


#-------------------------------------
#-------------------------------------
if(__name__ == "__main__"):
    main()



