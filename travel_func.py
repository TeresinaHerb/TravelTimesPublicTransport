import csv
import requests
from xml.etree import ElementTree

stopList = {}

def calcTravelTimes(stopID, dateV, timeV):
    travel_times = {}
    for startID, name in stopList.items():
        url = 'https://openservice-test.vrr.de/static02/XML_TRIP_REQUEST2?requestID=12827&locationServerActive=1'
        url += '&name_origin=' + startID + '&type_origin=stopID'
        url += '&name_destination=' + stopID + '&type_destination=stopID'
        url += '&stateless=1&itdTripDateTimeDepArr=dep&calcOneDirection=1&useRealtime=1'
        url += '&itdDate=' + dateV
        url += '&itdTime=' + timeV
        url += '&outputFormat=XML&language=de'

        # send out request
        r = requests.get(url)
        efa = ElementTree.fromstring(r.content)
        print(efa)
        # print the travelTimes
        #for child in efa.iter('publicDuration'):
            #print(child)
            #print(child.attrib.get('stopID'), child.text)
            #stopList[child.attrib.get('stopID')] = child.text
    return travel_times

def getStopListCity(cityID):
    global stopList
    stopList= {}
    # send request to EFA Backend with cityID
    url = 'https://openservice-test.vrr.de/static02/XML_STOPLIST_REQUEST?'
    url += 'stopListOMC=' + str(cityID)
    url += '000'
    #print(url)

    # send out request
    r = requests.get(url)
    efa = ElementTree.fromstring(r.content)

    # print all the stop ids and name of stops retrieved fpr defined cityID
    for child in efa.iter('odvNameElem'):
        #print(child.attrib.get('stopID'), child.text)
        stopList[child.attrib.get('stopID')] = child.text
    return stopList

def getStopListNRW(path):
    stopListNRW = {}
    # read csv and request line by line
    with open(path, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        # set up new dictionaries for results
        # key: efaID, value: stop name
        for row in reader:
            temp = row[0].split(";")
            cityID = temp[0]
            #city = temp[1]
            #stopListNRW[cityID] = city
            stopList_temp = getStopListCity(cityID)
            if len(stopList_temp) == 0:
                print(temp[1])
            else:
                stopListNRW.update(stopList_temp)
                print(len(stopListNRW))
    return stopListNRW
