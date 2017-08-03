import urllib
import json
from matplotlib import pyplot as ptl
fhand=urllib.urlopen("http://climatedataapi.worldbank.org/climateweb/rest/v1/country/annualavg/tas/1980/1999/IND")
info=json.load(fhand)
fromYear=info[0]["fromYear"]
AVG_annual=[]
length=len(info)
Years=[]
for p in range(length):
    Years.append(fromYear+p)
    AVG_annual=info[p]["annualData"]+AVG_annual
ptl.plot(Years,AVG_annual)
ptl.show()
