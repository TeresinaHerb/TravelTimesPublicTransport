import csv
import requests
from xml.etree import ElementTree

def calcTravelTimes(stopID):
    travel_times = {}
    return travel_times

def getStopListCity(cityID):
    stopList = {}
    # send request to EFA Backend with cityID
    url = 'https://openservice-test.vrr.de/static02/XML_STOPLIST_REQUEST?'
    url += 'stopListOMC={:d}'.format(cityID)
    url += '000'

    print(url)
    # send out request
    r = requests.get(url)
    efa = ElementTree.fromstring(r.content)

    # print all the stop ids and name of stops retrieved fpr defined cityID
    for child in efa.iter('odvNameElem'):
        #print(child.attrib.get('stopID'), child.text)
        stopList[child.attrib.get('stopID')] = child.text
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
