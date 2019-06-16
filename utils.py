import csv

def getStopListCity(cityID):
    # send request to EFA Backend with cityID
    url = 'https://openservice-test.vrr.de/static02/XML_STOPLIST_REQUEST?'
    url += 'stopListOMC={:d}'.format(cityID)
    url += '000'

    print(url)
    # send out request
    r = requests.get(url)
    r.encoding = 'UTF-8'
    efa = r.json()

    # parse request

   return stopList


def getStopListNRW(path='/TravelTimesPublicTransport/mainStops.csv'):
    stopListNRW = {}
    # read csv and request line by line
    with open(path, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        # set up new dictionaries for results
        # key: efaID, value: stop name
        for row in reader:
            cityStops = {}
            cityID = row[0]
            cityStops = getStopListCity(cityID)
            stopListNRW.update(cityStops)
    return stopListNRW
