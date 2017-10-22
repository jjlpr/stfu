import yaml
import subprocess
import json

# global state is best state
buffer = []
inNoisyState = False
noisyStateBeginTime = 0


# Load config file
with open('monitor.yml', 'r') as ymlfile:
    config = yaml.load(ymlfile)

# begin watching the file
f = subprocess.Popen(['tail','-F','-n 1', config['monitor_file']],\
        stdout=subprocess.PIPE,stderr=subprocess.PIPE)

def callTrigger():
  print(subprocess.check_output(config['trigger_command'].split()))

def checkBuffer():
  global buffer, inNoisyState, noisyStateBeginTime
  print(buffer)

  # just based on last av
  lastSecond = buffer[-1]
  print( config['noisy_end'], lastSecond['av'] )

  if( inNoisyState == True and lastSecond['av'] > config['noisy_end'] ):
    inNoisyState = False
    callTrigger()
    print('inNoisyState end!')
  elif( inNoisyState == False
          and lastSecond['time'] > (noisyStateBeginTime + config['rate_limit_ms'])
          and lastSecond['av'] > config['noisy_start'] ):
    inNoisyState = True
    noisyStateBeginTime = lastSecond['time']
    print('inNoisyState begin')


# all good programs have an infinate loop!
while True:
    line = f.stdout.readline()
    strippedLine = line.decode("utf-8").rstrip('\n').rstrip(',').strip(',')
    secondData = json.loads(strippedLine)
    buffer.append(secondData)
    if( len(buffer) > config['buffer_length'] ):
      buffer.pop(0)
    checkBuffer()
