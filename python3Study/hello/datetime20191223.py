# Python处理日期时间

import datetime, time
from dateutil.relativedelta import relativedelta

def test02():
    """
    参考： https://www.cnblogs.com/xrszff/p/10960132.html
    """
    _now = datetime.datetime.now()
    print(_now) # 2019-12-23 22:58:22.869218
    ans_time = time.mktime(_now.timetuple())
    print(ans_time) # 1577113102.0
    # -------------
    # time_str = 'Wed May 09 00:00:00 CST 2018'
    # # dt = datetime.datetime.strptime(time_str, "%a %b %d %X %Z %Y")
    # dt = datetime.datetime.strptime(time_str, "%a %b %d %H:%M:%S %Z %Y")
    # print(dt)
    a = '2018-10-03 00:55:00'
    b = datetime.datetime.strptime(a, '%Y-%m-%d %H:%M:%S').strftime('%m-%d')
    print(b)
    # ---
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    print(yesterday)
    # ---
    tmp_time = datetime.date(2018, 7, 20)
    _month = tmp_time.month
    _year = tmp_time.year
    print(_month)
    print(_year)
    # ---
    first_day_this_month = today.replace(day=1)
    print(first_day_this_month)
    last_month = first_day_this_month - datetime.timedelta(days=1)
    print(last_month)
    # 得到下个月的同一日
    next_month_same_day = today + relativedelta(months=1)
    print(next_month_same_day)


def test01():
    """
    参考： https://blog.csdn.net/ruguowoshiyu/article/details/80599288
    """
    from time import strftime, localtime
    print(strftime('%Y-%m-%d %H:%M:%S', localtime()))

def main():
    # test01()
    test02()

if __name__ == '__main__':
    main()