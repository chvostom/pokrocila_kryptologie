#skript se musí nacházet ve složce sts2.1.2 spolu se soubory f0 až f3
#!/bin/bash
for i in "f0" "f1" "f2" "f3"
do
    echo 0 > input1
    echo "../$i" >> input1
    echo 0 >> input1
    echo 111111111010010 >> input1
    echo 1 >> input1
    echo 125 >> input1
    echo 4 >> input1
    echo 5 >> input1
    echo 5 >> input1
    echo 5 >> input1
    echo 0 >> input1
    echo 576 >> input1
    echo 0 >> input1
    ./assess 9375 < input1
    mkdir -p ../Results/$i/
    cp -R experiments/AlgorithmTesting/Frequency ../Results/$i/
    cp -R experiments/AlgorithmTesting/BlockFrequency ../Results/$i/
    cp -R experiments/AlgorithmTesting/CumulativeSums ../Results/$i/
    cp -R experiments/AlgorithmTesting/Runs ../Results/$i/
    cp -R experiments/AlgorithmTesting/LongestRun ../Results/$i/
    cp -R experiments/AlgorithmTesting/Rank ../Results/$i/
    cp -R experiments/AlgorithmTesting/FFT ../Results/$i/
    cp -R experiments/AlgorithmTesting/NonOverlappingTemplate ../Results/$i/
    cp -R experiments/AlgorithmTesting/OverlappingTemplate ../Results/$i/
    cp -R experiments/AlgorithmTesting/ApproximateEntropy ../Results/$i/
    cp -R experiments/AlgorithmTesting/Serial ../Results/$i/
    cp -R experiments/AlgorithmTesting/finalAnalysisReport.txt ../Results/$i/finalAnalysisReportPart1.txt
    cp -R experiments/AlgorithmTesting/freq.txt ../Results/$i/freqPart1.txt
    rm input1
    echo 0 > input2
    echo "../$i" >> input2
    echo 0 >> input2
    echo 000000000100000 >> input2
    echo 12 >> input2
    echo 0 >> input2
    ./assess 450000 < input2
    cp -R experiments/AlgorithmTesting/Universal ../Results/$i/
    cp -R experiments/AlgorithmTesting/finalAnalysisReport.txt ../Results/$i/finalAnalysisReportPart2.txt
    cp -R experiments/AlgorithmTesting/freq.txt ../Results/$i/freqPart2.txt
    rm input2
    echo 0 > input3
    echo "../$i" >> input3
    echo 0 >> input3
    echo 000000000001101 >> input3
    echo 1 >> input3
    echo 1000 >> input3
    echo 0 >> input3
    echo 5 >> input3
    echo 0 >> input3
    ./assess 1080000 < input3
    cp -R experiments/AlgorithmTesting/RandomExcursions ../Results/$i/
    cp -R experiments/AlgorithmTesting/RandomExcursionsVariant ../Results/$i/
    cp -R experiments/AlgorithmTesting/LinearComplexity ../Results/$i/
    cp -R experiments/AlgorithmTesting/finalAnalysisReport.txt ../Results/$i/finalAnalysisReportPart3.txt
    cp -R experiments/AlgorithmTesting/freq.txt ../Results/$i/freqPart3.txt
    rm input3
done
