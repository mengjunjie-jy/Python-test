import datetime

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
# 将获取到的datetime对象仅取日期
yesterdaytime = yesterday.strftime("%Y-%m-%d")

print(today)  # 2020-04-02
print(yesterday)  # 2020-04-01
print(yesterdaytime)  # 2020-04-01
