#!bin/bash
date=1


echo "enter the month in two digit format (e.g- march = 03)"
read month



#echo "enter the date"
#read date


echo "enter the last two digits of the year"

read year

#Use the meterological files to caluculate the PBL for this region. We are using nam_12

#Check if the file exist ,if it is, don't download it again.



while [ $date -le 31 ]
do

FILE=$year$month'0'$date_'nam12'

if [[ -f "$FILE" ]] 
then
	echo "File  exist\n"

else

	if [ $date -le 10 ] 
	then

		wget ftp://ftp.arl.noaa.gov/archives/nam12/'20'$year$month'0'$date"_nam12"

	else 

		wget ftp://ftp.arl.noaa.gov/archives/nam12/'20'$year$month$date"_nam12"

	fi

fi


date=$(($date+1))

done

