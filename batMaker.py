#
# create .bat file to create a CONTROL file. Do not run this program directly, 
# use jobFileLooper.py  as a starting point.
#
import os
import subprocess
import sys

class Bat(object):
	def __init__(self, spatial, dur, filePrefix):	
		self.basePath = "/home/suhail/python/code/hysplit-924/working/"         # set this once
		self.jobfile = "/home/suhail/python/code/hysplit-924/working/parker_r2.txt" # this gets over ridden
		self.loc = spatial 							
		self.dur = dur								
		self.numEdas = 2							
		self.edasPath = "/home/suhail/python/code/"	# EDAS input file path
		self.controlPath = "/home/suhail/python/code/hysplit-924/working/"	# place where control file will be placed
		self.savePath = "./"
		self.filePrefix = filePrefix 
		
		self.days = []
		self.mos = {"01":"jan","02":"feb","03":"mar","04":"apr","05":"may","06":"jun","07":"jul","08":"aug","09":"sep","10":"oct", "11":"nov", "12":"dec"} # need to add all months
		
	def setJobFile(self, jobfilename):
		'''set jobfile if code called exteranally - a string path\joblistname.lst, optional'''
		self.jobfile = jobfilename
	
	def setLonLat(self, loc):
		'''set lon and lat externally, when this file called - loc is a list with lon and lat, [lon,lat], optional'''
		self.loc = loc	
	
	def pathExistance(self, checkThis):
		print "- Checking existance of", checkThis,
		if not os.path.exists(checkThis):
			print "- Error: Directory cannot be found, verify path."
			sys.exit("... Ending Execution\n\n")
		else:
			print ", ... Path Correct."

		
	def export(self, s):
		fh = open("./win.bat", "w")
		fh.write(str(s) + "\n")
		fh.close()
		
	def readFile(self):
		# read contrl file
		try:
			fh = open(self.jobfile, "r")
			while True:
				line = fh.readline().rstrip()
				if line == "":
					break
				self.days.append(line)
			fh.close()
		except:
			print "-  Could not open/find job-file, check path and name"
			sys.exit("... Terminating")
			
	def mkEdas(self, ds):
		'''first line in control file, a year, month, day, and hour (UTC)'''
		yr, mo, da, strtHr= ds.split(" ")
		holding = "echo " + yr + " " + mo + " " + da + " " + str(strtHr) + " >CONTROL" 	# add date
		holding += "\necho 1 >>CONTROL"													# number of start heights, use one only		
		return holding
		
	def addLoc(self, s):
		'''second line, lon, lat and height'''
		lon, lat, hgt = self.loc
		s += "\necho " + str(lon)+ " " + str(lat) + " " + str(hgt) + " >>CONTROL"
		return s 
		
	def addDur(self, s):
		s += "\necho " + str(self.dur) + " >>CONTROL"
		return s
		
	def addTypeMixCalc(self, s):
		s += "\necho 0 >>CONTROL"
		return s
		
	def addTopMod(self, s):	
		s += "\necho 10000.0  >>CONTROL"
		return s
		
	def numOfEdasFiles(self, s):
		s += "\necho " + str(self.numEdas) + " >>CONTROL"
		return s		
		
	def addEdasFileName(self, s, month, dia, year):
		if int(dia) > 15:
			s += "\necho " + self.edasPath + " >>CONTROL"				# add path
			cur_month = self.mos[month]					
						
			if int(month)-1 == 0:
				b_month = self.mos[str("12")]
			else:
				b_month = self.mos[str(int(month)-1).zfill(2)]
				
			ext = ".002"
			s += "\necho edas." + cur_month + year + ext + " >>CONTROL"	# add 1st edas name, current
			s += "\necho " + self.edasPath + " >>CONTROL"				# add path
			ext = ".001"
			s += "\necho edas." + b_month + year + ext + " >>CONTROL"	# add 2nd edas name, past
		else:
			cur_month = self.mos[month]	
			s += "\necho " + self.edasPath + " >>CONTROL"				# add path							
			ext = ".001"
			s += "\necho edas." + cur_month + year + ext + " >>CONTROL"	# add 1st edas name
			s += "\necho " + self.edasPath + " >>CONTROL"				# add path
			ext = ".002"
			cur_month = self.mos[month]			
			if int(month)-1 == 0:
				b_month = self.mos[str("12")]
			else:
				b_month = self.mos[str(int(month)-1).zfill(2)]			 
			s += "\necho edas." + b_month + year + ext + " >>CONTROL" # add 2nd edas name		
		return s

	


	'''def addNamfilename(self, s, yy, mm, dd, HH):
		s += "\necho " + self.edasPath + " >>CONTROL"
		#fname = self.filePrefix + str(yy) + "_" + str(mm) + "_" + str(dd) + "_" + str(HH) + 
		#s += "\necho " + self.savePath + fname + ">>CONTROL"

		ext = "_nam12"
		s +=  "\necho " + '20' + yy + mm + dd + ext +" >>CONTROL"	# add 1st edas name current
		s += "\necho " + self.edasPath + " >>CONTROL"				# add path
		ext = "_nam12"
		s +=  "\necho " + '20' + yy + mm + str((int(dd)+1)) + ext +" >>CONTROL" 	# add 2n
		#s += "\necho " + self.edasPath + " >>CONTROL"
		return s'''

		
	def addControlPath(self, s):
		s += "\necho " + self.controlPath + " >>CONTROL"
		return s
		
	def addSaveLoc(self, s, yy, mm, dd, HH):
		fname = self.filePrefix + str(yy) + "_" + str(mm) + "_" + str(dd) + "_" + str(HH) + ".dat"
		s += "\necho " + self.savePath + fname + ">>CONTROL"
		return s
	
	def addHysplitExec(self, s):
		s += "\n/home/suhail/python/code/hysplit-924/exec/hyts_std"
		return s
		
	def callHysplit(self):
		#subprocess.call(['C:\hysplit4\tdump\win.bat', ''])
		os.system('/home/suhail/python/code/hysplit-924/working/win.bat')				
		
	def main(self):
		self.pathExistance(self.basePath)		
		os.chdir(self.basePath)
		self.readFile()
		
		for i in self.days:
			yr, mo, da, hr = i.split(" ")	
			print "Finished:", "Year =", yr,  "Month =",mo, "Day =", da, "Hour =", hr
			mos = self.mos[mo]			
			phrase = self.mkEdas(i)
			phrase = self.addLoc(phrase)
			phrase = self.addDur(phrase)
			phrase = self.addTypeMixCalc(phrase)
			phrase = self.addTopMod(phrase)
			phrase = self.numOfEdasFiles(phrase)
			phrase = self.addEdasFileName(phrase, mo, da, yr)
			
			#phrase = self.addNamfilename(phrase, yr, mo, da, hr)
			phrase = self.addControlPath(phrase)
			
			phrase = self.addSaveLoc(phrase, yr, mo, da, hr)
			phrase = self.addHysplitExec(phrase)
			self.export(phrase)
		
			self.callHysplit()
			
		
if __name__=="__main__":
	b = Bat()
	b.main()
