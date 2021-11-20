
class Time(week, day, time):
    def __init__(self):
        days_of_the_week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        self.current_day = day
        self.current_week = week
        self.current_time = time

    def skip(self, minutes):
        current_time += minutes
        if current_time >= 1440:
            current_day += 1
            current_time = 0
            if current_day > 7:
                current_day = 1
    
    def readable(self):
        readable_time = 'Week {}, {}, {}:{}'.format(current_week, current_day, current_time%60, current_time//60)
        return readable_time

if __name__ == '__main__':
    run1 = Time(1, 1, 10)
    print(run1)