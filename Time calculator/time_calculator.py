def add_time(start_time, duration, start_day = ' '):

    #dividing hours and minutes for start_time
    ppoint = start_time.find(':')
    space = start_time.find(' ')
    am_pm = start_time[space + 1:]
    h = start_time[:ppoint]
    m = start_time[ppoint + 1:space]

    #dividing hours and minutes for duration
    ppoint = duration.find(':')
    h_add = duration[:ppoint]
    m_add = duration[ppoint + 1:]

    #first addition
    result_h = int(h) + int(h_add)
    result_m = int(m) + int(m_add)

    #matching the day
    week = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    final_m_int = result_m
    if result_m > 60:
        final_m_int = result_m - 60
        result_h += 1
    final_m = str(final_m_int).zfill(2)
    ndays = result_h // 24
    h_rem = result_h % 24
    sday = start_day.lower()
    ind = int() 
    rdays = int()
    if am_pm == 'PM' and ndays != 0:
        rdays = ndays + 1
    else:
        rdays = ndays
    if sday in week:
        ind = week.index(sday) 
        day_int = (ind + rdays) % 7
        day = week[day_int]
        f_day = day.capitalize()

    #final time
    new_time = str()
    final_h = h_rem
    if start_day != ' ':
        if h_rem >= 12:
            if am_pm == 'PM' and ndays == 0:
                am_pm = 'AM'
                final_h = h_rem - 12
                if final_h == 0:
                    final_h = 12
                new_time =str(final_h) +':'+ final_m +' '+ am_pm +', '+ f_day +' (next day)'
            elif am_pm == 'PM' and ndays != 0:
                am_pm = 'AM'
                final_h = h_rem - 12
                if final_h == 0:
                    final_h = 12
                new_time =str(final_h) +':'+ final_m +' '+ am_pm +', '+ f_day +' ('+ str(rdays) +' days later)'
            elif am_pm == 'AM' and ndays == 0:
                final_h = h_rem - 12
                if final_h == 0:
                    final_h = 12
                    am_pm = 'PM'
                elif final_h > 0:
                    am_pm = 'PM'
                new_time =str(final_h) +':'+ final_m +' '+ am_pm +', '+ f_day
            elif am_pm == 'AM' and ndays != 0:
                final_h = h_rem - 12
                if final_h == 0:
                    final_h = 12
                    am_pm = 'PM'
                elif final_h > 0:
                    am_pm = 'PM'
                new_time =str(final_h) +':'+ final_m +' '+ am_pm +', '+ f_day +' ('+ str(ndays) +' days later)'
        elif h_rem < 12:
            if ndays == 0:
                new_time =str(final_h) +':'+ final_m +' '+ am_pm +', '+ f_day 
            elif ndays == 1:
                new_time =str(final_h) +':'+ final_m +' '+ am_pm +', '+ f_day +' (next day)'
            elif ndays > 1:
                new_time =str(final_h) +':'+ final_m +' '+ am_pm +', '+ f_day +' ('+ str(ndays) +' days later)'
    else:
        if h_rem >= 12:
            if am_pm == 'PM' and ndays == 0:
                am_pm = 'AM'
                final_h = h_rem - 12
                if final_h == 0:
                    final_h = 12
                new_time =str(final_h) +':'+ final_m +' '+ am_pm +' (next day)'
            elif am_pm == 'PM' and ndays != 0:
                am_pm = 'AM'
                final_h = h_rem - 12
                if final_h == 0:
                    final_h = 12
                new_time =str(final_h) +':'+ final_m +' '+ am_pm +' ('+ str(rdays) +' days later)'
            elif am_pm == 'AM' and ndays == 0:
                final_h = h_rem - 12
                if final_h == 0:
                    final_h = 12
                    am_pm = 'PM'
                elif final_h > 0:
                    am_pm = 'PM'
                new_time =str(final_h) +':'+ final_m +' '+ am_pm
            elif am_pm == 'AM' and ndays != 0:
                final_h = h_rem - 12
                if final_h == 0:
                    final_h = 12
                    am_pm = 'PM'
                elif final_h > 0:
                    am_pm = 'PM'
                new_time =str(final_h) +':'+ final_m +' '+ am_pm +' ('+ str(ndays) +' days later)'
        elif h_rem < 12:
            if ndays == 0:
                new_time =str(final_h) +':'+ final_m +' '+ am_pm
            elif ndays == 1:
                new_time =str(final_h) +':'+ final_m +' '+ am_pm +' (next day)'
            elif ndays > 1:
                new_time =str(final_h) +':'+ final_m +' '+ am_pm +' ('+ str(ndays) +' days later)'
    return new_time                  
    




            


    















