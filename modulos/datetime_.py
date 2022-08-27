# https://docs.python.org/2/library/datetime.html

from datetime import datetime, timedelta, date

data = datetime.today()
#print(data)

data1 = date.today()
#print(data1)

# print(data.strftime('%d-%M-%Y'))

data2 = datetime.strptime('20/08/2022', '%d/%m/%Y')
data3 = datetime.strptime('21/08/2022', '%d/%m/%Y')
resultado = data2 + timedelta()
print(data1 + timedelta(hours=0,  minutes=0, seconds=0, weeks=4))




date3 = datetime.fromtimestamp(1660964400.0)
#print(date3)


