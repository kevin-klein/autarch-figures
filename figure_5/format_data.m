%%Script for processing and standardizing raw outline data from AutArch
%input: raw artifact outline data in json format (file named 'graves.json')
%output: outline data formatted for EFA analysis in PAST (variable named 'RAWpast')


%add all folders and subfolders to working directory
    addpath(genpath(pwd))

%load data from json file
    dat=loadjson([pwd,'\graves.json']);

%extract raw outline data in cell format
    for i = 1:length(dat)
        raw{i} = [dat(1,i).scaled_coordinates(:,1),dat(1,i).scaled_coordinates(:,2),zeros(length(dat(1,i).scaled_coordinates(:,1)),1)];
    end

%reformat data to equal number of coordinates
    for i = 1:length(raw)
        %resize array to r number of coordinates
            r=249;
            x = imresize(raw{1,i}(:,1),r/length(raw{1,i}(:,1))); x=x(1:249);
            y = imresize(raw{1,i}(:,2),r/length(raw{1,i}(:,2))); y=y(1:249);
        %close contour: duplicate first coordinate as final coordinate
            x(end+1) = raw{1,i}(1,1); y(end+1) = raw{1,i}(1,2);
    RAW{i} = [x,y];
    end

%reformat for LDA function in PAST 
    for i=1:length(RAW)
        A=RAW{1,i}(:,1)'; B=RAW{1,i}(:,2)';
        C = [A(:) B(:)]';
        RAWpast(i,:) =  C(:);
    end

open RAWpast