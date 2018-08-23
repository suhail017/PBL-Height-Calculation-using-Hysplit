#
# pass .lst files to batMaker.py, for multiple .lst files.
#
import batMaker

# a python list with lat, lon and height - starting location
receptor_loc = [31.768291,-106.501260,600.0]	# add you lat (deg), lon (deg) and height (meters), here


# file prefix output - user supplied
filePrefix = "UTEP_"


# duration of trajectory in hours, negative sign implies a back trajectory
duration = -72

# list jobs below as a python list, can have path included.  See supplied example.  Variables 
# are 2-digit year, 2-digit month, 2-digit day and a 2-digit start hour (UTC).
lst = ["parker_r2.txt"]


#### do not change anything below here ####
p = batMaker.Bat(receptor_loc, duration, filePrefix)

for i in lst:
	p.setJobFile(i)
	p.main()
