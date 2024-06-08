# imports
from playsound import playsound as ps; from time import sleep as wait; import os
# set sound path
script_dir = os.path.dirname(os.path.abspath(__file__)); sound_file_name = 'alarm.mp3'; sound_file_path = os.path.join(script_dir, sound_file_name)
# ask how long
hrs = int(input('Hours: '))
minutes = int(input('Minutes: '))
sec = int(input('Seconds: '))
# maths
sec = (((int(hrs)*60)*60) + (int(minutes)*60) + int(sec))
# timer
print('set')
wait(sec)
print('its done!!!!!!')
ps(sound_file_path)
exit