# Hysplit-PBL-calculation
Compute the PBL using hysplit 

## Methods:

we are using different meterolgical dataset to compute the PBLH for specific lat, lon and height. To execute the process, we are using the Linux version of Hysplit which takes input from the user and calculate the PBLH for given day or month of the year.  

## PBLH Calculation using NAM met file:

You will require two different file called `download_nam.sh` and `nam_hysplit_run.sh` to execute the process. `download_nam.sh` will download the required nam files from the FTP server of hysplit. It will ask for two inputs from the user, one is the month in two-digit format, another is the year. Keep in mind that it will download an entire month's worth of data, so it will take a little longer to complete.

When the download is complete, you need to run the second shell script file named `nam_hysplit_run.sh`. It will ask for the same input, so you must input the month and the year. You need to have sudo access to run those script, so please type those line to execute the program:

`sudo sh download_nam.sh`

`sudo sh nam_hysplit_run.sh`

Output will be in a .txt file called mix_hgts_sort.txt in the same directory. Please note you need to run both scripts from the directory of the hysplit computer.
