#Weather input
import wuApi

def getCity():
    city = input('Enter the name of a US city: ')
    return city

def getState():
    state = input('Enter the name of a US state: ')
    return state

def getPhone():
    phone = ''
    while len(phone) != 10:
        phone = input('Enter phone number: ')
    return phone

if __name__ == "__main__":
    city = getCity()
    state = getState()
    #phone = getPhone()
    url = wuApi.build_url(city,state)
    #url = wuApi.build_url('carlsbad','ca')
    json = wuApi.get_result(url)
    weatherDict = wuApi.parse(json)
    print()
    for date in weatherDict.keys():
        print(date)
        print(weatherDict[date])
        print()
    #print(json)

    
    
