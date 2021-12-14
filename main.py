def to_d_station(station, func):
    d_station={
        'a':0,
        'b':3,
        'c':5,
        'd':4}
    if station == 'f':
        station = 'b'
    elif station == 'e':
        station= 'a'
    time_arrive = func(station, d_station)
    return time_arrive


def to_a_station(station, func):
    a_station={
        'd':0,
        'c':4,
        'b':5,
        'a':3}
    if station == 'f':
        station = 'b'
    elif station == 'e':
        station= 'a'
    time_arrive = func(station, a_station)
    return time_arrive


def to_f_station(station, func):
    f_station={
        'e':0,
        'a':6,
        'b':3,
        'f':5}
    if not station in f_station:
        station = 'b'
    time_arrive = func(station, f_station)
    return time_arrive


def to_e_station(station, func):
    e_station={
        'f':0,
        'b':5,
        'a':3,
        'e':6}
    if not station in e_station:
        station = 'b'
    time_arrive = func(station, e_station)
    return time_arrive


def dt_now():
    from datetime import datetime
    dt_min = datetime.now().minute
    dt_hour = datetime.now().hour
    return dt_hour, dt_min


def all_minuts(h, m):
    hour,min = dt_now()
    hour = hour - h
    min = min - m
    all_min = hour*60+min
    return all_min


def close_bus_time_10(station_name, Gostation):
    times = all_minuts(5, 0)%10
    time = 0
    for i in Gostation:
        time += Gostation[i]
        if i == station_name:
            break
    if (time - times)<0:
        new = 10+time-times
        return new
    elif (time - times)>=10:
        new = time-times-10
        return new
    else:
        new = time-times
        return new


def close_bus_time_5(station_name, Gostation):
    times = all_minuts(5, 10)%5
    time = 0
    for i in Gostation:
        time += Gostation[i]
        if i == station_name:
            break
    if (time - times)<0:
        new = 5+time-times
        return new
    elif (time - times)>=5 and (time - times)<10:
        new = time-times-5
        return new
    elif (time - times)>=10:
        new = time-times-10
        return new
    else:
        new = time-times
        return new


def find_near(station):
    from datetime import datetime
    d_station = [104,'destination D',to_d_station(station, close_bus_time_10),'min', 'd']
    a_station = [104,'destination A',to_a_station(station, close_bus_time_10),'min', 'a']
    f_station = [437,'destination F',to_f_station(station, close_bus_time_5), 'min', 'f']
    e_station = [437,'destination E',to_e_station(station, close_bus_time_5), 'min', 'e']
    temp_list = [a_station, d_station, f_station, e_station]
    near_list = []
    for i in temp_list:
        if i[-1]!=station:
            near_list.append(i)
    near_list = sorted(near_list, key=lambda time: time[2], reverse=False)
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    print(f"Current time: {current_time} ")
    print('Schedule:')
    for i in near_list:
        print(f'| {i[0]} | {i[1]} | {i[2]} {i[3]} |')


def all_close():
    lst_stations = ['a','b','c','d','e','f']
    while True:
        station = input('Enter station: ').lower()
        if station in lst_stations:
            find_near(station)
        elif station == '':
            break
        else:
            print('No such station!')


all_close()
