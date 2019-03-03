import server
import datetime
import requests
import pprint
pp = pprint.PrettyPrinter()

epoch = datetime.datetime.utcfromtimestamp(0)
now = datetime.datetime.now()


placesToVisit =  ["Claremont, CA", "Los Angeles, CA"]


print(epoch)
print(now)

totalTime = 5 * 60 * 60
startTime = int(now.timestamp())
print(now.timestamp())


# half an hour in seconds
timeBetweenMatrices = int(1 * 60 * 60)

# distance matrices, each some time constant apart
distanceMatrices = []

# get matrix for every 30 mins, starting now, ending sometime before endTime
for i in range(int(totalTime / timeBetweenMatrices) + 1):
    print(startTime + timeBetweenMatrices * i)
    distanceMatrices.append(server.getTimeDelimitedMatricesFromGoogle( \
        startTime + timeBetweenMatrices * i, placesToVisit))

pp.pprint(distanceMatrices)
