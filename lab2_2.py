import sys
import math

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

couplet = (x - 1) * "la-"
couplet = couplet + "la"
if z == 1 :
	end = "!"

elif z == 0 :
	end = "."

n = 0
if y != 0 :
	n = 1

song = (couplet + " ") * (y-1) + couplet * n  + end

print "Everybody sing a song: " + song
