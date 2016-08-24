from datetime import datetime
import subprocess

# Write path to .exe that you want
application = r"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
expected = {'hour': 0, 'minute': 0, 'ampm': 'am'}

#User input
print('Uses 12 hour time...')
expected['hour'] = int(input('What HOUR do you want?: '))
expected['minute'] = int(input('What MINUTE do you want?: '))
expected['ampm'] = str(input('AM or PM?: ')).lower()

#goes from 12 to 24 hour timelines.
if (expected['ampm'] == 'pm') and (expected['hour'] < 12):
    #datetime uses 24 hour.
    expected['hour'] += 12

while (True):
    #when current time is > than now execute
    if (datetime.now().hour == expected['hour']) and (datetime.now().minute == expected['minute']):

        try:
            subprocess.Popen([application])
            break
        except Exception as e:
            print('Could not open application...\n', e)
            break
