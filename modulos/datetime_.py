# https://docs.python.org/2/library/datetime.html

from datetime import datetime, timedelta

data = datetime(2022, 8, 23)
# print(data.strftime('%d-%M-%Y'))

data2 = datetime.strptime('20/08/2022', '%d/%m/%Y')
print(data2.timestamp())

date3 = datetime.fromtimestamp(1660964400.0)
print(date3)

