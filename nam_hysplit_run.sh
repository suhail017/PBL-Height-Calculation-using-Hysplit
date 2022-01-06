#!bin/bash
date=1


echo "enter the month in two digit format"
read month



#echo "enter the date"
#read date


echo "enter the year (Enter the last two digits of the year)"

read year


#Use the meterological files to caluculate the PBL for this region. We are using nam_12

#Check if the file exist ,if it is, don't download it again.



while [ $date -le 31 ]
do




#This is a code for retrieving the PBl using hysplit model. This code is a shell script based which can take input from the user and calculate the PBl and plot it . 




#Clear the input file before putting the desired date

cat /dev/null > /home/lester/Desktop/hysplit/hysplit-924/working/parker_r2.txt

#echo "\nEnter the month in digit"
#read mont
#mont=03

for time in  6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 
do
        echo "$year $month $date $time" >> /home/lester/Desktop/hysplit/hysplit-924/working/parker_r2.txt

done
for tim in 0 1 2 3 4 5 6
do
        echo "$year $month $((date+1)) $tim" >> /home/lester/Desktop/hysplit/hysplit-924/working/parker_r2.txt
done

#Delete the previous calculated the PBL

rm /hysplit-924/working/UTEP_*


#Delete the output file before new run

cat /dev/null > /home/lester/Desktop/hysplit/result/mix_hgts.txt

cat /dev/null > /home/lester/Desktop/hysplit/result/mix_hgts_sort.txt


#Run the python program, don't forget to add the working directory

python /home/lester/Desktop/hysplit/hysplit-924/working/jobFileLooper.py 


python /home/lester/Desktop/hysplit/hysplit-924/working/aggregator_hysplit.py


#Delete the output file before new run

cat /dev/null > /home/lester/Desktop/hysplit/hysplit-924/result/mix_hgts.txt

cat /dev/null > /home/lester/Desktop/hysplit/hysplit-924/result/mix_hgts_sort.txt

#Sort the output file in ascending order

(head -n 1; sort -nk1,2) < /home/lester/Desktop/hysplit/result/mix_hgts.txt 1<> /home/lester/Desktop/hysplit/result/mix_hgts_sort.txt

#cp -r /home/lester/Desktop/hysplit/result/mix_hgts_sort.txt /home/lester/Desktop/hysplit/summer2018/

#cd /home/lester/Desktop/hysplit/summer2018/2015/

#mv mix_hgts_sort.txt $month$date.txt

#plot the data using matplotlib


#python /home/lester/Desktop/hysplit/result/plott.py

date=$(($date+1))

done

