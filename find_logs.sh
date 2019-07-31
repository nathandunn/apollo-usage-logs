#!/bin/bash
date=$1
echo $date


find report-logs -name $date\*  | xargs cat | grep production  | grep  running > logs_for_$date.txt

