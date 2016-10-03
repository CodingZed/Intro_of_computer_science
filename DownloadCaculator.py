# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download 
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size 
# is given in megabytes (MB).

#My Solution, Feel free to optimize it. Thanks a lot 

def convert_to_bits(size, unit):
    powers = [['k', 10], ['M', 20], ['G', 30], ['T', 40], ['B', 3]]
    unit = list(unit)
    exponent, i = 0, 0
    while i < len(powers):
        j = 0
        while j < len(unit):
            if powers[i][0] == unit[j]:
                exponent += powers[i][1]
            j+=1
        i += 1
    return float(size * 2**exponent)


def download_time(file,file_unit,bandwidth,bandwidth_unit):
    file=convert_to_bits(file,file_unit)
    bandwidth=convert_to_bits(bandwidth,bandwidth_unit)
    time=file/bandwidth
    
    #time transfer
    hor=(int(time/3600))
    minu=int((time-(hor*3600))/60)
    seg=time-((hor*3600)+(minu*60))
    if hor == 1 and minu == 1 and seg == 1:
        return "%s hour, %s minute, %s second" % (hor, minu, seg)
    elif hor==1 and minu == 1 and seg!=1:
        return "%s hour, %s minute, %s seconds" % (hor, minu, seg)
    elif hor==1 and minu != 1 and seg!=1:
        return "%s hour, %s minutes, %s seconds" % (hor, minu, seg)    
    elif hor!=1 and minu != 1 and seg!=1:
        return "%s hours, %s minutes, %s seconds" % (hor, minu, seg)
    elif hor==1 and minu != 1 and seg==1:
        return "%s hour, %s minutes, %s second" % (hor, minu, seg)
    elif hor!=1 and minu == 1 and seg==1:
        return "%s hours, %s minute, %s second" % (hor, minu, seg)
    elif hor!=1 and minu != 1 and seg==1:
        return "%s hours, %s minutes, %s second" % (hor, minu, seg)
    elif hor!=1 and minu == 1 and seg!=1:
        return "%s hours, %s minute, %s seconds" % (hor, minu, seg)
    
    
    
    



print download_time(1024,'kB', 1, 'MB')
#>>> 0 hours, 0 minutes, 1 second

print download_time(1024,'kB', 1, 'Mb')
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print download_time(13,'GB', 5.6, 'MB')
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print download_time(13,'GB', 5.6, 'Mb')
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print download_time(10,'MB', 2, 'kB')
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print download_time(10,'MB', 2, 'kb')
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable


