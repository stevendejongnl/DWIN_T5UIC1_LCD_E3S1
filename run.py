#!/usr/bin/env python3
import subprocess

from dwinlcd import DWIN_LCD

encoder_Pins = (19, 26)
button_Pin = 13
LCD_COM_Port = '/dev/ttyAMA0'
API_Key = subprocess.check_output('/home/steven/moonraker/scripts/fetch-apikey.sh', shell=True, text=True)

DWINLCD = DWIN_LCD(
    LCD_COM_Port,
    encoder_Pins,
    button_Pin,
    API_Key.strip()
)
