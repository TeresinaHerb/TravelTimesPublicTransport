# Travel Times Public Transport

Small private project on evaluating travel times between two stops within NRW

## Useful documentation and other sample projects

### OpenAPI

[VRR](https://www.vrr.de/de/service/opendataportal/)
[Bahn]()

### Generic reference to documentation of EFA API

Download Link for [Specification](https://wolke.vrr.de/node_share_links/448?token=a6404017-ade6-4d38-886b-df349f552349)

## Project documentation

### StopFind_Request

List of all GKZ which are needed to request the list of stops:
https://wiki.openstreetmap.org/wiki/VRR/Zusammenarbeit

All GKZ entries from the table of the website above need to be combined with `000` resulting in the parameter stopListOMC=GKZ+`000`

Sample request for Remscheid: https://openservice-test.vrr.de/static02/XML_STOPLIST_REQUEST?stopListOMC=05120000

### TravelTimesPublicTransport
Find out travel times between stops and visualize them
https://openservice-test.vrr.de/static02/XML_TRIP_REQUEST2?requestID=12827&locationServerActive=1&name_origin=80001611&type_origin=stopID&name_destination=80000066&type_destination=stopID&stateless=1&itdTripDateTimeDepArr=dep&calcOneDirection=1&useRealtime=1&itdDate=20190613&itdTime=22:00&outputFormat=XML&language=de

