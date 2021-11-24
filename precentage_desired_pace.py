# From a desired pace it gives you +- 25 % in leaps of 5%

# import PySimpleGUI as sg

pace = input('Enter your desired pace (min/km) [mm:ss] : \n')
split_pace = pace.split(':')
minutes_pace = split_pace[0]
seconds_fraction = int(split_pace[1])/60
conc_frac_pace = int(minutes_pace)+seconds_fraction
paces = []
paces_min = []
paces_sec = []

print('With a desired pace of ' + str(pace) + ' your pace at: ')
for x in range(-5,6):
   paces.append(conc_frac_pace * ((100+(x*5))/100))
   paces_min.append(paces[x+5] // 1)
   paces_sec.append((paces[x+5] % 1)*60)

for i in range(0,len(paces)):
   if i != len(paces)//2:
           print(str((125-(i*5))) +' % will be ' + str(round(paces_min[i])).zfill(2) +':'+ str(round(paces_sec[i])).zfill(2))
