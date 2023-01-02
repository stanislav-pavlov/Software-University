class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        return f"{self.hours}:{self.minutes}:{self.seconds}"

    def get_time(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def next_second(self):    # 10 : 59 : 59
        self.seconds += 1
        if self.seconds > Time.max_seconds: # 59 + 1 = 60   TRUE
            self.seconds = 0
            self.minutes += 1  # 10 :
            if self.minutes + 1 > Time.max_minutes:
                self.minutes = 0
                self.hours += 1
                if self.hours + 1 > Time.max_hours:
                    self.hours = 0

        return Time.get_time(self)


time = Time(23, 59, 59)
print(time.next_second())

