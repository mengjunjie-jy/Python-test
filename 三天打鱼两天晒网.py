try:
    Date = int(input('请输入日期(请以yyyymmdd输入):'))
    date = list(str(Date))

    try:
        if len(date) != 8:
            print("输入日期有误！")
        global year
        year = date[0] + date[1] + date[2] + date[3]
        year = int(year)
        month = date[4] + date[5]
        month = int(month)
        day = date[6] + date[7]
        day = int(day)

        if year < 1990:
            print("请输入正确的日期！")

        # 判断是不是闰年
        def runYear(year):
            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                return True
            else:
                return False

        # 判断每月有几天
        def getDays(year, month):
            days = 0
            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                days = 31
            elif month == 4 or month == 6 or month == 9 or month == 11:
                days = 30
            elif month == 2:
                if runYear(year):
                    days = 29
                else:
                    days = 28
            return days

        # 计算该日期本年总天数
        def thisYearDays(year, month, day):
            sum = 0
            i = 1
            while i < month:
                monthDay = getDays(year, month)
                sum += monthDay
                i += 1
            return sum + day

        # 计算距离输入日期的总天数
        def allDays(year, month, day):
            sum = 0
            i = 1990
            while i < year:
                if runYear(i):
                    sum += 366
                else:
                    sum += 365
                i += 1
            s = thisYearDays(year, month, day)
            sum += s
            return sum


        # 判断是捕鱼还是晒网
        def judge(days):
            x =days % 5
            if x >= 1 and x <= 3:  # 当余数为1/2/3时为打鱼，余数为0/4时候为晒网
                print("今天打鱼")
            else:
                print("今天晒网")

        sum = allDays(year, month, day)
        judge(sum)

    except IndexError:
        print("请输入八位整数")
except ValueError:
    print("请输入整数！")


