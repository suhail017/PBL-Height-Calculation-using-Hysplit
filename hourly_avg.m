clc
close all
% clear all

%% Reading the file
%  filename = uigetfile;
%  file = importdata(filename);
BL_height = zeros(length(file.data(:,5)),3);
BL_height(:,1) = file.data(:,5);
BL_height(:,2) = file.data(:,6);
BL_height(:,3) = file.data(:,7);
BL_height(BL_height==-999)=0;

bl1 = BL_height(:,1);
bl1(bl1==-999)=0;
bl2 = BL_height(:,2);
bl2(bl2==-999)=0;
bl3 = BL_height(:,3);
bl3(bl3==-999)=0;

% return
% %% Declaring the variables

n = 224;
%  hour =zeros(100);
s = 1:n:length(BL_height(:,1));

bl=bl2;
 %hour =BL_height_1(s(1):s(2));
 mean_hour = zeros(24,3);

for x=1:length(s)-1
     for i = 1:length(BL_height(1,:))
%         hour(:,x) = BL_height(s(x):s(x+1),i);
         hour(:,x) = bl(s(x):s(x+1));
%          mean_hour(:,i) = mean(hour) ;
        mean_hour = mean(hour);
%             mean_hour=mean_hour(:);
    end
end

time = 0:1:23;
% time = time(:);

A = [time ; mean_hour];

if bl ==bl1
    
    fileID = fopen('BL_height_BL1.txt','w');
    fprintf(fileID,'%6s %12s\r\n','time','mean_hour');
    fprintf(fileID,'%6.2f %12.8f\r\n',A);
    fclose(fileID);
    
else
    fileID = fopen('BL_height_BL2.txt','w');
    fprintf(fileID,'%6s %12s\r\n','time','mean_hour');
    fprintf(fileID,'%6.2f %12.8f\r\n',A);
    fclose(fileID);
    
end
    
    