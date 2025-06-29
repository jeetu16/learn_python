from datetime import datetime
import time

dt = datetime(2025, 6, 29)
currDt = datetime.now()
strpDt = datetime.strptime("2025/06/29", "%Y/%m/%d")
timeStampsDt = datetime.fromtimestamp(time.time())
print(dt)
print(f"{dt.year}/{dt.month}")
print(dt.strftime("%Y/%m"))
print(currDt)
print(strpDt)
print(timeStampsDt)

print(currDt > dt)
