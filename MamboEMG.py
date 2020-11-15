from pylsl import StreamInlet, resolve_stream
import time
from pyparrot.Minidrone import Mambo
from pynq.overlays.base import BaseOverlay

# 初始化Overlay
base = BaseOverlay('base.bit')

# 初始化LED and Button
for led in base.leds: # base.leds[0]
    led.off()

SW_0 = base.switches[0]

# 初始化时间间隔和EEG强度阈值
# initialize time threshold and variables for storing time
time_thres  = 3000  
r_th = 0.9
l_th = 0.9
if_takeoff = 0 # 1 for takeoff and 0 for landed
prev_time  = 0

# resolve an EMG stream on the lab network and notify the user
print("Looking for an EMG stream...")
streams = resolve_stream('type', 'EMG')
inlet = StreamInlet(streams[0])
print("EMG stream found!")

# Connect to Mambo FPV
mambo = Mambo(use_wifi=True)
print("Trying to connect Mambo")
success = mambo.connect(num_retries=3)
print("connected: %s" % success)

if(success):
    print("Mambo is sleeping...")
    base.leds[0].on()
    
mambo.smart_sleep(2)
mambo.ask_for_state_update()
mambo.smart_sleep(2)

while (True):  
    
    samples, timestamp = inlet.pull_sample() # get EMG data sample and its timestamp

    curr_time = int(round(time.time() * 1000)) # get current time in milliseconds
    
    if((samples[0] >= r_th and samples[1] >= l_th) & (curr_time - time_thres > prev_time) & (if_takeoff == 0)):
        prev_time = int(round(time.time() * 1000)) # update time
        print("Blink both eyes")
        mambo.safe_takeoff(2)  
        if_takeoff = 1

    elif((samples[0] > r_th and samples[1] < l_th) & (curr_time - time_thres > prev_time) & if_takeoff == 1):
        prev_time = int(round(time.time() * 1000)) # update time
        print("Blink right eye")
        mambo.turn_degrees(90)   


    elif((samples[0] < r_th and samples[1] > l_th) & (curr_time - time_thres > prev_time) & if_takeoff == 1):
        prev_time = int(round(time.time() * 1000)) # update time
        print("Blink left eye")
        mambo.turn_degrees(-90)  


    elif((samples[0] == 0 and samples[1] == 0) & (curr_time - time_thres > 2 * prev_time) & if_takeoff == 1):
        prev_time = int(round(time.time() * 1000)) # update time
        print("No Blink")
        print("landing...")   
        mambo.safe_land(5)      
        mambo.smart_sleep(2)

        print("disconnect")
        mambo.disconnect()

        break

    elif(curr_time - time_thres > prev_time): 
        prev_time = int(round(time.time() * 1000)) 