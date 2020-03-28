# -*- coding: utf-8 -*-
from time import *
from datetime import *
from calendar import *
import math

# time()　　　　——　　返回当前时间戳，浮点数形式，不接受参数。
#
# gmtime()　　 ——　　将时间戳转换为UTC时间，元组形式，接受一个浮点型时间戳参数，默认值为当前时间戳。
#
# localtime()　　——　　将时间戳转换为本地时间，元组形式，接受一个浮点型时间戳参数，默认值为当前时间戳。
#
# ctime()　　　　——　　将时间戳转换为指定的字符串形式，接受一个浮点型时间戳参数，默认值为当前时间戳。
#
# actime()　　　——　　将时间元组格式转换为指定字符串形式，接受一个元组参数，默认值为localtime()返回值。
#
# mktime()　　　——　　将本地时间元组转换为时间戳，接受一个元组参数，必选。
#
# strftime()　　 ——　　将时间元组以指定的格式转换为字符串形式，接受格式化字符串、时间元组，时间元组参数可选，默认为localtime()。
#
# strptime()　　——　　将指定格式的时间字符串解析为时间元组，接受格式化字符串、字符串形式的时间，两个参数均为必选。
#
# sleep()　　　　——　　延迟指定时间，接受整型、浮点型，单位为秒。


# strftime()　　 ——　　将时间元组以指定的格式转换为字符串形式，接受格式化字符串、时间元组，时间元组参数可选，默认为localtime()。
val_date_num='20200331'

local_time=datetime.strptime(val_date_num[0:6]+'01','%Y%m%d')+timedelta(days=-1)



def add_months(datamonth, num):
    months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    date=datetime.strptime(datamonth,'%Y%m%d')
    year=date.year
    day=date.day
    datamonth = int(datamonth)
    datamonth_str=int(str(datamonth)[0:6])
    num = int(num)
    new_list = []
    s = math.ceil(abs(num) / 12)
    for i in range(int(-s), s + 1):
        new_list += [str(year + i) + x for x in months]
    new_list = [int(x) for x in new_list]
    year_new=str(new_list[new_list.index(datamonth_str) + num])[0:4]
    month_new=str(new_list[new_list.index(datamonth_str) + num])[4:6]
    monthRange = monthrange(int(year_new), int(month_new))[1]
    day_new=day
    if day>monthRange:
        day_new=monthRange
    return f'{year_new}{month_new}{day_new}'



aa=add_months(val_date_num,-1)
print(aa)
















# 1. calendar.calendar(year, w=2, l=1, c=6, m=3)
# 　　返回一个多行字符串格式的year年年历。


#
# 2. calendar.firstweekday()
# 　　返回当前每周起始日期的设置。默认返回0，即星期一。

print(isleap(year=2020))
# 3. calendar.isleap(year)
# 　　闰年返回True，否则False。
#
# 4. calendar.leapdays(y1, y2)
# 　　返回y1到y2之间的闰年总数，包含y1，不包含y2。
#
# 5. calendar.month(year, month, w=2, l=1)
# 　　返回一个多行字符串格式的year年month月日历。
#
# 6. calendar.monthcalendar(year,month)
# 　　返回一个整数的单层嵌套列表。每个子列表装载一个星期。该月之外的日期都为0，该月之内的日期设为该日的日期，从1开始。
#
# 7. calendar.monthrange(year, month)
# 　　返回两个整数组成的元组，第一个是该月的第一天是星期几，第二个是该月的天数。（calendar.monthrange(year, month)：
# 　　Returns weekday of first day of the month and number of days in month, for the specified year and month.——Python文档）
# 　　ps：此处计算星期几是按照星期一为0计算。
#
# 8. calendar.prcal(year, w=2, l=1, c=6)
# 　　等于print calendar.calendar(year)
#
# 9. calendar.prmonth(year, month)
# 　　同上。
#
# 10. calendar.setfirstweekday(weekday)
# 　　设置每周起始日期码。0（星期一）到6（星期日）
#
# 11. calendar.timegm(tupletime)
# 　　和time.gmtime相反，接收一个时间元组，返回该时刻的时间戳（计算机元年之后的秒数）
#
# 12. calendar.weekday(year, month, day)
# 　　返回给定日期的星期码，0（星期一）到6（星期日）。


