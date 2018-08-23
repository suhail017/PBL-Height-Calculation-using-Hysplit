# class to aggregate hysplit output
import os
import sys
from os import listdir
from os.path import isfile, join


class HysplitAgg(object):
	def __init__(self, dataPath, outPath):
		self.dataPath = dataPath
		self.joblists = []
		self.outputPath = outPath 
		self.dat = []
		self.pathExistance(dataPath)
		self.pathExistance(outPath)
		self.mix = []
		
	def pathExistance(self, checkThis):
		#print "- Checking existance of", checkThis
		print "- Checking Paths"
		if not os.path.exists(checkThis):
			print "- Error: Directory cannot be found, verify path", checkThis
			sys.exit("... Ending Execution\n\n")
		else:
			print "- path exists"	
		
		
	def readFiles(self):
		""" reads jobe files """
		os.chdir(self.dataPath)
		fileList_0 = [f for f in listdir(self.dataPath) if isfile(join(self.dataPath, f))]
		
		##i = 0
		for line in fileList_0:
			##i =+ 1
			if line[-4: len(line)] == ".dat": 
				self.joblists.append( line.rstrip() )
			##if i == 1: break
		print "- Processing ", len(self.joblists), "files..."
		
	
	def readHysplitFile(self, j, outfname):
		'''
		Does read hysplit output but also writes them in a
		column/row file.
		'''
		# open file in joblist to READ a HYSPLIT file
		dfh = open(j.strip(), "r")
			
		# skip 6 lines, the header stuff I don't need
		for s in range(4):
			discard = dfh.readline()
			
		timeline = dfh.readline()
		first_date = "20" + timeline[1:6].strip().zfill(2) + timeline[7:13].strip().zfill(2) +\
				timeline[14:20].strip().zfill(2)
				
		for x in range(1):
			discard = dfh.readline()
			
		# process the data I do need
		lineIndex = 0
		
		# open file to WRITE
		fho = open(outfname, "w")
		
		while True:
			lineIndex += 1				
			line = dfh.readline().rstrip()
			if line == "": break
			fho.write(first_date+","+"20"+line[15:19].strip()+line[23:25].strip().zfill(2)+line[29:31].strip().zfill(2)+","\
			+line[66:75].strip() +","+ line[58:66].strip() +","+ line[76:84].strip() +","+ line[85:93].strip()\
			+","+ line[94:102].strip() +","+ line[50:57].strip()+","+ line[103:111].strip() +","+ line[112:120].strip() \
			+","+ line[121:129].strip() +","+ str(lineIndex) + "\n")
		dfh.close()
		fho.close()
		
		
	def read_first_line(self, fname):
		# open file in joblist to READ a HYSPLIT file
		dfh = open(fname.strip(), "r")
			
		# skip 6 lines, the header stuff I don't need
		for s in range(4):
			discard = dfh.readline()
		
		# still in the header section
		timeline = dfh.readline()	
		
		grp_date = "20" + timeline.strip()[0:4].strip() + timeline.strip()[4:9].strip().zfill(2) + timeline.strip()[12:14].strip().zfill(2)
		grp_hour = timeline[21:24].strip().zfill(2)
		
		for x in range(1):
			discard = dfh.readline()			

		dataLine = []	
		line = dfh.readline().rstrip()
		
		trj_date = "20" + line[14:19].strip().zfill(2) + line[21:26].strip().zfill(2) + line[26:32].strip().zfill(2) 
		trj_hour = line[32:37].strip().zfill(2)
		trj_lon = line[66:75].strip()
		trj_lat = line[59:66].strip()
		trj_hgt = line[76:84].strip()  #trajectory height
		trj_mix = line[94:102].strip() #mixing ratio
		trj_rh = line[103:112].strip() #RELHUMID 
		trj_mixratio = line[112:120].strip() #H2OMIXRA 
		trj_sol = line[121:129].strip() #SUN_FLUX
		
		dataLine = [grp_date, grp_hour, trj_date, trj_hour, trj_hgt, trj_mix]
		return dataLine
			
	
	def read_one_hysplitFile(self, fname):
		""" reads one HYSPLIT file, takes file name as argument """
		# open file in joblist to READ a HYSPLIT file
		dfh = open(fname.strip(), "r")
			
		# skip 6 lines, the header stuff I don't need
		for s in range(4):
			discard = dfh.readline()
		
		# still in the header section
		timeline = dfh.readline()	
		
		grp_date = "20" + timeline.strip()[0:4].strip() + timeline.strip()[4:9].strip().zfill(2) + timeline.strip()[12:14].strip().zfill(2)
		grp_hour = timeline[21:24].strip().zfill(2)
		
		for x in range(1):
			discard = dfh.readline()
			
		# process the data I do need
		lineIndex = 0	
		
		while True:
			lineIndex += 1				
			line = dfh.readline().rstrip()
			if line == "": break
			trj_date = "20" + line[14:19].strip().zfill(2) + line[21:26].strip().zfill(2) + line[26:32].strip().zfill(2) 
			trj_hour = line[32:37].strip().zfill(2)
			trj_lon = line[66:75].strip()
			trj_lat = line[59:66].strip()
			trj_hgt = line[76:84].strip()  #trajectory height
			trj_mix = line[94:102].strip() #mixing ratio
			trj_rh = line[103:112].strip() #RELHUMID 
			trj_mixratio = line[112:120].strip() #H2OMIXRA 
			trj_sol = line[121:129].strip() #SUN_FLUX
			self.dat.append([ grp_date, grp_hour, trj_date, trj_hour, trj_lon, trj_lat, trj_hgt, trj_mix, trj_rh, trj_mixratio, trj_sol ])		
			
		if lineIndex < 8:
			print "- Missing data in file, remove file", fname
		
		print fname, "has", lineIndex-1, "usable observations"
		dfh.close()
		
		
	def getTrjData(self):
		return self.dat
		
		
	def makeTrjFiles(self):
		numfiles = 0
		for j in self.joblists:
			numfiles += 1
			#print str(numfiles) + ".", "processing",j + "..."
			e=[]
			
			# make output file name
			outfname =  self.outputPath + j[:-4] + ".btrj"
			self.readHysplitFile(j, outfname)
		
		
	def makeAggregatedFile(self):
		''' this makes a file '''
		numfiles = 0
		c = "\t"
		
		# export file
		fho = open(self.outputPath + "All_Trajectories.txt", "w")
		fho.write("grp_date" +c+ "grp_hour" +c+ "trj_date" +c+ "trj_time" +c+ "lon" +c+ "lat" +c+ "alt" +c+ "pres" +c+ "mix" +c+ "rh" +c+ "h2o_mix_ratio" +c+ "solar" + "\n") 
		
		for j in self.joblists:
			numfiles += 1			
			data = []
			p.read_one_hysplitFile(j)
			data = p.getTrjData()		
		
			numrec = 0
			for j in data:
				numrec += 1
				fho.write( str(j[0]) + "\t" + str(j[1]) + "\t" + str(j[2])  + "\t" + str(j[3]) + "\t" + str(j[4])\
						   + "\t" + str(j[5])  + "\t" + str(j[6])  + "\t" + str(j[7]) + "\t" + str(j[8])  + "\t" + str(j[9])\
						   + "\t" + str(j[10]) + "\n")
				#print j[0]
			if numrec < 6:
				print "- File", j, "has less than 6 records, only", numrec-1
			numrec = 0	
		fho.close()
		print numfiles, "processed files, Done"
		
		
	def takeMixHgt(self):
		numfiles = 0
		for j in self.joblists:
			numfiles += 1			
			dline = []
			dline = p.read_first_line(j)		
			self.mix.append(dline)
			
		# write to file	
		c = "\t"	
		header = "date" +c+ "hour" +c+ "trj_hgt" +c+ "trj_mix" + "\n"
		fho = open(self.outputPath + "mix_hgts.txt", "w")
		fho.write(header)
		for i in self.mix:
			fho.write( str(i[0]) +c+  str(i[1]) +c+ str(i[4]) +c+ str(i[5]) + "\n")
		fho.close()
		print "- File mix_hgts.txt has been written, done."
		
		
if __name__ == "__main__":
	# user inputs
	in_path = "X:\\projects\\fernando\\Dallas\\DFW_2017_ConceptModel\\cart\\2016_special_endpts\\good_dotDats\\Hr18utc\\"
	out_path = "C:\\Users\\fmercado\\Desktop\\test\\"

	p = HysplitAgg(in_path, out_path)
	p.readFiles() 
	p.takeMixHgt()
	
	