from travel_func import getStopListCity, calcTravelTimes

# get all the stops in City 5111 (Bochum)
stopList = getStopListCity(5911)

# set start stop to which travel times shall be calculated: Bochum Hbf
# get value out of dictionary
start = "Hbf"
for stopID, name in stopList.items():
    if name == start:
        startStopID = stopID
        print(startStopID)

# calculate all travel times
travel_t = calcTravelTimes(startStopID)

# next steps:
# generate a complete list of all stops in NRW
# calculate travel times from all items in list to startStopID
