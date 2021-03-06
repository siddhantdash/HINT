import urllib
from bs4 import BeautifulSoup
import datetime
def StartTime_DateTime_Conveter(string):
    raw_date,raw_time = string.strip().split("at")
    date,month,year = raw_date.strip().split(",")
    if len(date)==3:
        date = "".join(("0",date[0]))
    else:
        date = date[:2]
    dt = "-".join((date,month,year))
    final = " ".join((dt,raw_time))
    return datetime.datetime.strptime(final,"%d- %b- %Y  %I:%M %p")

def ReachTime_DateTime_Conveter(string):
    raw_time,raw_date = string.strip().split("on")
    date,month= raw_date.strip().split(",")
    year = "2017"
    if len(date)==3:
        date = "".join(("0",date[0]))
    else:
        date = date[:2]
    dt = "-".join((date,month,year))
    final = " ".join((dt,raw_time))
    return datetime.datetime.strptime(final,"%d- %b-%Y %I:%M %p ")


def Create_DataFile(train_no):
    data_file = file("data.csv","w")
    f = urllib.urlopen("http://runningstatus.in/history/"+str(train_no)+"/thisyear")
    soup = BeautifulSoup(f,"html.parser")
    table = soup.body.table
    l = table.get_text().split("\n")
    if l == [u'', u'', u'', u'Started On', u'Status', u'Delay', u'Reach Time', u'', u'', u'', u'Data Not Available!']:
        raise ValueError
    try:
        while(1):
            l.remove("")
    except:
        pass
    start = l[:4]
    mid = l[4:-4]
    data_file.write(",".join(start))
    data_file.write("\n")
    for i in xrange(0,len(mid),4):
        start,status,delay,reach= mid[i:i+4]
        data_file.write(",".join((str(StartTime_DateTime_Conveter(start)),status,delay,str(ReachTime_DateTime_Conveter(reach)))))
        data_file.write("\n")
    data_file.close()

if __name__=="__main__":
    Create_DataFile(15160)