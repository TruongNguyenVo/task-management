#hàm thì viết hoa chữ cái đầu
#biến thì viết thường
#class thì viết hoa hết
def days_hours_minutes(td):
    return td.days, td.seconds//3600, (td.seconds//60)%60
def munis(startDate, endDate):
	return endDate - startDate