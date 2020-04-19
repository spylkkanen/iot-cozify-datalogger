#!/usr/bin/env python3

from cozify import hub

#ALERT BASS BATTERY_U BRIGHTNESS COLOR_HS COLOR_LOOP COLOR_TEMP CONTACT CONTROL_LIGHT CONTROL_POWER DEVICE DIMMER_CONTROL GENERATE_ALERT HUE_SWITCH HUMIDITY IDENTIFY IKEA_RC LOUDNESS LUX MOISTURE MOTION MUTE NEXT ON_OFF PAUSE PLAY PREVIOUS PUSH_NOTIFICATION REMOTE_CONTROL SEEK SMOKE STOP TEMPERATURE TRANSITION TREBLE TWILIGHT UPGRADE USER_PRESENCE VOLUME

print('')
print('1. Temperature/Humidity sensors') 
devices = hub.devices(capabilities=hub.capability.TEMPERATURE)
for id, dev in devices.items():
  print('{0}: {1}C'.format(dev['name'], dev['state']['temperature']))
  #print('{0}'.format(dev))

print('') 
print('2. Motion detection sensors')
devices = hub.devices(capabilities=hub.capability.MOTION)
for id, dev in devices.items():
  print('{0}: {1}'.format(dev['name'], dev['state']['motion']))
  #print('{0}'.format(dev))

print('')
print('3. Door/Window contact sensors')
devices = hub.devices(capabilities=hub.capability.CONTACT)
for id, dev in devices.items():
  print('{0}: {1}'.format(dev['name'], dev['state']['open']))
  #print('{0}'.format(dev))