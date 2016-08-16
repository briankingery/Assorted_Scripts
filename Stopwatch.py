import time

#   3 days 5hrs 30min   = 279000
#   1hr 12min           = 4320
#   53min               = 3189

print "Start"
start =time.clock()


# The time.sleep() will be replaced with what your script actually does
time.sleep(2)   

print "End"
end = time.clock()

Seconds = int(end - start)

Minutes = Seconds / 60
Hours   = Minutes / 60
Days    = Hours   / 24

seconds = int(Seconds - (Minutes*60)) 
minutes = int(Minutes - (Hours*60))   
hours   = int(Hours   - (Days*24)) 
days    = int(Days)  


if int(Days) == 0:
    if int(Hours) == 0:
        if int(Minutes) == 0:
            print "Total Seconds Ran: %ssec" % (seconds)
        else:
            print "Total time ran: %smin %ssec" % (minutes, seconds)
    else:
        print "Total time ran: %shrs %smin %ssec" % (hours, minutes, seconds)
else:
    print "Total time ran: %s Days %shrs %smin %ssec" % (days, hours, minutes, seconds)
