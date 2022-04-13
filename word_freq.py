#!/usr/bin/python

import sys

file = sys.argv[1]
text = open(file,"r")
num = sys.argv[2] # 상위 몇 개 출력 할지

word = text.read().split()

dic = {} #dictionary

for w in word:
	if not w in dic:
		dic[w] = 1
	else:
		dic[w] += 1

print(result[:num])#상위 num개 출력

