from datetime import time
some_time = time(10, 35)
fmt = "日期是 %B, %d, %Y,時間是 %I:%M:%S%p"
some_time.strftime(fmt)

print(fmt)
'日期是 January, 01, 1900,時間是 10:35:00AM'