from datetime import datetime as dt
import datetime

kr_now = dt.now() + datetime.timedelta(hours=9)
print(kr_now.strftime('%Y-%m-%d'))