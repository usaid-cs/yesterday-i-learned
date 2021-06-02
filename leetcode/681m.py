def nextClosestTime(input_time):
    def get_digits(time):
        return (
            int(time[0]),
            int(time[1]),
            int(time[3]),
            int(time[4]))

    def is_valid_time(time):
        hour = time[0] * 10 + time[1]
        if hour > 23:
            return False
        minute = time[2] * 10 + time[3]
        if minute > 59:
            return False
        return True

    def time_diff(time1, time2):
        time1_abs = (time1[0] * 10 + time1[1]) * 60 + time1[2] * 10 + time1[3]
        time2_abs = (time2[0] * 10 + time2[1]) * 60 + time2[2] * 10 + time2[3]
        if time1_abs <= time2_abs:
            return time2_abs - time1_abs
        time2_abs += 24 * 60  # Minutes
        return time2_abs - time1_abs

    current_diff = float('inf')
    closest_time = None
    input_time_digits = get_digits(input_time)
    for char1 in input_time_digits:
        for char2 in input_time_digits:
            for char3 in input_time_digits:
                for char4 in input_time_digits:
                    permute_time_digits = (char1, char2, char3, char4)
                    if is_valid_time(permute_time_digits):
                        diff = time_diff(input_time_digits, permute_time_digits)
                        if diff == 0:
                            continue
                        if diff < current_diff:
                            closest_time = permute_time_digits
                            current_diff = diff
    return '%s%s:%s%s' % closest_time


print(nextClosestTime('19:34'))
print(nextClosestTime('23:59'))
