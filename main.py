from travel_func import getStopListCity, calcTravelTimes, getStopListNRW

path = '/workspace/TravelTimesPublicTransport/mainStops.csv'
stopListNRW = getStopListNRW(path)
#print(stopListNRW)

# get all the stops in City 5111 (Bochum)
stopList1 = getStopListCity(5911)

# set start stop to which travel times shall be calculated: Bochum Hbf
# get value out of dictionary
start = "Hbf"
for stopID, name in stopList1.items():
    if name == start:
        startStopID = stopID
        print(startStopID)

# calculate travel times for big cities
dateV = '20190909'
timeV = '06:00'
#print(len(stopList1))
#travelT = calcTravelTimes(startStopID, dateV, timeV)

# next steps:
# generate a complete list of all stops in NRW
# calculate travel times from all items in list to startStopID
