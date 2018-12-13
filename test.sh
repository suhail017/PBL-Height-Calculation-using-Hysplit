
#!/bin/bash


>data.txt

line1=$(tail -1 CAN.txt | awk '{print $4}')
#echo $line1
A="$(cut -d'/' -f2 <<<"$line1")"
echo $A >> data.txt


line2=$(tail -1 NCAL.txt | awk '{print $4}')
#echo $line2
B="$(cut -d'/' -f2 <<<"$line2")"
echo $B >> data.txt


line3=$(tail -1 OH.txt | awk '{print $4}')
#echo $line3
C="$(cut -d'/' -f2 <<<"$line3")"
echo $C >> data.txt


line4=$(tail -1 NV.txt | awk '{print $4}')
#echo $line4
D="$(cut -d'/' -f2 <<<"$line4")"
echo $D >> data.txt

line5=$(tail -1 ORG.txt | awk '{print $4}')
#echo $line5
E="$(cut -d'/' -f2 <<<"$line5")"
echo $E >> data.txt


#if [ "$A" -lt "$B" ] && [ "$A" -lt "$C" ] && [ "$A" -lt "$D" ] && [ $A -lt $E ]
#if [ 1 -eq "$(echo "${A} < ${B}" | bc)" ]
# then
#echo "CAN is the lowest one"
#else 
#echo "CAN is not the lowest"

awk 'END { print min," is The minimum value"}
{ 
  min || min = $1
  s || s = NR
  if ($1 < min) {min=$1; s=NR} 
  }' data.txt


