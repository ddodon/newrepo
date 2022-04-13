#!/usr/bin/python3

# OSP HW05 <Python Programming>
# 2016112414 문상돈

import sys

file = sys.argv[1]
text = open(file,"r")
num = int(sys.argv[2]) # 상위 몇 개 출력 할지
dic = {} #dictionary

lines = text.readlines() #파일을 한 줄 씩 읽어서 리스트에 저장

for line in lines:
	words = line.split()
	for word in words:
		word = ''.join(char for char in word if char.isalnum()) #문장부호 제거
		word = word.lower() #소문자
		if not word in dic:
			dic[word] = 1
		else:
			dic[word] += 1
result = list()
for k, v in dic.items():
	token = (v,k)
	result.append(token)
result = sorted(result,reverse=True) #내림차순

for v,k in result[:num]: #상위 num개 출력
	print("{:<7}{:>7}".format(k,v))
