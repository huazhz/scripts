import os
import matplotlib.pyplot as plt
import datetime
import matplotlib as mpl
mpl.rcParams['pdf.fonttype'] = 42

startdate = datetime.date(year=2012,month=06,day=01)
numdays =61
dateList = []
for x in range(0,numdays):
    dateList.append(startdate +datetime.timedelta(days=x))

file = '/Users/home/matsonga/seisan/REA/NM76D/hypoDD10/hypoDD.reloc'

with open(file,'r') as fid:
    contents = fid.readlines()
eqRate = []
plotTimes = []
for line in contents:
    year=line.split()[10]
    month = '%02i' %int(line.split()[11])
    day = '%02i' %int(line.split()[12])
    hour= '%02i' %int(line.split()[13])
    minute = '%02i' %int(line.split()[14])
    second = '%2.3f' %float(line.split()[15])
    if line.split()[15].startswith('60.'):
        second = 59.9
    datetime1=datetime.datetime.strptime('%s/%s/%s %s:%s:%s'%(year,month,day,hour,minute,second),'%Y/%m/%d %H:%M:%S.%f')
    plotTimes.append(datetime1)

for i in range(0,len(dateList)):
    dayVector = filter(lambda x: x.month == dateList[i].month and x.day == dateList[i].day, plotTimes)
    eqRate.append(len(dayVector))

values = range(1,len(plotTimes)+1)
plotTimes.sort()
fig = plt.figure()
ax=fig.add_subplot(111)
ax.plot(plotTimes,values,lw = 3.0,color = 'm',label='Cumulative detections') # '#a6cee3' '#1f78b4'
ax.bar(dateList,eqRate,label='Detections per day',color='k')
fig.autofmt_xdate()
handles1,labels1 = ax.get_legend_handles_labels()


# file5 = 'NM10DrillingLoss.txt'
# fid5 = open(file5,'r')
# plotTimes5 = []
# flow5 = []
# cumInj5 = []
# for line in fid5:
#     time5 = line.split()[0]
#     print time5
#     date5 = line.split()[1]
#     datetime5 = datetime.datetime.strptime('%s %s' %(date5,time5),'%Y/%m/%d %H:%M')
#     datetime5 = datetime5 - datetime.timedelta(hours=12)
#     plotTimes5.append(datetime5)
#     flow5.append(float(line.split()[2]))
#     cumInj5.append(float(line.split()[3]))
# fid5.close()
# ax2=ax.twinx()
# ax2.plot(plotTimes5,flow5,'m',label='NM10 Fluid loss rate (t/hr)',linewidth = 3.0,alpha = 0.6)
# # ax2.plot(plotTimes5,cumInj5,'m',label='Cumulative Injected Vol (tonnes)',linewidth = 3.0,alpha = 0.6)
# handles2,labels2 = ax2.get_legend_handles_labels()
# handles = handles1+handles2
# labels = labels1+labels2
# ax.legend(handles,labels,loc=2,fontsize=14)
# ax.set_xlabel("Date",fontsize = 14)
# ax.set_ylabel(r"Number of Detections",fontsize = 14)
# ax2.set_ylabel(r"Fluid loss",color = 'm', fontsize = 14)
# ax.tick_params(axis = 'both',which='major'  ,labelsize = 14)
# ax2.tick_params(axis = 'both',which='major'  ,labelsize = 14)
# plt.show()
# #mCHF = metres below casing head flange
# # mRKB = meters relative to kelly-bushing


