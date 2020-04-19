#!/usr/bin/env python3

from cozify import hub
import datetime
from datetime import timezone
import os.path
from os import path
import mmap

fileFormat = 'utf-8' #'iso-8859-1' #'utf-16'

def EpochToTimeStamp(epochTime):
  return datetime.datetime.utcfromtimestamp(epochTime / 1e3).replace(tzinfo=timezone.utc).strftime('%Y-%m-%d %H:%M:%S') #UTC
  #return datetime.datetime.fromtimestamp(epochTime / 1e3).replace(tzinfo=timezone.utc)#.strftime('%Y-%m-%d %H:%M:%S') #LOCAL

def EmptyValueFix(value):
  if (value == None):
    return ''
  
  return value

def NumberSeparatorFix(value):  
  return str(value).replace('.', ',')

def LastNlines(fname, N): 
  list_of_lines = []
  with open(fname, encoding=fileFormat) as file:
    for line in (file.readlines() [-N:]):
      list_of_lines.append(line)
  
  return list_of_lines

def HandleError(exception):
  f = open('errors.log', 'a', newline='', encoding=fileFormat)
  errText = "{0}: {1}".format(datetime.utcnow().timestamp(), str(exception))
  f.writelines(errText + '\n')
  f.close()

# Main logic
try:
  fileName = 'device_temperatures.csv'
  lastLines = []

  if path.exists(fileName):
    size = os.path.getsize(fileName)
    print('File {0} exist and file size is {1} bytes.'.format(fileName, size))

    lastLines = LastNlines(fileName, 10)
    f = open(fileName, 'a', newline='', encoding=fileFormat)
  else:
    print('File {0} does not exist.'.format(fileName))
    f = open(fileName, 'w', newline='', encoding=fileFormat)
    header = '"Device","Timestamp","Temperature","Humidity"'
    f.writelines(header + '\n')

  print('')
  devices = hub.devices(capabilities=hub.capability.TEMPERATURE)

  for id, dev in devices.items():
    row = '"{0}","{1}","{2}","{3}"'.format(dev['name'], EpochToTimeStamp(dev['state']['lastSeen']), NumberSeparatorFix(EmptyValueFix(dev['state']['temperature'])), EmptyValueFix(dev['state']['humidity']))
    
    # check does measurement already exist on log file.
    matching = [s for s in lastLines if row in s]
    #print(row)

    if len(matching) > 0:
      print('{0}| Measurement not saved because it''s already exists.'.format(row))
    else:
      print('{0}| Measurement saved.'.format(row))
      f.writelines(row + '\n')

  f.close()
except Exception as e:
  HandleError(e)
  pass
finally:
  pass