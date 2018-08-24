#!/bin/sh
# This code is for calculating the PBL using HYSPLIT software developed by ARL lab,USA


echo "enter the month"
read month



echo "enter the year"
read year

echo "enter the date"
read date

echo "which date you want to use for pbl calc"
read choice

if $choice == "1"
then

wget ftp://arlftp.arlhq.noaa.gov/pub/archives/edas40/edas.$month$year.$date


else 
echo "enter the week"
read week

wget ftp://arlftp.arlhq.noaa.gov/pub/archives/gdas1/gdas1.$month$year.$week
fi

