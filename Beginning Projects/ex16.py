#! python3
# ex16.py

import copy, datetime

class Time:
    '''A class to represent the time of day.'''
    def __init__(self, hour = 0, minute = 0, second = 0):
        self.hour = hour + (minute + second//60)//60
        self.minute = minute + second//60
        self.second = second % 60
        
    def increment(self, seconds):
        return int_to_time(self.time_to_int() + seconds)
        
    def time_to_int(self):
        return (self.hour*3600 + self.minute*60 + self.second)
    
    def __str__(self):
        return '%.2d : %.2d : %.2d'% (self.hour, self.minute, self.second)
        
    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)
        
    def __radd__(self, other):
        return self.__add__(other)

    def add_time(self, other):
        return int_to_time(self.time_to_int() + other.time_to_int())

    def mul_time(self, n):
        return int_to_time(self.time_to_int() * n)

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

    
        
        





    
def int_to_time(sec):
    time = Time()
    minutes, time.second = divmod(sec, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time





def avg_pace(dist, time):
    avg_time_req = mul_time(time, 1/dist)
    return avg_time_req

def next_birthday(date):
    today = datetime.date.today()
    date = datetime.date(today.year, date.month, date.day)
    if date > today:
        return date - today
    else:
        return datetime.date(date.year + 1, date.month, date.day) - today
    
def n_date(b_date_1, b_date_2, n = 2):
    '''Returns the date on which the person born on greater date is n times older than the other.'''
    b_early = min(b_date_1, b_date_2)
    b_late = max(b_date_1, b_date_2)
    difference = b_late - b_early
    time_req = difference/(n - 1)
    n_date = b_late + time_req
    return n_date

    
