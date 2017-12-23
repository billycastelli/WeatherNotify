#wuServer

import wuApi
import wuTw
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import date

city = 'Irvine'
state = 'California'
phone = '17607077076'
twNum = '+17609744094'

def today(year, month, day):
    string = ""
    string = month + " " + str(day) + ", " + str(year)
    return string

def job():
    url = wuApi.build_url(city,state)
    print(url)
    #url = wuApi.build_url('carlsbad','ca')
    json = wuApi.get_result(url)
    weatherDict = wuApi.parse(json)
    print()
    #print(weatherDict)
    todayDate = today(date.today().year, date.today().strftime("%B"), date.today().day)
    conditions, high, low = weatherDict[todayDate]
    dateMessage = '\n \nToday is ' + todayDate + '\n'
    weatherMessage = "The weather today will be: "+ weatherDict[todayDate][0]
    tempsMessage = "\nThe high will be " + high +" degrees. The low will be " + low + " degrees."    
    wuTw.send(phone, twNum, dateMessage + weatherMessage + tempsMessage)

if __name__ == "__main__":
    scheduler = BlockingScheduler()
    scheduler.add_job(job, 'cron', hour = 15, minute = 52)
    scheduler.start()