# file6 = 'NM8InjectivityIndex.txt'
# with open(file6,'r') as fid6:
#     contents6 = fid6.readlines()
# IIlist = []
# plotTimes6 = []
# for line in contents6:
#     date = line.split()[0]
#     datetime6 = datetime.datetime.strptime('%s 12:00' %date,'%m/%d/%Y %H:%M')
#     datetime6 = datetime6 - datetime.timedelta(hours=12)
#     plotTimes6.append(datetime6)
#     day = line.split()[1]
#     II = line.split()[2]
#     IIlist.append(II)
# ax2=ax.twinx()
# ax2.plot(plotTimes6,IIlist,'mo-',label='NM8 II (t/hr/bar)',markersize=4.0,markeredgewidth = 0,linewidth = 3.0,alpha = 0.6)
# #ax2.plot(plotTimes5,cumInj5,'m',label='Cumulative Injected Vol (tonnes)',linewidth = 3.0,alpha = 0.6)
# handles2,labels2 = ax2.get_legend_handles_labels()
# handles = handles1+handles2
# labels = labels1+labels2
# ax.legend(handles,labels,loc=2,fontsize=14)
# ax.set_xlabel("Date",fontsize = 14)
# ax.set_ylabel(r"Number of Detections",fontsize = 14)
# ax2.set_ylabel(r"Injectivity Index",color = 'm', fontsize = 14)
# ax.tick_params(axis = 'both',which='major'  ,labelsize = 14)
# ax2.tick_params(axis = 'both',which='major'  ,labelsize = 14)
# plt.show()



# file4 = '/Volumes/GeoPhysics_07/users-data/matsonga/MRP_PROJ/data/mastersData/productionData/NM08_WHP_3.csv'
# fileObject4 = open(file4,'r')
# plotTimes4 = []
# whp = []
# flow = []
# cumInj = []
# injectivity = []
# for line in fileObject4:
#     data4 = line.split(',')
#     time4 = data4[0]
#     datetime4 = datetime.datetime.strptime('%s' %time4,'%m/%d/%Y %H:%M')
#     datetime4 = datetime4 - datetime.timedelta(hours=12)
#     plotTimes4.append(datetime4)
#     whp.append(float(data4[1]))
#     flow.append(float(data4[2]))
#     cumInj.append(float(data4[3]))
#     if data4[4] == '#DIV/0!':
#         injectivity.append(0)
#     else:
#         injectivity.append(float(data4[4]))
# flow[len(flow)-1]=0.0
# whp.append(0.0)
# flow.append(0.0)
# plotTimes4.append(datetime.datetime.strptime('07/31/2012 23:59','%m/%d/%Y %H:%M'))
# cumInj.append(float(data4[3]))
# fileObject4.close()
# ax2=ax.twinx()
# # ax2.plot(plotTimes4,cumInj,'m',label='NM8 Cumulative Injected Vol (tonnes)',linewidth = 3.0,alpha = 0.6)
# ax2.plot(plotTimes4,flow,'m',label='NM8 Flow rate (t/hr)',linewidth = 3.0,alpha = 0.6)
# ax2.plot(plotTimes4,whp,'m',color='y',label='NM8 WHP (bar)',linewidth = 3.0,alpha = 0.6)
# #ax2.set_zorder(1)
# #ax.legend(loc=0)
# #ax2.legend(loc=0)
# handles2,labels2 = ax2.get_legend_handles_labels()
# handles = handles1+handles2
# labels = labels1+labels2
ax.legend(handles1,labels1,loc=2,fontsize=14)
# #ax.grid()
ax.set_xlabel("Date",fontsize = 14)
ax.set_ylabel(r"Number of Detections",fontsize = 14)
# # ax2.set_ylabel(r"Injected Fluid(tonnes)",color = 'm', fontsize = 14)
# ax2.set_ylabel(r"Injected Fluid",color = 'm', fontsize = 14)
# ax.tick_params(axis = 'both',which='major'  ,labelsize = 14)
# ax2.tick_params(axis = 'both',which='major'  ,labelsize = 14)
# # plt.title('%s Detections over ',fontsize=14)
# #labels = ax.get_xticklabels()
# #for label in labels:
# #    label.set_rotation(30)
#
# #fig.autofmt_xdate()
# #ax.xticks(rotation=70)
# # #plt.savefig('commonDetectionsFigs/forThesis/Thresh%s%s_CummDet_PerDay_CummInj.pdf' %(threshMult5,cluster1))
plt.show()
