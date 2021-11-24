#!/usr/bin/env python
import tkinter
import PySimpleGUI as sg

sg.theme('Dark red')     # Please always add color to your window
# The tab 1, 2, 3 layouts - what goes inside the tab
tab1_layout = [[sg.Text('Conversion, enter two')],
               [sg.Text('and calculate the other')],
               [sg.Text('Pace:           '), sg.Input(size=(8,1), key='-PACE-')],
               [sg.Text('Distance:      '), sg.Input(size=(8,1), key='-DIST-')],
               [sg.Text('Time:           '), sg.Input(size=(8,1), key='-TIME-')],
               [sg.Button("Calculate")],
               [sg.Text('Speed    :  '),sg.Text(size=(15,1), key='-SPEED-')],
               [sg.Text('Pace      :  '),sg.Text(size=(15,1), key='-CPACE-')],
               [sg.Text('Distance :  '),sg.Text(size=(15,1), key='-CDIST-')],
               [sg.Text('Time      :  '),sg.Text(size=(15,1), key='-CTIME-')],
               ]

tab2_layout = [[sg.Text('Precentage of desired pace')],
               [sg.Text('Your pace:'), sg.Input(size=(6,1), key='-PACETOPRO-')],
               [sg.Button("Calculate precentage")],
               [sg.Text('125%   '),sg.Text(size=(15,1), key='-125-')],
               [sg.Text('120%   '),sg.Text(size=(15,1), key='-120-')],
               [sg.Text('115%   '),sg.Text(size=(15,1), key='-115-')],
               [sg.Text('110%   '),sg.Text(size=(15,1), key='-110-')],
               [sg.Text('105%   '),sg.Text(size=(15,1), key='-105-')],
               [sg.Text('95%    '),sg.Text(size=(15,1), key='-95-')],
               [sg.Text('90%    '),sg.Text(size=(15,1), key='-90-')],
               [sg.Text('85%    '),sg.Text(size=(15,1), key='-85-')],
               [sg.Text('80%    '),sg.Text(size=(15,1), key='-80-')],
               [sg.Text('75%    '),sg.Text(size=(15,1), key='-75-')],               
               ]

# The TabgGroup layout - it must contain only Tabs
tab_group_layout = [[sg.Tab('Conversion ', tab1_layout, font='Courier 15', key='-TAB1-'),
                     sg.Tab('% of pace', tab2_layout, key='-TAB2-'),
                     ]]

# The window layout - defines the entire window
layout = [[sg.TabGroup(tab_group_layout,
                       enable_events=True,
                       key='-TABGROUP-')],
          ]

window = sg.Window('Pace, time and distance tools', layout,location=(0,0), margins=(100, 100),
                     no_titlebar=False)

tab_keys = ('-Conversion-','-Precentage of desired pace-')         # map from an input value to a key

def to_pace(time_to_pace, distance_to_pace):
    time = str(time_to_pace)
    split_time = time.split(':')
    hours_time = int(split_time[0])
    minutes_time = int(split_time[1])
    seconds_time = int(split_time[2])
    total_minutes = ((hours_time * 3600) + (minutes_time * 60) + seconds_time)/60  
    pace_frac = total_minutes/float(distance_to_pace)
    pace_minute = pace_frac // 1
    pace_second = (pace_frac % 1) * 60
    pace_calc = str(round(pace_minute)).zfill(2) +':'+ str(round(pace_second)).zfill(2)
    speed = str(round(float(distance_to_pace)/(total_minutes/60),1))+ ' km/h'
    return pace_calc, speed

def to_time(pace_to_time, distance_to_time):
    split_pace = pace_to_time.split(':')
    # print(split_pace[0]+'  '+ split_pace[1])
    # for i in range(0,len(split_pace)):
    #     print(split_pace[i])
    minutes = split_pace[0]
    seconds_fraction = int(split_pace[1])/60
    conc_frac_pace = int(minutes)+seconds_fraction
    time_min = conc_frac_pace * float(distance_to_time)
    hours = time_min // 60
    minutes_tot = time_min % 60
    seconds = (minutes_tot % 1) * 60
    time_calc = str(int(hours)).zfill(2)+':'+str(int(minutes_tot)).zfill(2)+':'+ str(int(seconds)).zfill(2) 
    speed = str(round(float(distance_to_time)/(time_min/60),1))+' km/h'
    return time_calc, speed

def to_distance(pace_to_dist, time_to_dist):
    split_pace = pace_to_dist.split(':')
    # for i in range(0,len(split_pace)):
    #     print(split_pace[i])
    minutes_pace = split_pace[0]
    seconds_fraction = int(split_pace[1])/60
    conc_frac_pace = int(minutes_pace)+seconds_fraction
    split_time = time_to_dist.split(':')
    hours_time = int(split_time[0])
    minutes_time = int(split_time[1])
    seconds_time = int(split_time[2])
    total_minutes = ((hours_time * 3600) + (minutes_time * 60) + seconds_time)/60  
    distance = total_minutes / conc_frac_pace
    dist_calc = str(round(distance,1)).zfill(2)
    speed = str(round(distance/(total_minutes/60),1))+' km/h'
    return dist_calc, speed

#___________________________________________________________________________________________
while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break
    if event == "Calculate precentage":
        pace = values['-PACETOPRO-']
        print(pace)
        split_pace = pace.split(':')
        minutes_pace = split_pace[0]
        seconds_fraction = int(split_pace[1])/60
        conc_frac_pace = int(minutes_pace)+seconds_fraction
        paces = []
        paces_min = []
        paces_sec = []
        temp = []

        # print('With a desired pace of ' + str(pace) + ' your pace at: ')
        for x in range(-5,6):
            paces.append(conc_frac_pace * ((100+(x*5))/100))
            paces_min.append(paces[x+5] // 1)
            paces_sec.append((paces[x+5] % 1)*60)

        for i in range(0,len(paces)):
            if i != len(paces)//2:
                temp.append(str(round(paces_min[i])).zfill(2) +':'+ str(round(paces_sec[i])).zfill(2))
        for i in range(0,len(temp)//2):    
            window['-'+str(125-(i*5))+'-'].update(temp[i])
        for i in range(len(temp)//2, len(temp)):    
            window['-'+str(120-(i*5))+'-'].update(temp[i])


    if event == 'Calculate':
        if values['-PACE-'] == '':
            temp_tup = to_pace(values['-TIME-'],values['-DIST-'])
            # print(str(temp_tup[0]) + str(temp_tup[1]))
            window['-CPACE-'].update(temp_tup[0])
            window['-CDIST-'].update(values['-DIST-'])
            window['-CTIME-'].update(values['-TIME-'])
            window['-SPEED-'].update(temp_tup[1])

            
        if values['-DIST-'] == '':
            temp_tup = to_distance(values['-PACE-'],values['-TIME-'])
            # print(str(temp_tup[0]) + str(temp_tup[1]))
            window['-CPACE-'].update(values['-PACE-'])
            window['-CDIST-'].update(temp_tup[0])
            window['-CTIME-'].update(values['-TIME-'])
            window['-SPEED-'].update(temp_tup[1])
            
        if values['-TIME-'] == '':
            temp_tup = to_time(values['-PACE-'],values['-DIST-'])
            # print(str(temp_tup[0]) + str(temp_tup[1]))
            window['-CPACE-'].update(values['-PACE-'])
            window['-CDIST-'].update(values['-DIST-'])
            window['-CTIME-'].update(temp_tup[0])
            window['-SPEED-'].update(temp_tup[1])
            
window.close()