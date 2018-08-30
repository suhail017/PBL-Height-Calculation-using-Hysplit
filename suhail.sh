#!/bin/sh

echo "enter the month (Enter the first 3 letter of the month)"
read month



echo "enter the year (Enter the first two digits of the year)"
read year

echo "enter the date"
read date

echo "$year $month $date" >> hudai.txt 


echo "Enter the Meterological file you want to use for PBL. 
> 1=EDAS
> 2=GDAS
> 3=HRRR"

echo "which file you want to use for pbl calc"
read choice

if [ $choice -eq 1  ] &&  [ $date -lt 15 ]
then
wget ftp://arlftp.arlhq.noaa.gov/pub/archives/edas40/edas.$month$year.001
fi

if [ $choice -eq 1  ] &&  [ $date -ge 15 ]
then
wget ftp://arlftp.arlhq.noaa.gov/pub/archives/edas40/edas.$month$year.002
fi






if [ $choice -eq 2 ]
then

echo "enter the week (If the date is from 1-7,enter w1,If it's from 8-15,enter w2 and so on)"
read week

wget ftp://arlftp.arlhq.noaa.gov/pub/archives/gdas1/gdas1.$month$year.$week
fi


