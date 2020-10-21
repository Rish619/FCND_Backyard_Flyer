
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from udacidrone import Drone
#matplotlib inline

print(os.getcwd())

t_log = Drone.read_telemetry_data('./Logs/TLog.txt')
north = t_log['MsgID.LOCAL_POSITION'][1][:]
east = t_log['MsgID.LOCAL_POSITION'][2][:]

fig1 = plt.figure(figsize=(10,6))





plt.xlabel('East local position')
plt.ylabel('North local position')


plt.title('X & Y local positions during flight')
plt.plot(east,north)
plt.savefig('Output_Images/East_North_Autonomous_Plot.png')
plt.show() 


t_log = Drone.read_telemetry_data('./Logs/TLog-manual.txt')
north = t_log['MsgID.LOCAL_POSITION'][1][:]
east = t_log['MsgID.LOCAL_POSITION'][2][:]

fig1 = plt.figure(figsize=(10,6))





plt.xlabel('East local position')
plt.ylabel('North local position')


plt.title('X & Y local positions during flight')
plt.plot(east,north)
plt.savefig('Output_Images/East_North_Manual_Plot.png')
plt.show() 


