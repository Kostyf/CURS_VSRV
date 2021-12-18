#подключаю нужные библиотеки
from smbus import SMBus
from bme280 import BME280
import time
import datetime
from datetime import date
from openpyxl import load_workbook

#инициализирую датчик BME280
bus = SMBus(1)
bme280 = BME280(i2c_dev=bus)

#считываю данные в первый раз, как мусорные
temperature = bme280.get_temperature()
pressure = bme280.get_pressure()
humidity = bme280.get_humidity()
time.sleep(1)	

#подгружаю табличку и выбираю её, для заполнения
wb = load_workbook('/home/pi/Python_Code/weather.xlsx')
sheet = wb['Табличка']

try:
	while True:
		
		#получаю информацию от датчиков и округляю
		temperature = round(bme280.get_temperature(),1)
		pressure = round(bme280.get_pressure(),1)
		humidity = round(bme280.get_humidity(),1)

		# информация для пользователя
		print('Заношу данные в табличку:')
		print('{}*C {}hPa {}%'.format(temperature, pressure, humidity))
	
		#Заношу данные в табличку
		row = (temperature, pressure, humidity)
		sheet.append(row)
		
		#сохраняю табличку
		wb.save('/home/pi/Python_Code/weather.xlsx')
		time.sleep(600)

finally:
	#сохраняю
	wb.save('/home/pi/Python_Code/weather.xlsx')
	
	print('До скорого использования :)')
	