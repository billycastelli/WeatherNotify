#Weather input

import wuApi
import wuTw

def getCity():
    city = input('Enter the name of a US city: ')
    return city

def getState():
    state = input('Enter the name of a US state: ')
    return state

def getPhone():
    phone = ''
    #while len(phone) != 10:
    #for now only my phone number will work because this program
    #uses the twilio free trial
    phone = input('Enter phone number (10 digits, include 1): ')
    return phone

if __name__ == "__main__":
    city = getCity()
    state = getState()
    phone = getPhone()
    twNum = '+18589265834'

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
        #print(date)
        #print(weatherDict[date])
        #print()
    wuTw.send(phone, twNum, todayDate + todayW + todayHiLow)
    
    #print(json)

   
    
