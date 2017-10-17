#wuServer

import wuApi
import wuTw
from apscheduler.schedulers.blocking import BlockingScheduler


city = 'Irvine'
state = 'California'
phone = '17607077076'
twNum = '+18589265834'

def job():
    url = wuApi.build_url(city,state)
    print(url)
    #url = wuApi.build_url('carlsbad','ca')
    json = wuApi.get_result(url)
    weatherDict = wuApi.parse(json)
    print()
    #print(weatherDict)
    for date in weatherDict.keys():
        conditions, high, low = weatherDict[date]
        todayDate = '\n \nToday is ' + date + '\n'
        todayW = "The weather today will be: "+ weatherDict[date][0]
        todayHiLow = "\nThe high will be " + high +" degrees. The low will be " + low + " degrees."
        break
    wuTw.send(phone, twNum, todayDate + todayW + todayHiLow)



if __name__ == "__main__":
    scheduler = BlockingScheduler()
    scheduler.add_job(job, 'cron', hour = 8, minute = 30)
    scheduler.start()

    

    

    
