from pynq.overlays.base import BaseOverlay
from pynq.lib.arduino import Arduino_IO
from pynq import Overlay
from pynq.lib import Wifi
import time

# 初始化Overlay
base = BaseOverlay('base.bit')

# USB WiFi连接Mambo
port = Wifi()
port.connect('Mambo_785167','1234567890')

# 初始化Audio语音播报模块，使用Arduino作为GPIO
A = []
for i in range(0,5):
    A.append(Arduino_IO(base.ARDUINO,i+15,"out"))
    A[i].write(1)

def audio_1():
    A[0].write(0)
    A[1].write(0)
    A[2].write(0)
    time.sleep(1.7)
    A[0].write(1)
    time.sleep(0.01)
    A[1].write(1)
    time.sleep(0.01)
    A[2].write(1)
    time.sleep(0.1)

def audio_2():
    A[1].write(0)
    A[2].write(0)
    time.sleep(1.5)
    A[1].write(1)
    time.sleep(0.01)
    A[2].write(1)
    time.sleep(0.01)

def audio_3():
    A[0].write(0)
    A[1].write(0)
    time.sleep(1.7)
    A[0].write(1)
    time.sleep(0.01)
    A[1].write(1)
    time.sleep(0.1)

def audio_4():    
    A[0].write(0)
    A[2].write(0)
    time.sleep(1.75)
    A[0].write(1)
    time.sleep(0.01)
    A[2].write(1)
    time.sleep(0.01)
    
def audio_5():
    A[0].write(0)
    time.sleep(0.15)
    A[0].write(1)
    time.sleep(0.01)
    
def audio_5():
    A[1].write(0)
    time.sleep(0.15)
    A[1].write(1)
    time.sleep(0.01)

def audio_6():
    time.sleep(5)
    print("降落")
    A[3].write(0)
    time.sleep(1.7)
    A[3].write(1)
    time.sleep(0.1)
    
def audio_7():   
    A[0].write(0)
    A[2].write(0)
    time.sleep(1.4)
    A[0].write(1)
    time.sleep(0.01)
    A[2].write(1)
    time.sleep(0.01)
    
def audio_8():
    A[2].write(0)
    time.sleep(0.2)
    A[2].write(1)
    time.sleep(0.01)