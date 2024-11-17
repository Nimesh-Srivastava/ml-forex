from functools import reduce
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np
import time

# Name of file
filename = 'GBPUSD1d.txt'

date, bid, ask = np.loadtxt(filename, unpack=True, delimiter=',', converters={0: lambda x: mdates.datestr2num(x)})
avgLine = ((bid + ask) / 2)

patternArr = []
performanceArr = []

def percentChange(startPoint, currentPoint):
    return ((float(currentPoint) - startPoint)/abs(startPoint)) * 100.0

def patternStorage():
    patStartTime = time.time()
    x = len(avgLine) - 30

    y = 11
    while y < x:
        pattern = []
        p1 = percentChange(avgLine[y - 10], avgLine[y - 9])
        p2 = percentChange(avgLine[y - 10], avgLine[y - 8])
        p3 = percentChange(avgLine[y - 10], avgLine[y - 7])
        p4 = percentChange(avgLine[y - 10], avgLine[y - 6])
        p5 = percentChange(avgLine[y - 10], avgLine[y - 5])
        p6 = percentChange(avgLine[y - 10], avgLine[y - 4])
        p7 = percentChange(avgLine[y - 10], avgLine[y - 3])
        p8 = percentChange(avgLine[y - 10], avgLine[y - 2])
        p9 = percentChange(avgLine[y - 10], avgLine[y - 1])
        p10 = percentChange(avgLine[y - 10], avgLine[y])

        outcomeRange = avgLine[y + 20 : y + 30]
        currentPoint = avgLine[y]

        try:
            avgOutcome = (reduce(lambda x, y : x + y, outcomeRange) / len(outcomeRange))
        except:
            print("Exception triggered")
            avgOutcome = 0

        futureOutcome = percentChange(currentPoint, avgOutcome)
        
        pattern.append(p1)
        pattern.append(p2)
        pattern.append(p3)
        pattern.append(p4)
        pattern.append(p5)
        pattern.append(p6)
        pattern.append(p7)
        pattern.append(p8)
        pattern.append(p9)
        pattern.append(p10)
        
        patternArr.append(pattern)
        performanceArr.append(futureOutcome)

        y += 1
    
    patEndTime = time.time()
    print (len(patternArr))
    print (len(performanceArr))
    print('Pattern storage took : ', patEndTime - patStartTime, ' seconds')

def patternRecognition():
    patForRec = []

    currPatt_1 = percentChange(avgLine[-11], avgLine[-10])
    currPatt_2 = percentChange(avgLine[-11], avgLine[-9])
    currPatt_3 = percentChange(avgLine[-11], avgLine[-8])
    currPatt_4 = percentChange(avgLine[-11], avgLine[-7])
    currPatt_5 = percentChange(avgLine[-11], avgLine[-6])
    currPatt_6 = percentChange(avgLine[-11], avgLine[-5])
    currPatt_7 = percentChange(avgLine[-11], avgLine[-4])
    currPatt_8 = percentChange(avgLine[-11], avgLine[-3])
    currPatt_9 = percentChange(avgLine[-11], avgLine[-2])
    currPatt_10 = percentChange(avgLine[-11], avgLine[-1])

    patForRec.append(currPatt_1)
    patForRec.append(currPatt_2)
    patForRec.append(currPatt_3)
    patForRec.append(currPatt_4)
    patForRec.append(currPatt_5)
    patForRec.append(currPatt_6)
    patForRec.append(currPatt_7)
    patForRec.append(currPatt_8)
    patForRec.append(currPatt_9)
    patForRec.append(currPatt_10)

    print(patForRec)

def graphRawFX():
    fig = plt.figure(figsize = (10, 7))
    ax1 = plt.subplot2grid((40, 40), (0, 0), rowspan = 40, colspan = 40)

    ax1.plot(date, bid)
    ax1.plot(date, ask)

    plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)

    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y %H:%M:%S'))
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)

    ax1_2 = ax1.twinx()
    ax1_2.fill_between(date, 0, (ask-bid), facecolor='g', alpha=0.3)

    plt.subplots_adjust(bottom=0.23)

    plt.grid(True)
    plt.show()

# graphRawFX()
# patternStorage()
patternRecognition()