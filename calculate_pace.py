# A pace, distance and time converter

def to_pace():
    distance = input('Enter the distance [km]: ') 
    time = input('Enter a time [hh:mm:ss]: ')
    split_time = time.split(':')
    hours_time = int(split_time[0])
    minutes_time = int(split_time[1])
    seconds_time = int(split_time[2])
    total_minutes = ((hours_time * 3600) + (minutes_time * 60) + seconds_time)/60  
    pace_frac = total_minutes/float(distance)
    pace_minute = pace_frac // 1
    pace_second = (pace_frac % 1) * 60
    print('With a time of '+str(time)+ ' and a distance of '+ str(distance)+' km')
    print('Your pace will be: ['+ str(round(pace_minute)).zfill(2) +':'+ str(round(pace_second)).zfill(2)+']')
    print(str(round(float(distance)/(total_minutes/60),1))+' km/h')
    return

def to_time():
    pace = input('Enter a pace (min/km) [xx:xx] :')
    distance = input('Enter a distance in km: ')
    split_pace = pace.split(':')
    minutes = split_pace[0]
    seconds_fraction = int(split_pace[1])/60
    conc_frac_pace = int(minutes)+seconds_fraction
    time_min = conc_frac_pace * float(distance)
    hours = time_min // 60
    minutes_tot = time_min % 60
    seconds = (minutes_tot % 1) * 60
    print('With a pace of '+str(pace)+ ' and a distance of '+ str(distance)+' km')
    print('The total time will be ['+str(int(hours)).zfill(2)+':'+str(int(minutes_tot)).zfill(2)+':'+ str(int(seconds)).zfill(2)+ ']') 
    print(str(round(float(distance)/(time_min/60),1))+' km/h')
    return

def to_distance():
    pace = input('Enter a pace (min/km) [xx:xx] :')
    time = input('Enter a time [hh:mm:ss]: ')
    split_pace = pace.split(':')
    minutes_pace = split_pace[0]
    seconds_fraction = int(split_pace[1])/60
    conc_frac_pace = int(minutes_pace)+seconds_fraction
    split_time = time.split(':')
    hours_time = int(split_time[0])
    minutes_time = int(split_time[1])
    seconds_time = int(split_time[2])
    total_minutes = ((hours_time * 3600) + (minutes_time * 60) + seconds_time)/60  
    distance = total_minutes / conc_frac_pace
    print('With a time of '+str(time)+ ' and a pace of '+ str(pace))
    print('The distance covered is: '+ str(round(distance,1)).zfill(2)+ ' km')
    print(str(round(distance/(total_minutes/60),1))+' km/h')
    return

# Ask user which conversion


try:
    while True: 
        convert = input('Which conversion? pace, time, distance \n')
        if convert == 'pace' or convert == 'p':
            to_pace()
        if convert == 'time' or convert == 't':
            to_time()
        if convert == 'distance' or convert == 'd':
            to_distance()
        convert = None

        poll_new_conv = input('Another conversion? y or n \n')
        if poll_new_conv == 'n':
            break


except KeyboardInterrupt:
    print('Stopped by user')
except ValueError:
    print('Faulty input')
except:
    print('Fuck some error occured')    

