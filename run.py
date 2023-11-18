#!/usr/bin/env python3
import datetime
import subprocess
from subprocess import PIPE

from dwinlcd import DWIN_LCD

process = subprocess.Popen('/home/steven/moonraker/scripts/fetch-apikey.sh', stdout=PIPE, stderr=PIPE)
output, error = process.communicate()
print(output)
API_Key = output
process.kill()

encoder_Pins = (19, 26)
button_Pin = 13
LCD_COM_Port = '/dev/ttyAMA0'

print(f"Run start time: {datetime.datetime.now():%Y-%m-%d %H:%M}")

DWINLCD = DWIN_LCD(
    LCD_COM_Port,
    encoder_Pins,
    button_Pin,
    API_Key.strip()
)
