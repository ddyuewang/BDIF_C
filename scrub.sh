#!/bin/bash
export datamonth=0
while [ $datamonth -lt 1 ]; do
let datamonth=datamonth+1
newdatamonth=`echo $datamonth | awk '{printf("%02d",$1)}'`
echo "aws s3 cp s3://bdif-tweets/cleaned/cleaned_2013_$newdatamonth.tar.gz 2013_$newdatamonth.tar.gz"
aws s3 cp s3://bdif-tweets/cleaned/cleaned_2013_$newdatamonth.tar.gz 2013_$newdatamonth.tar.gz
done

