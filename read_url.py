import html5lib
import urllib2

aResp = urllib2.urlopen("https://uniservices1.uobgroup.com/secure/online_rates/gold_and_silver_prices.jsp")
t = aResp.read()
dom = html5lib.parse(t, treebuilder="dom")
trlist = dom.getElementsByTagName("PAMP GOLD BARS WITH HOOK")
print trlist
#print trlist[-3].childNodes[1].firstChild.childNodes[0].nodeValue

# import urllib
# import urllib2
# import re
#
# def Connect2Web():
#   aResp = urllib2.urlopen("https://uniservices1.uobgroup.com/secure/online_rates/gold_and_silver_prices.jsp")
#   web_pg = aResp.read()
#   #print web_pg
#
#   pattern = "<td><b>PAMP GOLD BARS WITH HOOK</b></td>" + "<td>(.*)</td>" * 4
#   print pattern
#   m = re.search(pattern, web_pg)
#   if m:
#     print "PAMP GOLD BARS WITH HOOK:"
#     print "\tCurrency:", m.group(1)
#     print "\tUnit:", m.group(2)
#     print "\tBank Sells:", m.group(3)
#     print "\tBank Buys:", m.group(4)
#   else:
#     print "Nothing found"
#
# Connect2Web()