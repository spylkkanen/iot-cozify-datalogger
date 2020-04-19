#!/usr/bin/env python3

from cozify import hub
import json

#ALERT BASS BATTERY_U BRIGHTNESS COLOR_HS COLOR_LOOP COLOR_TEMP CONTACT CONTROL_LIGHT CONTROL_POWER DEVICE DIMMER_CONTROL GENERATE_ALERT HUE_SWITCH HUMIDITY IDENTIFY IKEA_RC LOUDNESS LUX MOISTURE MOTION MUTE NEXT ON_OFF PAUSE PLAY PREVIOUS PUSH_NOTIFICATION REMOTE_CONTROL SEEK SMOKE STOP TEMPERATURE TRANSITION TREBLE TWILIGHT UPGRADE USER_PRESENCE VOLUME

devices = hub.devices()
result = "[";
for id, dev in devices.items():
  result += '{0},'.format(dev).replace('\'','"').replace(': None',': "None"').replace(': False',': "False"').replace(': True',': "True"').replace('\\x00','')

if len(result) > 0:
  result = result[:-1]

result += "]";

parsed = json.loads(result)
print(json.dumps(parsed, indent=4, sort_keys=True))