import pymysql

connection = pymysql.connect(
    host='172.16.5.81',
    user='hotel_user',
    password='Guest01',
    database='hotel_reservations',
    cursorclass=pymysql.cursors.DictCursor
)
