#hàm thì viết hoa chữ cái đầu
#biến thì viết thường
#class thì viết hoa hết

import psycopg2
import time
from datetime import datetime, timedelta
import requests
import json
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

# connectDB()
def fiveDayAfter():
	return datetime.now() + timedelta(days=5)

#hàm lấy thời tiết
def getWeather(day = None, time = None,location = None):
	try:
		code_country = {
			'CanTho' : '352508',
			'VinhLong' : '356354'
		}
		apikey = 'RB3TP3Vkbv7d1Qa5cwOpYWSxAHcb0BlD'

		url_days = 'https://dataservice.accuweather.com/forecasts/v1/daily/1day/'+ code_country['CanTho'] +'?language=vi&apikey=' + apikey
		#url_hours = 'https://dataservice.accuweather.com/forecasts/v1/hourly/1hour/' + code_country['CanTho'] + '?language=vi&apikey=' + apikey
		res = requests.get(url_days).json()
		
		dataDay = {
			'Advice' : res['Headline']['Text'], # Nguy hiểm mất nước và sốc nhiệt nếu ở ngoài trời trong khoảng thời gian dài Thứ 5
			'Date' : res['DailyForecasts'][0]['Date'], # 2023-06-07T07:00:00+05:30
			
			# Nhiệt độ F
			'MaxF' : res['DailyForecasts'][0]['Temperature']['Minimum']['Value'], # 79.0
			'MinF' : res['DailyForecasts'][0]['Temperature']['Maximum']['Value'], # 104.0
			# Dự báo kiểu thời tiết

			'Day' : res['DailyForecasts'][0]['Day']['IconPhrase'], # Nắng có sương mờ
			'Night': res['DailyForecasts'][0]['Night']['IconPhrase'], # Quang mây
		}
		return {
			'status' : True,
			'data' : dataDay
			}
	except Exception as error:
		return {
			'status' : False,
			'data' : error,
		}


# hàm lấy mức độ giao thông
def getTraffic(day, time, location = None):
	pass

