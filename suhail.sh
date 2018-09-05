#!/bin/sh
#!/bin/sh

echo "enter the month (Enter the first 3 letter of the month)"
read month



echo "enter the year (Enter the first two digits of the year)"
read year

echo "enter the date"
read date




echo "Enter the Meterological file you want to use for PBL. 
> 1=EDAS
> 2=GDAS
> 3=HRRR"

read choice

FILE=edas.$month$year.001 || edas.$month$year.002
if [ -e "/home/lester/Desktop/hysplit/$FILE" ]
then
echo "File  exist\n"

else

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





fi

cat /dev/null > /home/lester/Desktop/hysplit/hysplit-924/working/parker_r2.txt

echo "\nEnter the month in digit"
read mont

for time in 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
do
	echo "$year $mont $date $time" >> /home/lester/Desktop/hysplit/hysplit-924/working/parker_r2.txt
done

rm hysplit-924/working/UTEP_*
python /home/lester/Desktop/hysplit/hysplit-924/working/jobFileLooper.py 


python /home/lester/Desktop/hysplit/hysplit-924/working/aggregator_hysplit.py

sort  -k2,4 -n /home/lester/Desktop/hysplit/result/mix_hgts.txt


