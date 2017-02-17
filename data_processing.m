clear all;
%%Read each file in each directory.  Add. Average.  Format.  Next directory

directories = ['Y1'; 'Y2'; 'Y3'; 'Y4'; 'Y5'; 'Y6'; 'Y7'; 'Y8']
%directories = ['y 18.5'; 'y 48.5'; 'y 78.5'; 'y 108.5'; 'y 138.5'; 'y 168.5'; 'y 198.5'; 'y 228.5']
% files = ['DATALOG0.TXT'; 'DATALOG1.TXT'; 'DATALOG2.TXT'; 'DATALOG3.TXT';...
%          'DATALOG4.TXT'; 'DATALOG5.TXT'; 'DATALOG6.TXT'; 'DATALOG7.TXT';...
%          'DATALOG8.TXT'; 'DATALOG9.TXT']
file = ['DATALOGS.xlsx']
compilationfile = 'Feb_16_2017 XYPHI Data and Corrections.xlsx';
sheets = [1; 2; 3; 4; 5; 6; 7; 8; 9; 10]
samplesize = 10;
collection = zeros(208, 18, 8);
for d = 1:length(directories)
    filename = cat(2, directories(d,:), '/', file)
    datalog = zeros(208, 18)
    datalogavg = zeros(208, 18);
    samplelog = zeros(208, 18, 10);
    stdlog = zeros(209, 18);
    saslog = zeros(209, 18);
    for s = 1:length(sheets) 
        samplelog(:, :, s) = xlsread(filename, s);
        datalog = datalog + samplelog(:, :, s);
    end
    datalogavg = datalog/10;
    if d == 1
        datalogavg(:, 1) = datalogavg(:, 1) + 0.2;
    end
    if d == 1 || d == 2 || d == 3
        angleoff = 15;
        ir1 = 0;
        ir2 = 0;
        ir3 = 0;
        ir4 = 0;
        ir5 = 0;
        ir6 = 0;
        ir7 = 0;
        for i = 1:208
            ir1 = i + angleoff;
            ir2 = i + angleoff - 2;
            ir3 = i + angleoff - 4;
            ir4 = i + angleoff - 6;
            ir5 = i + angleoff - 8;
            ir6 = i + angleoff - 10;
            ir7 = i + angleoff - 12;
            if ir7 < 1
                ir7 = ir1 + 4;
            end
            if ir6 < 1
                ir6 = ir7 + 2;
            end
            if ir5 < 1
                ir5 = ir6 + 2;
            end
            if ir4 < 1
                ir4 = ir5 + 2;
            end
            if ir3 < 1
                ir3 = ir4 + 2;
            end
            if ir2 < 1
                ir2 = ir3 + 2;
            end
            if ir1 < 1
                ir1 = ir2 + 2;
            end
            datalogavg(i, 17) = mean([datalogavg(ir1, 3);...
                                      datalogavg(ir2, 5);...
                                      datalogavg(ir3, 7);...
                                      datalogavg(ir4, 9);...
                                      datalogavg(ir5, 11);...
                                      datalogavg(ir6, 13);...
                                      datalogavg(ir7, 15);]);
            angleoff = angleoff - 2;
            if mod(i, 16) == 0
                angleoff = 15;
            end
        end
    end
    collection(:, :, d) = datalogavg;
    %By here we have the averages for this y, as well as all individual
    %values.  Thus, we can comput stdv (sample) for this y.
    for i = 1:208
        for j = 1:18
            for s = 1:length(sheets)
                saslog(i+1, j) = (samplelog(i, j, s) - datalogavg(i, j)).^2;
            end
        end
    end
    %Square root of (the squares of the sum of differences, divided by N-1)
    stdlog = sqrt(saslog/(samplesize - 1));
    xlswrite(compilationfile, stdlog, d+1);
end

compilation = zeros(208 * length(directories) + 1, 19);

count = 2;
colindx = 1;

for x = 1:13
    colindx = ((x-1) * 16) + 1;
    for y = 1:length(directories)
        for phi = 1:16%0:15
                compilation(count, 1)     = collection(colindx, 1, y);    %X
                compilation(count, 2)     = 18.5 + ((y-1) * 30);          %Y
                compilation(count, 3)     = collection(colindx, 2, y);    %PHI
                compilation(count, 4:end) = collection(colindx, 3:end, y);%DATA
                count = count + 1;
                colindx = colindx + 1;
        end
        colindx = ((x-1) * 16) + 1;
    end
end

xlswrite(compilationfile, compilation, 1);