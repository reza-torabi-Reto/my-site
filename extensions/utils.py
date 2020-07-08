from . import jalali

def persian_numbers_converter(mystr):
    numbers = {
        "1":"۱",
        "2":"۲",
        "3":"۳",
        "4":"۴",
        "5":"۵ ",
        "6":"۶",
        "7":"۷",
        "8":"۸",
        "9":"۹",
        "0":"۰",
    }
    for e, p in numbers.items():
        mystr = mystr.replace(e, p)
    return mystr

def peersian_time(tm):
    return persian_numbers_converter("{}:{}".format(tm.hour, tm.minute))
    # return "{}:{}".format(tm.hour, tm.minute)


def jalali_convert(time):
    jmounts= [
    'فروردین',
    'اردیبهشت',
    'خرداد',
    'تیر',
    'اَمرداد',
    'شهریور',
    'مهر',
    'آبان',
    'آذر',
    'دی',
    'بهمن',
    'اسفند'
    ]
    time_to_str = "{},{},{}".format(time.year, time.month, time.day)
    time_to_tuple = jalali.Gregorian(time_to_str).persian_tuple()

    time_to_list = list(time_to_tuple)

    for index, month in enumerate(jmounts):
        if time_to_list[1] == index + 1:
            time_to_list[1] = month
            break
    
    output = persian_numbers_converter("{} {} {}".format(
        time_to_list[2],
        time_to_list[1],
        time_to_list[0]
    ))
    return output