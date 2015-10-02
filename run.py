from tasks import wordcount

compresult = [0,0,0,0,0,0,0,0]

tweet1  = 'http://smog.uppmax.uu.se:8080/swift/v1/tweets/tweets_1.txt'
tweet2  = 'http://smog.uppmax.uu.se:8080/swift/v1/tweets/tweets_2.txt'
tweet3  = 'http://smog.uppmax.uu.se:8080/swift/v1/tweets/tweets_3.txt'
tweet4  = 'http://smog.uppmax.uu.se:8080/swift/v1/tweets/tweets_4.txt'
tweet5  = 'http://smog.uppmax.uu.se:8080/swift/v1/tweets/tweets_5.txt'
tweet6  = 'http://smog.uppmax.uu.se:8080/swift/v1/tweets/tweets_6.txt'
tweet7  = 'http://smog.uppmax.uu.se:8080/swift/v1/tweets/tweets_7.txt'
tweet8  = 'http://smog.uppmax.uu.se:8080/swift/v1/tweets/tweets_8.txt'
tweet9  = 'http://smog.uppmax.uu.se:8080/swift/v1/tweets/tweets_9.txt'
tweet10  = 'http://smog.uppmax.uu.se:8080/swift/v1/tweets/tweets_10.txt'
tweet11  = 'http://smog.uppmax.uu.se:8080/swift/v1/tweets/tweets_11.txt'
tweet12  = 'http://smog.uppmax.uu.se:8080/swift/v1/tweets/tweets_12.txt'
tweet13  = 'http://smog.uppmax.uu.se:8080/swift/v1/tweets/tweets_13.txt'
tweet14  = 'http://smog.uppmax.uu.se:8080/swift/v1/tweets/tweets_14.txt'
tweet15  = 'http://smog.uppmax.uu.se:8080/swift/v1/tweets/tweets_15.txt'
tweet16  = 'http://smog.uppmax.uu.se:8080/swift/v1/tweets/tweets_16.txt'
tweet17  = 'http://smog.uppmax.uu.se:8080/swift/v1/tweets/tweets_17.txt'
tweet18  = 'http://smog.uppmax.uu.se:8080/swift/v1/tweets/tweets_18.txt'
tweet19  = 'http://smog.uppmax.uu.se:8080/swift/v1/tweets/tweets_19.txt'


result1 = wordcount.delay(tweet1)
result2 = wordcount.delay(tweet2)
result3 = wordcount.delay(tweet3)
result4 = wordcount.delay(tweet4)
result5 = wordcount.delay(tweet5)
result6 = wordcount.delay(tweet6)
result7 = wordcount.delay(tweet7)
result8 = wordcount.delay(tweet8)
result9 = wordcount.delay(tweet9)
result10 = wordcount.delay(tweet10)
result11 = wordcount.delay(tweet11)
result12 = wordcount.delay(tweet12)
result13 = wordcount.delay(tweet13)
result14 = wordcount.delay(tweet14)
result15 = wordcount.delay(tweet15)
result16 = wordcount.delay(tweet16)
result17 = wordcount.delay(tweet17)
result18 = wordcount.delay(tweet18)
result19 = wordcount.delay(tweet19)



while result1.ready() and result2.ready() and result3.ready() and result4.ready() and result5.ready() and result6.ready() and result7.ready() and result8.ready() and result9.ready() and result10.ready() and result11.ready() and result12.ready() and result13.ready() and result14.ready() and result15.ready() and result16.ready() and result17.ready() and result18.ready() and result19.ready():
    print "Not ready"

for i in range(0, len(compresult)):
    compresult[i] = result1[i] + result2[i] + result3[i] + result4[i] + result5[i] + result6[i] + result7[i] + result8[i] + result9[i] + result10[i] + result11[i] + result12[i ] + result13[i] + result14[i] + result15[i] + result16[i] + result17[i] + result18[i] + result19[i]
        

print "Antalet forekomster av ordet han: " + str(compresult[0])
print "Antalet forekomster av ordet hon: " + str(compresult[1])
print "Antalet forekomster av ordet den: " + str(compresult[2])
print "Antalet forekomster av ordet det: " + str(compresult[3])
print "Antalet forekomster av ordet denna: " + str(compresult[4])
print "Antalet forekomster av ordet denne: " + str(compresult[5])
print "Antalet forekomster av ordet hen: " + str(compresult[6])
print "Antal tweets: " + str(compresult[7])
print "Antal retweets: " + str(compresult[8])
