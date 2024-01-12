print()
# 1. show_id,type,title,director,cast,country,date_added,release_year,rating,duration,listed_in,description
# 2. Profile Name,Start Time,Duration,Attributes,Title,Supplemental Video Type,Device Type,Bookmark,Latest Bookmark,Country

# import libraries
import csv
import datetime
import matplotlib.pyplot as plt
import numpy as np

def remove_sq(s):
    n=""
    for i in s:
        if i not in ["'"]:
            n+=i
    return n

dates={}
duration_per_day={}     # So as to calculate max watch time, avg watch time
time={"00:00-03:00":0,"03:00-08:00":0,"08:00-12:00":0,"12:00-16:00":0,"16:00-20:00":0,"20:00-00:00":0}

# A sample row in reader_obj : <class 'list'> ['Aarya', '18/3/2021 14:53', '0:26:38', 'Prison Break: Season 1: Allen (Episode 2)', 'DefaultWidevineAndroidPhone', '0:28:01', 'Not latest view', 'IND (India)', 'Adventure']

#Printing pie chart which shows at which time of the day user prefers to watch
with open("Aarya_ViewingHistory.csv") as f:
    reader_obj=csv.reader(f)
    next(reader_obj,None)
    count=0
    for row in reader_obj:
        l=[int(s) for s in row[2].split(":")]
        start = datetime.time(l[0],l[1], 0)
        if datetime.time(3,0,0)<=start<datetime.time(8,0,0):
            time["03:00-08:00"]+=1
        elif datetime.time(8,0,0)<=start<datetime.time(12,0,0):
            time["08:00-12:00"]+=1
        elif datetime.time(12,0,0)<=start<datetime.time(16,0,0):
            time["12:00-16:00"]+=1
        elif datetime.time(16,0,0)<=start<datetime.time(20,0,0):
            time["16:00-20:00"]+=1
        elif datetime.time(20,0,0)<=start<datetime.time(23,59,59):
            time["20:00-00:00"]+=1
        elif datetime.time(0,0,0)<=start<datetime.time(3,0,0):
            time["00:00-03:00"]+=1
        count+=1
    y = np.array([time["03:00-08:00"],time["08:00-12:00"],time["12:00-16:00"],time["16:00-20:00"],time["20:00-00:00"],time["00:00-03:00"]])
    plt.pie(y,labels=time.keys())
    plt.title("Representation of a User Watching Netflix in a Particular Time Slot of the Day")
    plt.show()
    #print(time) # Dictionary containing Time v/s Frequency of user watching Netflix


# Making graphical representation for device usage
with open("Aarya_ViewingHistory.csv","r") as f:
    reader_obj=csv.reader(f)
    next(reader_obj,None)
    d={"DefaultWidevineAndroidPhone":0,"Chrome PC (Cadmium)":0,"DefaultWidevineAndroidTablets":0}
    l=[]
    for row in reader_obj:
        if row[5] not in l:
            l.append(row[5])
        if row[5]=="DefaultWidevineAndroidPhone":
            d["DefaultWidevineAndroidPhone"]+=1
        elif row[5]=="DefaultWidevineAndroidTablets":
            d["DefaultWidevineAndroidTablets"]+=1
        elif row[5]=="Chrome PC (Cadmium)":
            d["Chrome PC (Cadmium)"]+=1
    tot=d["DefaultWidevineAndroidPhone"]+d["DefaultWidevineAndroidTablets"]+d["Chrome PC (Cadmium)"]
    y = np.array([round(d["DefaultWidevineAndroidPhone"]*100/tot,0),round(d["DefaultWidevineAndroidTablets"]*100/tot,0),round(d["Chrome PC (Cadmium)"]*100/tot,0)])
    plt.pie(y,labels=d.keys())
    plt.title("Device Used For Watching Netflix")
    plt.show()

    
