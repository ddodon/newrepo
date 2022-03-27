#!/bin/bash

#디렉토리 생성
mkdir temp
echo "...create temp directory..."

#파일 복사
cp cal.sh num1.txt num2.txt temp
echo "...copy files to temp directory..."

PS3='select menu: '
select op in "add" "sub" "div" "mul"
do
 echo "...add selected..."
 echo "...run calculater..."
 ./cal.sh $op
 break
done
