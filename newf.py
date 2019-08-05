from datetime import datetime
import requests

print("this is a test")

zocationServerActive = 1
lsShowTrainsExplicit = 1
stateless = 1
language = 'de'
SpEncId = 0
anySigWhenPerfectNoOtherMatches = 1
# max amount of arrivals to be returned
limit = 100
depArr = 'departure'
type_dm = 'any'
anyObjFilter_dm = 2
deleteAssignedStops = 1
name_dm = '5000002'
mode = 'direct'
dmLineSelectionAll = 1
useRealtime = 1
outputFormat = 'json'
coordOutputFormat = 'WGS84[DD.ddddd]'

url = 'http://www2.vvs.de/vvs/widget/XML_DM_REQUEST?'
url += 'zocationServerActive={:d}'.format(zocationServerActive)
url += '&lsShowTrainsExplicit{:d}'.format(lsShowTrainsExplicit)
url += '&stateless={:d}'.format(stateless)
url += '&language={}'.format(language)
url += '&SpEncId={:d}'.format(SpEncId)
url += '&anySigWhenPerfectNoOtherMatches={:d}'.format(
    anySigWhenPerfectNoOtherMatches
)
url += '&limit={:d}'.format(limit)
url += '&depArr={}'.format(depArr)
url += '&type_dm={}'.format(type_dm)
url += '&anyObjFilter_dm={:d}'.format(anyObjFilter_dm)
url += '&deleteAssignedStops={:d}'.format(deleteAssignedStops)
url += '&name_dm={}'.format(name_dm)
url += '&mode={}'.format(mode)
url += '&dmLineSelectionAll={:d}'.format(dmLineSelectionAll)

url += ('&itdDateYear={0:%Y}&itdDateMonth={0:%m}&itdDateDay={0:%d}' +
        '&itdTimeHour={0:%H}&itdTimeMinute={0:%M}').format(datetime.now())

url += '&useRealtime={:d}'.format(useRealtime)
url += '&outputFormat={}'.format(outputFormat)
url += '&coordOutputFormat={}'.format(coordOutputFormat)

r = requests.get(url)
r.encoding = 'UTF-8'
efa = r.json()

print(url)
#print(efa)

parsedDepartures = []

if not efa or "departureList" not in efa or not efa["departureList"]:
    #return parsedDepartures
    print("error")

for departure in efa["departureList"]:
    stopName = departure["stopName"]
    latlon = departure['y'] + "," + departure['x']
    number = departure["servingLine"]["number"]
    direction = departure["servingLine"]["direction"]

    if "realDateTime" in departure:
        realDateTime = departure["realDateTime"]
    elif "dateTime" in departure:
        realDateTime = departure["dateTime"]
    else:
        realDateTime = None

    if "dateTime" in departure and "realDateTime" in departure:
        dateTimeDatetime = datetime(
            year=int(departure["dateTime"]["year"]),
            month=int(departure["dateTime"]["month"]),
            day=int(departure["dateTime"]["day"]),
            hour=int(departure["dateTime"]["hour"]),
            minute=int(departure["dateTime"]["minute"]),
        )
        realDateTimeDatetime = datetime(
            year=int(departure["realDateTime"]["year"]),
            month=int(departure["realDateTime"]["month"]),
            day=int(departure["realDateTime"]["day"]),
            hour=int(departure["realDateTime"]["hour"]),
            minute=int(departure["realDateTime"]["minute"]),
        )
        timeDelta = realDateTimeDatetime - dateTimeDatetime
        delay = int(timeDelta.total_seconds()/60)
    else:
        delay = 0

    departureObject = {
        "stopName": stopName,
        "number": number,
        "direction": direction,
        "departureTime": realDateTime,
        "delay": delay,
        "stationCoordinates": latlon
    }

parsedDepartures.append(departureObject)

print(parsedDepartures)