# Genre based results
with open("Aarya_ViewingHistory.csv") as f:
    reader_obj=csv.reader(f)
    next(reader_obj,None)
    count=0
    genre={'Historical':0, 'Adventure':0, 'Action':0, 'Fantasy':0, 'Crime':0, 'Romance':0, 'Comedy':0, 'Horror':0, 'Drama':0}
    for row in reader_obj:
        if row[-1] =="Historical":
            genre["Historical"]+=1
        elif row[-1] =="Adventure":
            genre["Adventure"]+=1
        elif row[-1] =="Action":
            genre["Action"]+=1
        elif row[-1] =="Fantasy":
            genre["Fantasy"]+=1
        elif row[-1] =="Crime":
            genre["Crime"]+=1
        elif row[-1] =="Romance":
            genre["Romance"]+=1
        elif row[-1] =="Comedy":
            genre["Comedy"]+=1
        elif row[-1] =="Horror":
            genre["Horror"]+=1
        elif row[-1] =="Drama":
            genre["Drama"]+=1
    
    print("Genre v/s No. Of Movies Watched Data :\n",genre)
    print("Your viewing trends w.r.t genre are graphically displayed as follows : \n")
    
    data=[genre["Historical"],genre["Adventure"],genre["Action"],genre["Fantasy"],genre["Crime"],genre["Romance"],genre["Comedy"],genre["Horror"],genre["Drama"]]
    x = np.array(['Historical', 'Adventure', 'Action', 'Fantasy', 'Crime', 'Romance', 'Comedy', 'Horror', 'Drama'])
    y = np.array([genre["Historical"],genre["Adventure"],genre["Action"],genre["Fantasy"],genre["Crime"],genre["Romance"],genre["Comedy"],genre["Horror"],genre["Drama"]])
    plt.title("No. of Movies Watched w.r.t a Particular Genre")
    plt.bar(x,y)
    plt.xlabel("Movie Genres")
    plt.ylabel("No. Of Movies Watched")
    plt.show()
    max=0
    g=""         # Most favourable Genre
    for i in genre:
        if genre[i]>max:
            g=i
    print(f"\nThe Genre Of Movies Which You Love To Watch is {g}.\n")


# Line Graph of day v/s time spent on watching Netflix
# Just to qualititatively show the user how varying his watch time is.
with open("Aarya_ViewingHistory.csv","r") as f:
    reader_obj=csv.reader(f)
    next(reader_obj,None)
    date={}
    for row in reader_obj:
        time=[int(i) for i in row[3].split(":")]
        if row[1] in date:
            time_change=datetime.timedelta(hours=time[0],minutes=(time[1]),seconds=(time[2]))
            date[row[1]]+=time_change
        else:
            dt=[int(i) for i in row[1].split("/")]
            date[row[1]]=datetime.datetime(dt[2],dt[1],dt[0],time[0],time[1],time[2])
    l=[]
    for k in date:
        durn=[int(i) for i in (str(date[k]).split(" ")[1]).split(":")]
        l.append(durn[0]*60+durn[1]+durn[2]/60)
    ypoints = np.array(l)
    plt.xlabel("Time Extent")
    plt.ylabel("Watch Time")
    plt.title(" Line Graph Representing A Qualitative Analysis Of How Variable the User's Watch Time Is w.r.t Time")
    plt.plot(ypoints, linestyle = 'dotted')
    plt.show()


#Recommmending Movies
with open("netflix_titles.csv","r") as f:
    reader_obj=csv.reader(f)
    next(reader_obj,None)
    recomm=[]
    for row in reader_obj:
        if row[-1]==g:
            recomm.append(", ".join((remove_sq(str(row[1:-1])[1:-1])).split(", ")))
    print("The Following Movies/Shows are Recommended to You on the Basis of Your Viewing Insights : \n")
    count=1
    for title in recomm:
        print(f"{count}. {title}\n")
        count+=1
        if count==6:
            break
