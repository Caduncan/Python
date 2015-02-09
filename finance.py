print "welcome to the stock ticker program"
import csv
highest_level = None
try:
f= csv.reader (pen('dow_pices.csv'))
except:
    print "could not open dow_prices.csv file"
    print "ending program "
    raw_input("\n\nPress the enter key to extit out of the program")
else:
    column = zip(*f)
    date = columns[0]
    start = columns[1]
    high = columns [2]
    low = columns [3]
    close = columns [4]
    vol = columns [5]
    adj_close = columns [6]
    print "The highest point in the Dow in 2011 was at" max(high)
    print "The lowest poin in the Dow in 2011 was at" min(low)
    raw_input ("\n\n\Press the enter key to exit out of the progam")
