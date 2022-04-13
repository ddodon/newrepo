#!/usr/bin/python

import sys

file = sys.argv[1]
text = open(file,"r")
num = sys.argv[2] # 상위 몇 개 출력 할지
dic = {} #dictionary

lines = text.readline()

for line in lines:
	for word in line.split():
		if not word in dic:
			dic[word] = 1
		else:
			dic[word] += 1
result = sorted(dic.item(),key=lambda x: x[1],reverse=True)

print(result[:num])#상위 num개 출력

