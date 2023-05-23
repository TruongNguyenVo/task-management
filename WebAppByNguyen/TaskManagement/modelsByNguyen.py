#hàm thì viết hoa chữ cái đầu
#biến thì viết thường
#class thì viết hoa hết

import psycopg2
import time
def delay(timeDelay):
	time.sleep(float(timeDelay))
def days_hours_minutes(td): # hiển thị về ngày giờ phút
    return td.days, td.seconds//3600, (td.seconds//60)%60
def munis(startDate, endDate): # trừ hai mốc thời gian gồm ngày tháng năm giờ phút giây
	startDate = startDate.replace(tzinfo=None)
	endDate = endDate.replace(tzinfo=None)
	return endDate - startDate

def connectDB():
	conn = psycopg2.connect(
		host = "localhost",
		database = "dbTaskManagement",
		user = "postgres",
		password = "1234"
		)
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM public."TaskManagement_taskcreation"')
	rows = cursor.fetchall()

	temp = []
	for row in rows:
		print(row[1])
		temp.append(row[1])
	cursor.close()
	conn.close()
	return temp

connectDB()