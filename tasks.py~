import string
import urllib2

from celery import Celery

app = Celery('tasks', backend='amqp', broker='amqp://')

@app.task
def wordcount(adress):

#Initate needed variables
    occur = [0,0,0,0,0,0,0,0,0]
    process = [0,0,0,0,0,0,0,0,0]

    
#Search for occurances of different words
    for line in urllib2.urlopen(adress):
        process[0] = process[0] + string.count(line, 'han')
        process[1] = process[1] + string.count(line, 'hon')
        process[2] = process[2] + string.count(line, 'den')
        process[3] = process[3] + string.count(line, 'det')
        process[4] = process[4] + string.count(line, 'denna')
        process[5] = process[5] + string.count(line, 'denne')
        process[6] = process[6] + string.count(line, 'hen')
        process[7] = process[7] + string.count(line, '"retweeted":false')
        
#Determine if it's a retweet or not, if not, add the occurances to the occur array
        if line.find('"retweeted":true') == -1: 
            for i in range(0, len(process)-1):
                occur[i] = occur[i] + process[i]
        elif line.find('"retweeted":true') != -1: 
            for i in range(0, len(process)-1):
                process[i] = 0
                process[8] = process[8] + 1
        else: 
            for i in range(0, len(process)-1):
                process[i] = 0
                process[8] = process[8] + 1
#return result
    return occur    


#Print result
'''
    print "Antalet forekomster av ordet han: " + str(process[0])
    print "Antalet forekomster av ordet hon: " + str(process[1])
    print "Antalet forekomster av ordet den: " + str(process[2])
    print "Antalet forekomster av ordet det: " + str(process[3])
    print "Antalet forekomster av ordet denna: " + str(process[4])
    print "Antalet forekomster av ordet denne: " + str(process[5])
    print "Antalet forekomster av ordet hen: " + str(process[6])
    print "Antal tweets: " + str(process[7])
    print "Antal retweets: " + str(process[8])
''' 
